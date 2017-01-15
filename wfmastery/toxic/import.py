
import db
from data import data_v1 as d1
from parse_wikia_primes import main as primes_main
from parse_wikia_primes import Rarity


def reconcile_primes(NewTRX):
    by_name, tiers, relics, names, url_map = primes_main()

    rarity_map = {}
    tier_map = {}
    relics_map = {}

    with db.scope(NewTRX) as session:

        for pos, rarity in enumerate(Rarity, 1):
            obj_rare = db.Rarity(id=pos, name=rarity.name)
            rarity_map[rarity.name] = obj_rare
            session.add(obj_rare)

        for pos, tier_name in enumerate(tiers, 1):
            obj_relic_tier = db.RelicTier(id=pos, name=tier_name)
            tier_map[tier_name] = obj_relic_tier
            session.add(obj_relic_tier)

        for pos, relic_name in enumerate(relics, 1):
            relic_obj = db.RelicName(id=pos, name=relic_name)
            relics_map[relic_name] = relic_obj
            session.add(relic_obj)

    #To prevent something insane like o(n^n*c) look ups, preload a map of name:=id
    equipment_map = dict()
    with db.scope(NewTRX) as session:

        pre_cache = session.query(db.Equipment)\
            .filter(db.Equipment.special_id == d1.WFSpecials.Prime.value)

        for obj_equipment in pre_cache:
            try:
                equipment_name, _ = obj_equipment.name.split(" Prime")
            except ValueError:
                if obj_equipment.name == "Forma":
                    #The road to hell is paved with exceptions
                    equipment_name = obj_equipment.name
                else:
                    raise

            equipment_map[equipment_name] = obj_equipment.id
            if equipment_name in url_map:
                obj_equipment.wiki_url = url_map[equipment_name]




    with db.scope(NewTRX) as session:
        for raw_equipment_name, components in by_name.items():
            if raw_equipment_name not in equipment_map and raw_equipment_name != "Forma":
                raise ValueError("Missing {}".format(raw_equipment_name))
            else:

                if raw_equipment_name == "Forma":
                    continue

                parent_id = equipment_map[raw_equipment_name]
                for component_name, relic_tiers in components.items():
                    obj_component = db.Component(
                        parent_id=parent_id,
                        name=component_name,
                    )

                    for tier_name, relic_names in relic_tiers.items():
                        for relic_name, rarity_name in relic_names.items():
                            obj_component.locations.append(
                                db.Location(
                                    tier=tier_map[tier_name],
                                    relic=relics_map[relic_name],
                                    rarity=rarity_map[rarity_name.name]
                                )
                            )

                    session.add(obj_component)

def main(engine, NewTRX):


    #cats and subcats first
    with db.scope(NewTRX) as session:
        for cat_element in d1.WFCategories:
            category = db.EquipmentCategory(
                id=cat_element.value,
                name=cat_element.name,
                display_order=cat_element.value)

            session.add(category)

        for subcat_element in d1.WFSubcategories:
            subcat = db.EquipmentSubcategory(id=subcat_element.value, name=subcat_element.name)
            session.add(subcat)

        for special_element in d1.WFSpecials:
            special = db.SpecialIdentifier(id=special_element.value, name=special_element.name, pretty_name=special_element.name)
            session.add(special)




    with db.scope(NewTRX) as session:
        for _, elements in d1.indexed.items():
            for __, things in elements.items():
                for display_position, thing in enumerate(sorted(things, key=lambda x: x['name']), 1):

                    equipment = db.Equipment(
                        data_id=thing['id'],
                        index_id=thing['position'],
                        display_pos=display_position,
                        category_id=thing['category'].value,
                        subcategory_id=thing['subcategory'].value,
                        special_id=thing['special'],
                        name=thing['name'],
                        pretty_name=thing['name']
                        )

                    session.add(equipment)


    #Now to make our initial test

    # with db.scope(NewTRX) as session:
    #     """
    #         There is no organize by penis BUT there is an order_by wtf
    #     """
    #     records = session.query(db.Equipment)\
    #         .join(db.EquipmentCategory, db.Equipment.category)\
    #         .order_by(db.EquipmentCategory.display_order)\
    #         .all()
    #
    #
    #     for record in records:
    #         print(record.category.name, record.name)



if __name__ == '__main__':
    engine, NewTRX = db.boostrap("sqlite:///test.sqlite3", True, True)
    main(engine, NewTRX)
    reconcile_primes(NewTRX)
