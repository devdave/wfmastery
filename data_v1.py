# pylint: disable-msg=C0103,C0301,C0111,E1101
#kindly fuck off, I know
"""
    This was automagically generated so don't expect it to make sense

    Version: 1
    Dec 25th, 2016 ransack date

    Version: 1.2
        No change to order BUT this is now hand-edited :(
"""


from collections import namedtuple
import attr





category = [
    "Warframe",
    "Primary",
    "Secondary",
    "Melee",
    "Archwing",
    "Things",
    "Dojo",
    "Sentinel"
]



subcat = [
    "Bows", "Blade_Whip",
    "Continuous", "Claws",
    "Dual", "Dual_Swords", "Dagger", "Dual_Dagger",
    "Fist",
    "Glaive", "Gun", "Gunblade",
    "Hammer", "Heavy_Blade", "Hybrid",
    "Launchers",
    "Rifle", "Rapier",
    "Shotgun", "Spearguns", "Sidearms", "Single", "Sword_Shield", "Sword", "Sparring",
    "Staff", "Scythe", "Sniper",
    "Tonfa", "Thrown",
    "Machete", "Melee",
    "Nikana", "Nunchaku",
    "Polearm",
    "Whip",
    #Dojo stuff
    "Energy", "Chem", "Tenno", "Bio"
]



WFConsts = namedtuple("WFConsts", ",".join(category))
WFSubtypes = namedtuple("WFSubtypes", ",".join(subcat))

make_const = lambda x, y: x(*list(range(len(y))))

group_consts = make_const(WFConsts, category)
sub_consts = make_const(WFSubtypes, subcat)


def i(etype, name, subtype, **kwargs):
    """Data semi-future proofing"""
    # sourced = kwargs.get("sourced", [])
    is_dojo = kwargs.get("is_dojo", False)
    is_prime = True if "prime" in name.lower() else False

    return dict(category=etype,
                name=name.strip(),
                subcategory=subtype,
                is_prime=is_prime,
                id="-1",
                is_dojo=is_dojo
               )

#sub_consts.Rifles
wfmastery_data = [
    i(group_consts.Primary, "Boltor", sub_consts.Rifle),
    i(group_consts.Primary,
      "Boltor Prime",
      sub_consts.Rifle,
     ),
    i(group_consts.Primary, "Telos Boltor", sub_consts.Rifle),
    i(group_consts.Primary, "Braton", sub_consts.Rifle),
    i(group_consts.Primary, "MK1 Braton", sub_consts.Rifle),
    i(group_consts.Primary, "Braton Prime", sub_consts.Rifle),
    i(group_consts.Primary, "Braton Vandal", sub_consts.Rifle),
    i(group_consts.Primary, "Burston", sub_consts.Rifle),
    i(group_consts.Primary, "Burston Prime", sub_consts.Rifle),
    i(group_consts.Primary, "Buzlok", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Dera", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Dera Vandal", sub_consts.Rifle),
    i(group_consts.Primary, "Gorgon", sub_consts.Rifle),
    i(group_consts.Primary, "Gorgon Prisma", sub_consts.Rifle),
    i(group_consts.Primary, "Gorgon Wraith", sub_consts.Rifle),
    i(group_consts.Primary, "Grakata", sub_consts.Rifle),
    i(group_consts.Primary, "Grakata Prisma", sub_consts.Rifle),
    i(group_consts.Primary, "Grinlok", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Harpak", sub_consts.Rifle),
    i(group_consts.Primary, "Hema", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Hind", sub_consts.Rifle),
    i(group_consts.Primary, "Karak", sub_consts.Rifle),
    i(group_consts.Primary, "Karak Wraith", sub_consts.Rifle),
    i(group_consts.Primary, "Latron", sub_consts.Rifle),
    i(group_consts.Primary, "Latron Prime", sub_consts.Rifle),
    i(group_consts.Primary, "Latron Wraith", sub_consts.Rifle),
    i(group_consts.Primary, "Mutalist Quanta", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Opticor", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Paracyst", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Soma", sub_consts.Rifle),
    i(group_consts.Primary, "Soma Prime", sub_consts.Rifle),
    i(group_consts.Primary, "Stradavar", sub_consts.Rifle),
    i(group_consts.Primary, "Supra", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Sybaris", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Sybaris Dex", sub_consts.Rifle),
    i(group_consts.Primary, "Tetra", sub_consts.Rifle),
    i(group_consts.Primary, "Tetra Prisma", sub_consts.Rifle),
    i(group_consts.Primary, "Tiberon", sub_consts.Rifle),
    #continuous
    i(group_consts.Primary, "Amprex", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Flux Rifle", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Glaxion", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Ignis", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Quanta ", sub_consts.Rifle, is_dojo=True),
    i(group_consts.Primary, "Quanta Vandal", sub_consts.Rifle),
    i(group_consts.Primary, "Synapse", sub_consts.Rifle, is_dojo=True),
    #sub_consts.Shotguns
    i(group_consts.Primary, "Boar", sub_consts.Shotgun),
    i(group_consts.Primary, "Boar Prime", sub_consts.Shotgun),
    i(group_consts.Primary, "Convectrix", sub_consts.Shotgun),
    i(group_consts.Primary, "Drakgoon", sub_consts.Shotgun),
    i(group_consts.Primary, "Hek", sub_consts.Shotgun),
    i(group_consts.Primary, "Vaykor Hek", sub_consts.Shotgun),
    i(group_consts.Primary, "Kohm", sub_consts.Shotgun),
    i(group_consts.Primary, "Phage", sub_consts.Shotgun, is_dojo=True),
    i(group_consts.Primary, "Sobek", sub_consts.Shotgun),
    i(group_consts.Primary, "Strun", sub_consts.Shotgun),
    i(group_consts.Primary, "Strun MK1", sub_consts.Shotgun),
    i(group_consts.Primary, "Strun Wraith", sub_consts.Shotgun),
    i(group_consts.Primary, "Tigris", sub_consts.Shotgun),
    i(group_consts.Primary, "Tigris Prime", sub_consts.Shotgun),
    i(group_consts.Primary, "Tigris Sancti", sub_consts.Shotgun),
    #Snipers
    i(group_consts.Primary, "Lanka", sub_consts.Sniper, is_dojo=True),
    i(group_consts.Primary, "Rubico", sub_consts.Sniper),
    i(group_consts.Primary, "Snipetron", sub_consts.Sniper),
    i(group_consts.Primary, "Snipetron Vandal", sub_consts.Sniper),
    i(group_consts.Primary, "Vectis", sub_consts.Sniper),
    i(group_consts.Primary, "Vectis Prime", sub_consts.Sniper),
    i(group_consts.Primary, "Vulkar", sub_consts.Sniper),
    i(group_consts.Primary, "Vulkar Wraith", sub_consts.Sniper),
    #Bows
    i(group_consts.Primary, "Attica", sub_consts.Bows, is_dojo=True),
    i(group_consts.Primary, "Cernos", sub_consts.Bows),
    i(group_consts.Primary, "Cernos Prime", sub_consts.Bows),
    i(group_consts.Primary, "Rakta Cernos", sub_consts.Bows),
    i(group_consts.Primary, "Daikyu", sub_consts.Bows, is_dojo=True),
    i(group_consts.Primary, "Dread", sub_consts.Bows),
    i(group_consts.Primary, "Mutalist Cernos", sub_consts.Bows),
    i(group_consts.Primary, "Paris", sub_consts.Bows),
    i(group_consts.Primary, "Paris MK1", sub_consts.Bows),
    i(group_consts.Primary, "Paris Prime", sub_consts.Bows),
    i(group_consts.Primary, "Zhuge", sub_consts.Bows),
    #Launchers
    i(group_consts.Primary, "Miter", sub_consts.Launchers),
    i(group_consts.Primary, "Ogris", sub_consts.Launchers, is_dojo=True),
    i(group_consts.Primary, "Panthera", sub_consts.Launchers),
    i(group_consts.Primary, "Penta", sub_consts.Launchers),
    i(group_consts.Primary, "Penta Secura", sub_consts.Launchers),
    i(group_consts.Primary, "Simulor", sub_consts.Launchers),
    i(group_consts.Primary, "Simulor Synoid", sub_consts.Launchers),
    i(group_consts.Primary, "Tonkor", sub_consts.Launchers),
    i(group_consts.Primary, "Torid", sub_consts.Launchers, is_dojo=True),
    i(group_consts.Primary, "Zarr", sub_consts.Launchers),
    #wtf
    i(group_consts.Primary, "Javlok", sub_consts.Spearguns, is_dojo=True),  #WTF

    #Secondaries
    i(group_consts.Secondary, "Acrid", sub_consts.Single, is_dojo=True),
    i(group_consts.Secondary, "Angstrum", sub_consts.Single),
    i(group_consts.Secondary, "Azima", sub_consts.Single),
    i(group_consts.Secondary, "Ballistica", sub_consts.Single),
    i(group_consts.Secondary, "Ballistica Rakta", sub_consts.Single),
    i(group_consts.Secondary, "Bolto", sub_consts.Single),
    i(group_consts.Secondary, "Cestra", sub_consts.Single),
    i(group_consts.Secondary, "Furis", sub_consts.Single),
    i(group_consts.Secondary, "Furis MK1", sub_consts.Single),
    i(group_consts.Secondary, "Kraken", sub_consts.Single),
    i(group_consts.Secondary, "Kulstar", sub_consts.Single),
    i(group_consts.Secondary, "Lato", sub_consts.Single),
    i(group_consts.Secondary, "Lato Prime", sub_consts.Single),
    i(group_consts.Secondary, "Lato Vandal", sub_consts.Single),
    i(group_consts.Secondary, "Lex", sub_consts.Single),
    i(group_consts.Secondary, "Lex Prime", sub_consts.Single),
    i(group_consts.Secondary, "Magnus", sub_consts.Single),
    i(group_consts.Secondary, "Marelok", sub_consts.Single, is_dojo=True),
    i(group_consts.Secondary, "Vaykor Marelok", sub_consts.Single),
    i(group_consts.Secondary, "Seer", sub_consts.Single),
    i(group_consts.Secondary, "Sicarus", sub_consts.Single),
    i(group_consts.Secondary, "Sicarus Prime", sub_consts.Single),
    i(group_consts.Secondary, "Sonicor", sub_consts.Single),
    i(group_consts.Secondary, "Stug", sub_consts.Single),
    i(group_consts.Secondary, "Tysis", sub_consts.Single),
    i(group_consts.Secondary, "Vasto", sub_consts.Single),
    i(group_consts.Secondary, "Vasto Prime", sub_consts.Single),
    i(group_consts.Secondary, "Viper", sub_consts.Single),
    i(group_consts.Secondary, "Atomos", sub_consts.Continuous),
    i(group_consts.Secondary, "Embolist", sub_consts.Continuous, is_dojo=True),
    i(group_consts.Secondary, "Gammacor", sub_consts.Continuous),
    i(group_consts.Secondary, "Gammacor Synoid", sub_consts.Continuous),
    i(group_consts.Secondary, "Nukor", sub_consts.Continuous, is_dojo=True),
    i(group_consts.Secondary, "Spectra", sub_consts.Continuous, is_dojo=True),
    i(group_consts.Secondary, "Brakk", sub_consts.Shotgun),
    i(group_consts.Secondary, "Bronco", sub_consts.Shotgun),
    i(group_consts.Secondary, "Bronco Prime", sub_consts.Shotgun),
    i(group_consts.Secondary, "Detron", sub_consts.Shotgun),
    i(group_consts.Secondary, "Detron Mara", sub_consts.Shotgun),
    i(group_consts.Secondary, "Kohmak", sub_consts.Shotgun, is_dojo=True),
    i(group_consts.Secondary, "Pyrana", sub_consts.Shotgun, is_dojo=True),
    i(group_consts.Secondary, "Afuris", sub_consts.Dual),
    i(group_consts.Secondary, "Afuris Dex", sub_consts.Dual),
    i(group_consts.Secondary, "Akbolto", sub_consts.Dual),
    i(group_consts.Secondary, "Akbolto Telos", sub_consts.Dual),
    i(group_consts.Secondary, "Akbronco", sub_consts.Dual),
    i(group_consts.Secondary, "Akbronco Prime", sub_consts.Dual),
    i(group_consts.Secondary, "Akjagara", sub_consts.Dual),
    i(group_consts.Secondary, "Aklato", sub_consts.Dual),
    i(group_consts.Secondary, "Aklex", sub_consts.Dual),
    i(group_consts.Secondary, "Akmagnus", sub_consts.Dual),
    i(group_consts.Secondary, "Aksomati", sub_consts.Dual),
    i(group_consts.Secondary, "Akstiletto", sub_consts.Dual, is_dojo=True),
    i(group_consts.Secondary, "Akstiletto Prime", sub_consts.Dual),
    i(group_consts.Secondary, "Akvasto", sub_consts.Dual),
    i(group_consts.Secondary, "Akzani", sub_consts.Dual),
    i(group_consts.Secondary, "Dual Cestra", sub_consts.Dual, is_dojo=True),
    i(group_consts.Secondary, "Dual Cestra Secura", sub_consts.Dual),
    i(group_consts.Secondary, "Dual Toxocyst", sub_consts.Dual, is_dojo=True),
    i(group_consts.Secondary, "Staticor", sub_consts.Dual, is_dojo=True),
    i(group_consts.Secondary, "Twin Grakatas", sub_consts.Dual),
    i(group_consts.Secondary, "Twin Gremlins", sub_consts.Dual),
    i(group_consts.Secondary, "Twin Kohmak", sub_consts.Dual),
    i(group_consts.Secondary, "Twin Rogga", sub_consts.Dual),
    i(group_consts.Secondary, "Twin Vipers", sub_consts.Dual),
    i(group_consts.Secondary, "Twin Vipers Wraith", sub_consts.Dual),
    i(group_consts.Secondary, "Castanas", sub_consts.Thrown, is_dojo=True),
    i(group_consts.Secondary, "Castanas Sancti", sub_consts.Thrown),
    i(group_consts.Secondary, "Despair", sub_consts.Thrown),
    i(group_consts.Secondary, "Hikou", sub_consts.Thrown),
    i(group_consts.Secondary, "Hikou Prime", sub_consts.Thrown),
    i(group_consts.Secondary, "Kunai", sub_consts.Thrown),
    i(group_consts.Secondary, "Kunai MK1", sub_consts.Thrown),
    i(group_consts.Secondary, "Pox", sub_consts.Thrown),
    i(group_consts.Secondary, "Spira", sub_consts.Thrown),
    i(group_consts.Secondary, "Spira Prime", sub_consts.Thrown),
    i(group_consts.Secondary, "Talons", sub_consts.Thrown, is_dojo=True),
    #Melee
    i(group_consts.Melee, "Broken-War", sub_consts.Sword),
    i(group_consts.Melee, "Cronus", sub_consts.Sword),
    i(group_consts.Melee, "Dakra Prime", sub_consts.Sword),
    i(group_consts.Melee, "Dark Sword", sub_consts.Sword),
    i(group_consts.Melee, "Ether Sword", sub_consts.Sword),
    i(group_consts.Melee, "Heat Sword", sub_consts.Sword),
    i(group_consts.Melee, "Jaw Sword", sub_consts.Sword),
    i(group_consts.Melee, "Mire", sub_consts.Sword),
    i(group_consts.Melee, "Pangolin Sword", sub_consts.Sword),
    i(group_consts.Melee, "Plasma Sword", sub_consts.Sword),
    i(group_consts.Melee, "Skana", sub_consts.Sword),
    i(group_consts.Melee, "Skana Prime", sub_consts.Sword),
    i(group_consts.Melee, "Skana Prisma", sub_consts.Sword),
    i(group_consts.Melee, "Dex Dakra", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Cleavers", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Cleavers Prisma", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Ether", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Heat Swords", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Ichor", sub_consts.Dual_Swords, is_dojo=True),
    i(group_consts.Melee, "Dual Kamas", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Kamas Prime", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Raza", sub_consts.Dual_Swords, is_dojo=True),
    i(group_consts.Melee, "Dual Skana", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Dual Zoren", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Nami Skyla", sub_consts.Dual_Swords, is_dojo=True),
    i(group_consts.Melee, "Twin Basolk", sub_consts.Dual_Swords),
    i(group_consts.Melee, "Ceramic Dagger", sub_consts.Dagger),
    i(group_consts.Melee, "Dark Dagger", sub_consts.Dagger),
    i(group_consts.Melee, "Dark Dagger Rakta", sub_consts.Dagger),
    i(group_consts.Melee, "Heat Dagger", sub_consts.Dagger),
    i(group_consts.Melee, "Karyst", sub_consts.Dagger),
    i(group_consts.Melee, "Sheev", sub_consts.Dagger),
    i(group_consts.Melee, "Kama", sub_consts.Machete),
    i(group_consts.Melee, "Gazal Machete", sub_consts.Machete),
    i(group_consts.Melee, "Machete", sub_consts.Machete),
    i(group_consts.Melee, "Machete Wraith", sub_consts.Machete),
    i(group_consts.Melee, "Nami Solo", sub_consts.Machete),
    i(group_consts.Melee, "Prova", sub_consts.Machete, is_dojo=True),
    i(group_consts.Melee, "Prova Vandal", sub_consts.Machete),
    i(group_consts.Melee, "Ether Daggers", sub_consts.Dual_Dagger),
    i(group_consts.Melee, "Fang", sub_consts.Dual_Dagger),
    i(group_consts.Melee, "Fang Prime", sub_consts.Dual_Dagger),
    i(group_consts.Melee, "Okina", sub_consts.Dual_Dagger, is_dojo=True),
    i(group_consts.Melee, "Ankyros", sub_consts.Fist),
    i(group_consts.Melee, "Ankyros Prime", sub_consts.Fist),
    i(group_consts.Melee, "Furax", sub_consts.Fist),
    i(group_consts.Melee, "Furax MK1", sub_consts.Fist),
    i(group_consts.Melee, "Furax Wraith", sub_consts.Fist),
    i(group_consts.Melee, "Tekko", sub_consts.Fist),
    i(group_consts.Melee, "Silva & Aegis", sub_consts.Sword_Shield, is_dojo=True),
    i(group_consts.Melee, "Ack & Brunt", sub_consts.Sword_Shield, is_dojo=True),
    i(group_consts.Melee, "Hirudo", sub_consts.Sparring),
    i(group_consts.Melee, "Kogake", sub_consts.Sparring),
    i(group_consts.Melee, "Obex", sub_consts.Sparring),
    i(group_consts.Melee, "Lesion", sub_consts.Polearm),
    i(group_consts.Melee, "Kesheg", sub_consts.Polearm, is_dojo=True),
    i(group_consts.Melee, "Orthos", sub_consts.Polearm),
    i(group_consts.Melee, "Orthos Prime", sub_consts.Polearm),
    i(group_consts.Melee, "Serro", sub_consts.Polearm, is_dojo=True),
    i(group_consts.Melee, "Sydon", sub_consts.Polearm, is_dojo=True),
    i(group_consts.Melee, "Sydon Vaykor", sub_consts.Polearm),
    i(group_consts.Melee, "Tonbo", sub_consts.Polearm, is_dojo=True),
    i(group_consts.Melee, "Amphis", sub_consts.Staff),
    i(group_consts.Melee, "Bo", sub_consts.Staff),
    i(group_consts.Melee, "Bo MK1", sub_consts.Staff),
    i(group_consts.Melee, "Bo Prime", sub_consts.Staff),
    i(group_consts.Melee, "Broken Scepter", sub_consts.Staff),
    i(group_consts.Melee, "Tipedo", sub_consts.Staff),
    i(group_consts.Melee, "Cerata", sub_consts.Glaive, is_dojo=True),
    i(group_consts.Melee, "Glaive", sub_consts.Glaive),
    i(group_consts.Melee, "Glaive Prime", sub_consts.Glaive),
    i(group_consts.Melee, "Halikar", sub_consts.Glaive),
    i(group_consts.Melee, "Kestrel", sub_consts.Glaive),
    i(group_consts.Melee, "Orvius", sub_consts.Glaive),
    i(group_consts.Melee, "Atterax", sub_consts.Whip),
    i(group_consts.Melee, "Lecta", sub_consts.Whip),
    i(group_consts.Melee, "Lecta Secura", sub_consts.Whip),
    i(group_consts.Melee, "Scoliac", sub_consts.Whip, is_dojo=True),
    i(group_consts.Melee, "Galatine", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "Galatine Prime", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "Gram", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "Scindo", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "Scindo Prime", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "War", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "Zenistar", sub_consts.Heavy_Blade),
    i(group_consts.Melee, "Fragor", sub_consts.Hammer),
    i(group_consts.Melee, "Fragor Prime", sub_consts.Hammer),
    i(group_consts.Melee, "Heliocor", sub_consts.Hammer),
    i(group_consts.Melee, "Heliocor Synoid", sub_consts.Hammer),
    i(group_consts.Melee, "Jat Kittag", sub_consts.Hammer, is_dojo=True),
    i(group_consts.Melee, "Magistar", sub_consts.Hammer),
    i(group_consts.Melee, "Magistar Sancti", sub_consts.Hammer),
    i(group_consts.Melee, "Sibear", sub_consts.Hammer),
    i(group_consts.Melee, "Nikana", sub_consts.Nikana, is_dojo=True),
    i(group_consts.Melee, "Nikana Dragon", sub_consts.Nikana),
    i(group_consts.Melee, "Nikana Prime", sub_consts.Nikana),
    i(group_consts.Melee, "Ripkas", sub_consts.Claws),
    i(group_consts.Melee, "Venka", sub_consts.Claws, is_dojo=True),
    i(group_consts.Melee, "Venka Prime", sub_consts.Claws),
    i(group_consts.Melee, "Anku", sub_consts.Scythe, is_dojo=True),
    i(group_consts.Melee, "Caustacyst", sub_consts.Scythe, is_dojo=True),
    i(group_consts.Melee, "Ether Reaper", sub_consts.Scythe),
    i(group_consts.Melee, "Hate", sub_consts.Scythe),
    i(group_consts.Melee, "Reaper Prime", sub_consts.Scythe),
    i(group_consts.Melee, "Boltace", sub_consts.Tonfa),
    i(group_consts.Melee, "Boltace Telos", sub_consts.Tonfa),
    i(group_consts.Melee, "Kronen", sub_consts.Tonfa),
    i(group_consts.Melee, "Redeemer", sub_consts.Gunblade),
    i(group_consts.Melee, "Sarpa", sub_consts.Gunblade),
    i(group_consts.Melee, "Ninkondi", sub_consts.Nunchaku),
    i(group_consts.Melee, "Shaku", sub_consts.Nunchaku, is_dojo=True),
    i(group_consts.Melee, "Lacera", sub_consts.Blade_Whip, is_dojo=True),
    i(group_consts.Melee, "Mios", sub_consts.Blade_Whip),
    i(group_consts.Melee, "Dark Split-Sword", sub_consts.Hybrid, is_dojo=True),
    i(group_consts.Melee, "Destreza", sub_consts.Rapier),
    #Archwing
    i(group_consts.Archwing, "Corvas", sub_consts.Gun),
    i(group_consts.Archwing, "Cyngas", sub_consts.Gun),
    i(group_consts.Archwing, "Dual Decurion", sub_consts.Gun),
    i(group_consts.Archwing, "Fluctus", sub_consts.Gun),
    i(group_consts.Archwing, "Grattler", sub_consts.Gun, is_dojo=True),
    i(group_consts.Archwing, "Imperator", sub_consts.Gun),
    i(group_consts.Archwing, "Imperator Vandal", sub_consts.Gun),
    i(group_consts.Archwing, "Phaedra", sub_consts.Gun),
    i(group_consts.Archwing, "Velocitus", sub_consts.Gun),
    i(group_consts.Archwing, "Agkuza", sub_consts.Melee),
    i(group_consts.Archwing, "Centaur", sub_consts.Melee),
    i(group_consts.Archwing, "Kaszas", sub_consts.Melee),
    i(group_consts.Archwing, "Knux", sub_consts.Melee, is_dojo=True),
    i(group_consts.Archwing, "Onorix", sub_consts.Melee),
    i(group_consts.Archwing, "Rathbone", sub_consts.Melee),
    i(group_consts.Archwing, "Veritux", sub_consts.Melee),
    i(group_consts.Archwing, "Veritux Prisma", sub_consts.Melee),
    #Dojo
    i(group_consts.Dojo, "Amprex", sub_consts.Energy),
    i(group_consts.Dojo, "Dera", sub_consts.Energy),
    i(group_consts.Dojo, "Dual Cestra", sub_consts.Energy),
    i(group_consts.Dojo, "Flux Rifle", sub_consts.Energy),
    i(group_consts.Dojo, "Glaxion", sub_consts.Energy),
    i(group_consts.Dojo, "Lanka", sub_consts.Energy),
    i(group_consts.Dojo, "Opticor", sub_consts.Energy),
    i(group_consts.Dojo, "Prova", sub_consts.Energy),
    i(group_consts.Dojo, "Quanta", sub_consts.Energy),
    i(group_consts.Dojo, "Serro", sub_consts.Energy),
    i(group_consts.Dojo, "Spectra", sub_consts.Energy),
    i(group_consts.Dojo, "Staticor", sub_consts.Energy),
    i(group_consts.Dojo, "Supra", sub_consts.Energy),
    i(group_consts.Dojo, "Acrid", sub_consts.Bio),
    i(group_consts.Dojo, "Caustacyst", sub_consts.Bio),
    i(group_consts.Dojo, "Cerata", sub_consts.Bio),
    i(group_consts.Dojo, "Dual Ichor", sub_consts.Bio),
    i(group_consts.Dojo, "Dual Toxocyst", sub_consts.Bio),
    i(group_consts.Dojo, "Embolist", sub_consts.Bio),
    i(group_consts.Dojo, "Mutalist Quanta", sub_consts.Bio),
    i(group_consts.Dojo, "Hema", sub_consts.Bio),
    i(group_consts.Dojo, "Paracyst", sub_consts.Bio),
    i(group_consts.Dojo, "Phage", sub_consts.Bio),
    i(group_consts.Dojo, "Scoliac", sub_consts.Bio),
    i(group_consts.Dojo, "Synapse", sub_consts.Bio),
    i(group_consts.Dojo, "Torid", sub_consts.Bio),
    i(group_consts.Dojo, "Ack & Brunt", sub_consts.Chem),
    i(group_consts.Dojo, "Buzlok", sub_consts.Chem, is_dojo=True),
    i(group_consts.Dojo, "Grattler", sub_consts.Chem, is_dojo=True),
    i(group_consts.Dojo, "Grinlok", sub_consts.Chem),
    i(group_consts.Dojo, "Ignis", sub_consts.Chem),
    i(group_consts.Dojo, "Jat Kittag", sub_consts.Chem),
    i(group_consts.Dojo, "Javlok", sub_consts.Chem),
    i(group_consts.Dojo, "Kesheg", sub_consts.Chem),
    i(group_consts.Dojo, "Knux", sub_consts.Chem),
    i(group_consts.Dojo, "Kohmak", sub_consts.Chem),
    i(group_consts.Dojo, "Marelok", sub_consts.Chem),
    i(group_consts.Dojo, "Nukor", sub_consts.Chem),
    i(group_consts.Dojo, "Ogris", sub_consts.Chem),
    i(group_consts.Dojo, "Sydon", sub_consts.Chem),
    i(group_consts.Dojo, "Akstiletto", sub_consts.Tenno),
    i(group_consts.Dojo, "Anku", sub_consts.Tenno),
    i(group_consts.Dojo, "Attica", sub_consts.Tenno),
    i(group_consts.Dojo, "Castanas", sub_consts.Tenno),
    i(group_consts.Dojo, "Daikyu", sub_consts.Tenno),
    i(group_consts.Dojo, "Dark Split-Sword", sub_consts.Tenno),
    i(group_consts.Dojo, "Dual Raza", sub_consts.Tenno),
    i(group_consts.Dojo, "Lacera", sub_consts.Tenno),
    i(group_consts.Dojo, "Nami Skyla", sub_consts.Tenno),
    i(group_consts.Dojo, "Nikana", sub_consts.Tenno),
    i(group_consts.Dojo, "Okina", sub_consts.Tenno),
    i(group_consts.Dojo, "Pyrana", sub_consts.Tenno),
    i(group_consts.Dojo, "Shaku", sub_consts.Tenno),
    i(group_consts.Dojo, "Silva & Aegis", sub_consts.Tenno),
    i(group_consts.Dojo, "Sybaris", sub_consts.Tenno),
    i(group_consts.Dojo, "Talons", sub_consts.Tenno),
    i(group_consts.Dojo, "Tonbo", sub_consts.Tenno),
    i(group_consts.Dojo, "Venka", sub_consts.Tenno),
    #Sentinels
    i(group_consts.Sentinel, "Deth Machine Rifle", sub_consts.Rifle),
    i(group_consts.Sentinel, "Laser Rifle", sub_consts.Rifle),
    i(group_consts.Sentinel, "Laser Rifle Prime", sub_consts.Rifle),
    i(group_consts.Sentinel, "Stinger", sub_consts.Rifle),
    i(group_consts.Sentinel, "Sweeper", sub_consts.Shotgun),
    i(group_consts.Sentinel, "Sweeper Prime", sub_consts.Shotgun),
    i(group_consts.Sentinel, "Vulklok", sub_consts.Sniper),
    i(group_consts.Sentinel, "Burst Laser", sub_consts.Sidearms),
    i(group_consts.Sentinel, "Burst Laser Prisma", sub_consts.Sidearms),
    i(group_consts.Sentinel, "Deconstructor", sub_consts.Melee) #wtf?
]

def index(raw_data):
    product = {}
    position2id = {}
    id2position = {}
    dojo = {} #going to rely heavily on Python's by-ref here
    for pos, thing in enumerate(raw_data):
        cat_name = category[thing["category"]]
        #got that goddamn song in my head now
        scat_name = subcat[thing["subcategory"]]


        #could be refactored to defaultdict but meh?
        if cat_name not in product:
            product[cat_name] = {}

        if scat_name not in product[cat_name]:
            product[cat_name][scat_name] = []

        if cat_name != "Dojo":
            thing['id'] = "{0}{1:02d}{2:03d}".format(thing["category"], thing['subcategory'], pos)
            #Order SHOULD have dojo stuff at bottom but
            #if something goes wrong then the index won't have the id set yet
            if thing['is_dojo'] is True:
                dojo[thing['name']] = thing

            position2id[pos] = thing['id']
            id2position[thing['id']] = pos


        elif thing['category'] == group_consts.Dojo:
            assert thing['name'] in dojo, "Assumption is incorrect, {} was hit ahead of time".format(thing)
            thing['id'] = dojo[thing['name']]["id"]
        else:
            raise Exception("How did we get here? {}".format(thing))



        #In process URL encoding

        thing['position'] = pos

        product[cat_name][scat_name].append(thing)


    return product, position2id, id2position


indexed, positions, id2position = index(wfmastery_data)

debug = 1
debug = debug + 2
