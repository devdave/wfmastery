# pylint: disable-msg=C0103,C0301,C0111,E1101
#kindly fuck off, I know
"""
    This was automagically generated so don't expect it to make sense

    Version: 1
    Dec 25th, 2016 ransack date

    Version: 1.2
        No change to order BUT this is now hand-edited :(
"""


# from collections import namedtuple
from enum import Enum, unique, IntEnum




@unique
class WFCategories(IntEnum):
    Warframe = 1
    Primary = 2
    Secondary = 3
    Melee = 4
    Archwing_Equipment = 5
    Things = 6
    Dojo = 7
    Sentinel = 8
    Sentinel_Equipment = 9
    Companions = 10
    Companion_Equipment = 11
    Archwing = 12


@unique
class WFSubcategories(IntEnum):
    NA = 0
    Bows = 1
    Blade_Whip = 2
    Continuous = 3
    Claws = 4
    Dual = 5
    Dual_Swords = 6
    Dagger = 7
    Dual_Dagger = 8
    Fist = 9
    Glaive = 10
    Gun = 11
    Gunblade = 12
    Hammer = 13
    Heavy_Blade = 14
    Hybrid = 15
    Launchers = 16
    Rifle = 17
    Rapier = 18
    Shotgun = 19
    Spearguns = 20
    Sidearms = 21
    Single = 22
    Sword_Shield = 23
    Sword = 24
    Sparring = 25
    Staff = 26
    Scythe = 27
    Sniper = 28
    Tonfa = 29
    Thrown = 30
    Machete = 31
    Melee = 32
    Nikana = 33
    Nunchaku = 34
    Polearm = 35
    Whip = 36
    Kubrow = 37
    Kavat = 38


class AutoNumber(IntEnum):
    #from stdlib docs on enum
    def __new__(cls):
        #goddamn I miss metaprogramming
        value = len(cls.__members__) + 1
        obj = int.__new__(cls)
        #todo ask/find out why its wrapped in only one _ and not double
        obj._value_ = value #pylint: disable=W0212
        return obj

@unique
class WFSpecials(AutoNumber):
    Standard = ()
    # Dojo = ()
    Prime = ()
    Prisma = ()
    Quest = ()
    Rakta = ()
    Secura = ()
    Synoid = ()
    Sancti = ()
    Telos = ()
    Vandal = ()
    Vaykor = ()
    Wraith = ()
    #Dojo stuff
    Energy_lab = ()
    Chem_lab = ()
    Tenno_lab = ()
    Bio_lab = ()





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


def i(etype, name, subtype, **kwargs):
    """Data semi-future proofing"""
    # sourced = kwargs.get("sourced", [])
    is_dojo = kwargs.get("is_dojo", False)
    is_prime = True if "prime" in name.lower() else False
    special = kwargs.get("special", WFSpecials.Standard)


    return dict(category=etype,
                name=name.strip(),
                subcategory=subtype,
                is_prime=is_prime,
                id="-1",
                is_dojo=is_dojo,
                special=special.value

               )

#sub_consts.Rifles
wfmastery_data = [
    i(WFCategories.Primary, "Boltor", WFSubcategories.Rifle),
    i(WFCategories.Primary,
      "Boltor Prime",
      WFSubcategories.Rifle,
      special=WFSpecials.Prime
     ),
    i(WFCategories.Primary, "Telos Boltor", WFSubcategories.Rifle, special=WFSpecials.Telos),
    i(WFCategories.Primary, "Braton", WFSubcategories.Rifle),
    i(WFCategories.Primary, "MK1 Braton", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Braton Prime", WFSubcategories.Rifle, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Braton Vandal", WFSubcategories.Rifle, special=WFSpecials.Vandal),
    i(WFCategories.Primary, "Burston", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Burston Prime", WFSubcategories.Rifle, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Buzlok", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Primary, "Dera", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Dera Vandal", WFSubcategories.Rifle, special=WFSpecials.Vandal),
    i(WFCategories.Primary, "Gorgon", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Gorgon Prisma", WFSubcategories.Rifle, special=WFSpecials.Prisma),
    i(WFCategories.Primary, "Gorgon Wraith", WFSubcategories.Rifle, special=WFSpecials.Wraith),
    i(WFCategories.Primary, "Grakata", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Grakata Prisma", WFSubcategories.Rifle, special=WFSpecials.Prisma),
    i(WFCategories.Primary, "Grinlok", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Primary, "Harpak", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Hema", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Primary, "Hind", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Karak", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Karak Wraith", WFSubcategories.Rifle, special=WFSpecials.Wraith),
    i(WFCategories.Primary, "Latron", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Latron Prime", WFSubcategories.Rifle, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Latron Wraith", WFSubcategories.Rifle, special=WFSpecials.Wraith),
    i(WFCategories.Primary, "Mutalist Quanta", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Primary, "Opticor", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Paracyst", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Primary, "Soma", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Soma Prime", WFSubcategories.Rifle, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Stradavar", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Supra", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Sybaris", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Primary, "Sybaris Dex", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Tetra", WFSubcategories.Rifle),
    i(WFCategories.Primary, "Tetra Prisma", WFSubcategories.Rifle, special=WFSpecials.Prisma),
    i(WFCategories.Primary, "Tiberon", WFSubcategories.Rifle),
    #continuous
    i(WFCategories.Primary, "Amprex", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Flux Rifle", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Glaxion", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Ignis", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Primary, "Quanta ", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Quanta Vandal", WFSubcategories.Rifle, special=WFSpecials.Vandal),
    i(WFCategories.Primary, "Synapse", WFSubcategories.Rifle, is_dojo=True, special=WFSpecials.Bio_lab),
    #WFSubcategories.Shotguns
    i(WFCategories.Primary, "Boar", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Boar Prime", WFSubcategories.Shotgun, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Convectrix", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Drakgoon", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Hek", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Vaykor Hek", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Kohm", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Phage", WFSubcategories.Shotgun, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Primary, "Sobek", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Strun", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Strun MK1", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Strun Wraith", WFSubcategories.Shotgun, special=WFSpecials.Wraith),
    i(WFCategories.Primary, "Tigris", WFSubcategories.Shotgun),
    i(WFCategories.Primary, "Tigris Prime", WFSubcategories.Shotgun, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Tigris Sancti", WFSubcategories.Shotgun, special=WFSpecials.Sancti),
    #Snipers
    i(WFCategories.Primary, "Lanka", WFSubcategories.Sniper, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Primary, "Rubico", WFSubcategories.Sniper),
    i(WFCategories.Primary, "Snipetron", WFSubcategories.Sniper),
    i(WFCategories.Primary, "Snipetron Vandal", WFSubcategories.Sniper, special=WFSpecials.Vandal),
    i(WFCategories.Primary, "Vectis", WFSubcategories.Sniper),
    i(WFCategories.Primary, "Vectis Prime", WFSubcategories.Sniper, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Vulkar", WFSubcategories.Sniper),
    i(WFCategories.Primary, "Vulkar Wraith", WFSubcategories.Sniper, special=WFSpecials.Wraith),
    #Bows
    i(WFCategories.Primary, "Attica", WFSubcategories.Bows, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Primary, "Cernos", WFSubcategories.Bows),
    i(WFCategories.Primary, "Cernos Prime", WFSubcategories.Bows, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Rakta Cernos", WFSubcategories.Bows, special=WFSpecials.Rakta),
    i(WFCategories.Primary, "Daikyu", WFSubcategories.Bows, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Primary, "Dread", WFSubcategories.Bows),
    i(WFCategories.Primary, "Mutalist Cernos", WFSubcategories.Bows),
    i(WFCategories.Primary, "Paris", WFSubcategories.Bows),
    i(WFCategories.Primary, "Paris MK1", WFSubcategories.Bows),
    i(WFCategories.Primary, "Paris Prime", WFSubcategories.Bows, special=WFSpecials.Prime),
    i(WFCategories.Primary, "Zhuge", WFSubcategories.Bows),
    #Launchers
    i(WFCategories.Primary, "Miter", WFSubcategories.Launchers),
    i(WFCategories.Primary, "Ogris", WFSubcategories.Launchers, is_dojo=True),
    i(WFCategories.Primary, "Panthera", WFSubcategories.Launchers),
    i(WFCategories.Primary, "Penta", WFSubcategories.Launchers),
    i(WFCategories.Primary, "Penta Secura", WFSubcategories.Launchers, special=WFSpecials.Secura),
    i(WFCategories.Primary, "Simulor", WFSubcategories.Launchers),
    i(WFCategories.Primary, "Simulor Synoid", WFSubcategories.Launchers, special=WFSpecials.Synoid),
    i(WFCategories.Primary, "Tonkor", WFSubcategories.Launchers),
    i(WFCategories.Primary, "Torid", WFSubcategories.Launchers, is_dojo=True),
    i(WFCategories.Primary, "Zarr", WFSubcategories.Launchers),
    #wtf
    i(WFCategories.Primary, "Javlok", WFSubcategories.Spearguns, is_dojo=True),  #WTF

    #Secondaries
    i(WFCategories.Secondary, "Acrid", WFSubcategories.Single, is_dojo=True),
    i(WFCategories.Secondary, "Angstrum", WFSubcategories.Single),
    i(WFCategories.Secondary, "Azima", WFSubcategories.Single),
    i(WFCategories.Secondary, "Ballistica", WFSubcategories.Single),
    i(WFCategories.Secondary, "Ballistica Rakta", WFSubcategories.Single, special=WFSpecials.Rakta),
    i(WFCategories.Secondary, "Bolto", WFSubcategories.Single),
    i(WFCategories.Secondary, "Cestra", WFSubcategories.Single),
    i(WFCategories.Secondary, "Furis", WFSubcategories.Single),
    i(WFCategories.Secondary, "Furis MK1", WFSubcategories.Single),
    i(WFCategories.Secondary, "Kraken", WFSubcategories.Single),
    i(WFCategories.Secondary, "Kulstar", WFSubcategories.Single),
    i(WFCategories.Secondary, "Lato", WFSubcategories.Single),
    i(WFCategories.Secondary, "Lato Prime", WFSubcategories.Single, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Lato Vandal", WFSubcategories.Single, special=WFSpecials.Vandal),
    i(WFCategories.Secondary, "Lex", WFSubcategories.Single),
    i(WFCategories.Secondary, "Lex Prime", WFSubcategories.Single, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Magnus", WFSubcategories.Single),
    i(WFCategories.Secondary, "Marelok", WFSubcategories.Single, is_dojo=True),
    i(WFCategories.Secondary, "Vaykor Marelok", WFSubcategories.Single, special=WFSpecials.Vaykor),
    i(WFCategories.Secondary, "Seer", WFSubcategories.Single),
    i(WFCategories.Secondary, "Sicarus", WFSubcategories.Single),
    i(WFCategories.Secondary, "Sicarus Prime", WFSubcategories.Single, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Sonicor", WFSubcategories.Single),
    i(WFCategories.Secondary, "Stug", WFSubcategories.Single),
    i(WFCategories.Secondary, "Tysis", WFSubcategories.Single),
    i(WFCategories.Secondary, "Vasto", WFSubcategories.Single),
    i(WFCategories.Secondary, "Vasto Prime", WFSubcategories.Single, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Viper", WFSubcategories.Single),
    i(WFCategories.Secondary, "Atomos", WFSubcategories.Continuous),
    i(WFCategories.Secondary, "Embolist", WFSubcategories.Continuous, is_dojo=True),
    i(WFCategories.Secondary, "Gammacor", WFSubcategories.Continuous),
    i(WFCategories.Secondary, "Gammacor Synoid", WFSubcategories.Continuous, special=WFSpecials.Synoid),
    i(WFCategories.Secondary, "Nukor", WFSubcategories.Continuous, is_dojo=True),
    i(WFCategories.Secondary, "Spectra", WFSubcategories.Continuous, is_dojo=True),
    i(WFCategories.Secondary, "Brakk", WFSubcategories.Shotgun),
    i(WFCategories.Secondary, "Bronco", WFSubcategories.Shotgun),
    i(WFCategories.Secondary, "Bronco Prime", WFSubcategories.Shotgun, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Detron", WFSubcategories.Shotgun),
    i(WFCategories.Secondary, "Detron Mara", WFSubcategories.Shotgun),
    i(WFCategories.Secondary, "Kohmak", WFSubcategories.Shotgun, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Secondary, "Pyrana", WFSubcategories.Shotgun, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Secondary, "Afuris", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Afuris Dex", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Akbolto", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Akbolto Telos", WFSubcategories.Dual, special=WFSpecials.Telos),
    i(WFCategories.Secondary, "Akbronco", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Akbronco Prime", WFSubcategories.Dual, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Akjagara", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Aklato", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Aklex", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Akmagnus", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Aksomati", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Akstiletto", WFSubcategories.Dual, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Secondary, "Akstiletto Prime", WFSubcategories.Dual, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Akvasto", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Akzani", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Dual Cestra", WFSubcategories.Dual, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Secondary, "Dual Cestra Secura", WFSubcategories.Dual, special=WFSpecials.Secura),
    i(WFCategories.Secondary, "Dual Toxocyst", WFSubcategories.Dual, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Secondary, "Staticor", WFSubcategories.Dual, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Secondary, "Twin Grakatas", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Twin Gremlins", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Twin Kohmak", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Twin Rogga", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Twin Vipers", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Twin Vipers Wraith", WFSubcategories.Dual),
    i(WFCategories.Secondary, "Castanas", WFSubcategories.Thrown, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Secondary, "Castanas Sancti", WFSubcategories.Thrown, special=WFSpecials.Sancti),
    i(WFCategories.Secondary, "Despair", WFSubcategories.Thrown),
    i(WFCategories.Secondary, "Hikou", WFSubcategories.Thrown),
    i(WFCategories.Secondary, "Hikou Prime", WFSubcategories.Thrown, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Kunai", WFSubcategories.Thrown),
    i(WFCategories.Secondary, "Kunai MK1", WFSubcategories.Thrown),
    i(WFCategories.Secondary, "Pox", WFSubcategories.Thrown),
    i(WFCategories.Secondary, "Spira", WFSubcategories.Thrown),
    i(WFCategories.Secondary, "Spira Prime", WFSubcategories.Thrown, special=WFSpecials.Prime),
    i(WFCategories.Secondary, "Talons", WFSubcategories.Thrown, is_dojo=True),
    #Melee
    i(WFCategories.Melee, "Broken-War", WFSubcategories.Sword, special=WFSpecials.Quest),
    i(WFCategories.Melee, "Cronus", WFSubcategories.Sword),
    i(WFCategories.Melee, "Dakra Prime", WFSubcategories.Sword, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Dark Sword", WFSubcategories.Sword),
    i(WFCategories.Melee, "Ether Sword", WFSubcategories.Sword),
    i(WFCategories.Melee, "Heat Sword", WFSubcategories.Sword),
    i(WFCategories.Melee, "Jaw Sword", WFSubcategories.Sword),
    i(WFCategories.Melee, "Mire", WFSubcategories.Sword),
    i(WFCategories.Melee, "Pangolin Sword", WFSubcategories.Sword),
    i(WFCategories.Melee, "Plasma Sword", WFSubcategories.Sword),
    i(WFCategories.Melee, "Skana", WFSubcategories.Sword),
    i(WFCategories.Melee, "Skana Prime", WFSubcategories.Sword, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Skana Prisma", WFSubcategories.Sword, special=WFSpecials.Prisma),
    i(WFCategories.Melee, "Dex Dakra", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Dual Cleavers", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Dual Cleavers Prisma", WFSubcategories.Dual_Swords, special=WFSpecials.Prisma),
    i(WFCategories.Melee, "Dual Ether", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Dual Heat Swords", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Dual Ichor", WFSubcategories.Dual_Swords, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Melee, "Dual Kamas", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Dual Kamas Prime", WFSubcategories.Dual_Swords, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Dual Raza", WFSubcategories.Dual_Swords, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Dual Skana", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Dual Zoren", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Nami Skyla", WFSubcategories.Dual_Swords, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Twin Basolk", WFSubcategories.Dual_Swords),
    i(WFCategories.Melee, "Ceramic Dagger", WFSubcategories.Dagger),
    i(WFCategories.Melee, "Dark Dagger", WFSubcategories.Dagger),
    i(WFCategories.Melee, "Dark Dagger Rakta", WFSubcategories.Dagger, special=WFSpecials.Rakta),
    i(WFCategories.Melee, "Heat Dagger", WFSubcategories.Dagger),
    i(WFCategories.Melee, "Karyst", WFSubcategories.Dagger),
    i(WFCategories.Melee, "Sheev", WFSubcategories.Dagger),
    i(WFCategories.Melee, "Kama", WFSubcategories.Machete),
    i(WFCategories.Melee, "Gazal Machete", WFSubcategories.Machete),
    i(WFCategories.Melee, "Machete", WFSubcategories.Machete),
    i(WFCategories.Melee, "Machete Wraith", WFSubcategories.Machete, special=WFSpecials.Wraith),
    i(WFCategories.Melee, "Nami Solo", WFSubcategories.Machete),
    i(WFCategories.Melee, "Prova", WFSubcategories.Machete, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Melee, "Prova Vandal", WFSubcategories.Machete, special=WFSpecials.Vandal),
    i(WFCategories.Melee, "Ether Daggers", WFSubcategories.Dual_Dagger),
    i(WFCategories.Melee, "Fang", WFSubcategories.Dual_Dagger),
    i(WFCategories.Melee, "Fang Prime", WFSubcategories.Dual_Dagger, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Okina", WFSubcategories.Dual_Dagger, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Ankyros", WFSubcategories.Fist),
    i(WFCategories.Melee, "Ankyros Prime", WFSubcategories.Fist, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Furax", WFSubcategories.Fist),
    i(WFCategories.Melee, "Furax MK1", WFSubcategories.Fist),
    i(WFCategories.Melee, "Furax Wraith", WFSubcategories.Fist, special=WFSpecials.Wraith),
    i(WFCategories.Melee, "Tekko", WFSubcategories.Fist),
    i(WFCategories.Melee, "Silva & Aegis", WFSubcategories.Sword_Shield, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Ack & Brunt", WFSubcategories.Sword_Shield, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Melee, "Hirudo", WFSubcategories.Sparring),
    i(WFCategories.Melee, "Kogake", WFSubcategories.Sparring),
    i(WFCategories.Melee, "Obex", WFSubcategories.Sparring),
    i(WFCategories.Melee, "Lesion", WFSubcategories.Polearm),
    i(WFCategories.Melee, "Kesheg", WFSubcategories.Polearm, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Melee, "Orthos", WFSubcategories.Polearm),
    i(WFCategories.Melee, "Orthos Prime", WFSubcategories.Polearm, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Serro", WFSubcategories.Polearm, is_dojo=True, special=WFSpecials.Energy_lab),
    i(WFCategories.Melee, "Sydon", WFSubcategories.Polearm, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Melee, "Sydon Vaykor", WFSubcategories.Polearm, special=WFSpecials.Vaykor),
    i(WFCategories.Melee, "Tonbo", WFSubcategories.Polearm, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Amphis", WFSubcategories.Staff),
    i(WFCategories.Melee, "Bo", WFSubcategories.Staff),
    i(WFCategories.Melee, "Bo MK1", WFSubcategories.Staff),
    i(WFCategories.Melee, "Bo Prime", WFSubcategories.Staff, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Broken Scepter", WFSubcategories.Staff, special=WFSpecials.Quest),
    i(WFCategories.Melee, "Tipedo", WFSubcategories.Staff),
    i(WFCategories.Melee, "Cerata", WFSubcategories.Glaive, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Melee, "Glaive", WFSubcategories.Glaive),
    i(WFCategories.Melee, "Glaive Prime", WFSubcategories.Glaive, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Halikar", WFSubcategories.Glaive),
    i(WFCategories.Melee, "Kestrel", WFSubcategories.Glaive),
    i(WFCategories.Melee, "Orvius", WFSubcategories.Glaive),
    i(WFCategories.Melee, "Atterax", WFSubcategories.Whip),
    i(WFCategories.Melee, "Lecta", WFSubcategories.Whip),
    i(WFCategories.Melee, "Lecta Secura", WFSubcategories.Whip, special=WFSpecials.Secura),
    i(WFCategories.Melee, "Scoliac", WFSubcategories.Whip, is_dojo=True),
    i(WFCategories.Melee, "Galatine", WFSubcategories.Heavy_Blade),
    i(WFCategories.Melee, "Galatine Prime", WFSubcategories.Heavy_Blade, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Gram", WFSubcategories.Heavy_Blade),
    i(WFCategories.Melee, "Scindo", WFSubcategories.Heavy_Blade),
    i(WFCategories.Melee, "Scindo Prime", WFSubcategories.Heavy_Blade, special=WFSpecials.Prime),
    i(WFCategories.Melee, "War", WFSubcategories.Heavy_Blade),
    i(WFCategories.Melee, "Zenistar", WFSubcategories.Heavy_Blade),
    i(WFCategories.Melee, "Fragor", WFSubcategories.Hammer),
    i(WFCategories.Melee, "Fragor Prime", WFSubcategories.Hammer, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Heliocor", WFSubcategories.Hammer),
    i(WFCategories.Melee, "Heliocor Synoid", WFSubcategories.Hammer, special=WFSpecials.Synoid),
    i(WFCategories.Melee, "Jat Kittag", WFSubcategories.Hammer, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Melee, "Magistar", WFSubcategories.Hammer),
    i(WFCategories.Melee, "Magistar Sancti", WFSubcategories.Hammer, special=WFSpecials.Synoid),
    i(WFCategories.Melee, "Sibear", WFSubcategories.Hammer),
    i(WFCategories.Melee, "Nikana", WFSubcategories.Nikana, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Nikana Dragon", WFSubcategories.Nikana),
    i(WFCategories.Melee, "Nikana Prime", WFSubcategories.Nikana, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Ripkas", WFSubcategories.Claws),
    i(WFCategories.Melee, "Venka", WFSubcategories.Claws, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Venka Prime", WFSubcategories.Claws, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Anku", WFSubcategories.Scythe, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Caustacyst", WFSubcategories.Scythe, is_dojo=True, special=WFSpecials.Bio_lab),
    i(WFCategories.Melee, "Ether Reaper", WFSubcategories.Scythe),
    i(WFCategories.Melee, "Hate", WFSubcategories.Scythe),
    i(WFCategories.Melee, "Reaper Prime", WFSubcategories.Scythe, special=WFSpecials.Prime),
    i(WFCategories.Melee, "Boltace", WFSubcategories.Tonfa),
    i(WFCategories.Melee, "Boltace Telos", WFSubcategories.Tonfa, special=WFSpecials.Telos),
    i(WFCategories.Melee, "Kronen", WFSubcategories.Tonfa),
    i(WFCategories.Melee, "Redeemer", WFSubcategories.Gunblade),
    i(WFCategories.Melee, "Sarpa", WFSubcategories.Gunblade),
    i(WFCategories.Melee, "Ninkondi", WFSubcategories.Nunchaku),
    i(WFCategories.Melee, "Shaku", WFSubcategories.Nunchaku, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Lacera", WFSubcategories.Blade_Whip, is_dojo=True, special=WFSpecials.Tenno_lab),
    i(WFCategories.Melee, "Mios", WFSubcategories.Blade_Whip, special=WFSpecials.Bio_lab),
    i(WFCategories.Melee, "Dark Split-Sword", WFSubcategories.Hybrid, is_dojo=True),
    i(WFCategories.Melee, "Destreza", WFSubcategories.Rapier),
    #Archwing
    i(WFCategories.Archwing, "Corvas", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Cyngas", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Dual Decurion", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Fluctus", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Grattler", WFSubcategories.Gun, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Archwing, "Imperator", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Imperator Vandal", WFSubcategories.Gun, special=WFSpecials.Vandal),
    i(WFCategories.Archwing, "Phaedra", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Velocitus", WFSubcategories.Gun),
    i(WFCategories.Archwing, "Agkuza", WFSubcategories.Melee),
    i(WFCategories.Archwing, "Centaur", WFSubcategories.Melee),
    i(WFCategories.Archwing, "Kaszas", WFSubcategories.Melee),
    i(WFCategories.Archwing, "Knux", WFSubcategories.Melee, is_dojo=True, special=WFSpecials.Chem_lab),
    i(WFCategories.Archwing, "Onorix", WFSubcategories.Melee),
    i(WFCategories.Archwing, "Rathbone", WFSubcategories.Melee),
    i(WFCategories.Archwing, "Veritux", WFSubcategories.Melee),
    i(WFCategories.Archwing, "Veritux Prisma", WFSubcategories.Melee, special=WFSpecials.Prisma),
    #Dojo
    # i(WFCategories.Dojo, "Amprex", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Dera", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Dual Cestra", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Flux Rifle", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Glaxion", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Lanka", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Opticor", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Prova", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Quanta", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Serro", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Spectra", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Staticor", WFSubcategories.Energy),
    # i(WFCategories.Dojo, "Supra", WFSubcategories.Energy),
    #
    # i(WFCategories.Dojo, "Acrid", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Caustacyst", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Cerata", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Dual Ichor", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Dual Toxocyst", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Embolist", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Mutalist Quanta", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Hema", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Paracyst", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Phage", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Scoliac", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Synapse", WFSubcategories.Bio),
    # i(WFCategories.Dojo, "Torid", WFSubcategories.Bio),
    #
    # i(WFCategories.Dojo, "Ack & Brunt", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Buzlok", WFSubcategories.Chem, is_dojo=True),
    # i(WFCategories.Dojo, "Grattler", WFSubcategories.Chem, is_dojo=True),
    # i(WFCategories.Dojo, "Grinlok", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Ignis", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Jat Kittag", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Javlok", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Kesheg", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Knux", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Kohmak", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Marelok", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Nukor", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Ogris", WFSubcategories.Chem),
    # i(WFCategories.Dojo, "Sydon", WFSubcategories.Chem),
    #
    # i(WFCategories.Dojo, "Akstiletto", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Anku", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Attica", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Castanas", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Daikyu", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Dark Split-Sword", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Dual Raza", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Lacera", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Nami Skyla", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Nikana", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Okina", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Pyrana", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Shaku", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Silva & Aegis", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Sybaris", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Talons", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Tonbo", WFSubcategories.Tenno),
    # i(WFCategories.Dojo, "Venka", WFSubcategories.Tenno),
    #Sentinels
    i(WFCategories.Sentinel_Equipment, "Deth Machine Rifle", WFSubcategories.Rifle),
    i(WFCategories.Sentinel_Equipment, "Laser Rifle", WFSubcategories.Rifle),
    i(WFCategories.Sentinel_Equipment, "Laser Rifle Prime", WFSubcategories.Rifle, special=WFSpecials.Prime),
    i(WFCategories.Sentinel_Equipment, "Stinger", WFSubcategories.Rifle),
    i(WFCategories.Sentinel_Equipment, "Sweeper", WFSubcategories.Shotgun),
    i(WFCategories.Sentinel_Equipment, "Sweeper Prime", WFSubcategories.Shotgun, special=WFSpecials.Prime),
    i(WFCategories.Sentinel_Equipment, "Vulklok", WFSubcategories.Sniper),
    i(WFCategories.Sentinel_Equipment, "Burst Laser", WFSubcategories.Sidearms),
    i(WFCategories.Sentinel_Equipment, "Burst Laser Prisma", WFSubcategories.Sidearms, special=WFSpecials.Prisma),
    i(WFCategories.Sentinel_Equipment, "Deconstructor", WFSubcategories.Melee), #wtf?
    #Companion equipment
    i(WFCategories.Companion_Equipment, "Kavasa Collar Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    #Warframes
    i(WFCategories.Warframe, "Ash", WFSubcategories.NA),
    i(WFCategories.Warframe, "Ash Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Atlas", WFSubcategories.NA, special=WFSpecials.Quest),
    i(WFCategories.Warframe, "Banshee", WFSubcategories.NA, special=WFSpecials.Tenno_lab),
    i(WFCategories.Warframe, "Chroma", WFSubcategories.NA),
    i(WFCategories.Warframe, "Ember", WFSubcategories.NA),
    i(WFCategories.Warframe, "Ember Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Equinox", WFSubcategories.NA),
    i(WFCategories.Warframe, "Excalibur", WFSubcategories.NA),
    i(WFCategories.Warframe, "Excalibur Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Frost", WFSubcategories.NA),
    i(WFCategories.Warframe, "Frost Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Hydroid", WFSubcategories.NA),
    i(WFCategories.Warframe, "Inaros", WFSubcategories.NA, special=WFSpecials.Quest),
    i(WFCategories.Warframe, "Ivara", WFSubcategories.NA),
    i(WFCategories.Warframe, "Limbo", WFSubcategories.NA, special=WFSpecials.Quest),
    i(WFCategories.Warframe, "Loki", WFSubcategories.NA),
    i(WFCategories.Warframe, "Loki Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Mag", WFSubcategories.NA),
    i(WFCategories.Warframe, "Mag Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Mesa", WFSubcategories.NA),
    i(WFCategories.Warframe, "Mirage", WFSubcategories.NA, special=WFSpecials.Quest),
    i(WFCategories.Warframe, "Nekros", WFSubcategories.NA),
    i(WFCategories.Warframe, "Nekros Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Nezha", WFSubcategories.NA),
    i(WFCategories.Warframe, "Nidus", WFSubcategories.NA, special=WFSpecials.Quest),
    i(WFCategories.Warframe, "Nova", WFSubcategories.NA),
    i(WFCategories.Warframe, "Nova Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Nyx", WFSubcategories.NA),
    i(WFCategories.Warframe, "Nyx Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Oberon", WFSubcategories.NA),
    i(WFCategories.Warframe, "Rhino", WFSubcategories.NA),
    i(WFCategories.Warframe, "Rhino Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Saryn", WFSubcategories.NA),
    i(WFCategories.Warframe, "Saryn Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Titania", WFSubcategories.NA, special=WFSpecials.Quest),
    i(WFCategories.Warframe, "Trinity", WFSubcategories.NA),
    i(WFCategories.Warframe, "Trinity Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Valkyr", WFSubcategories.NA),
    i(WFCategories.Warframe, "Valkyr Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Vauban", WFSubcategories.NA),
    i(WFCategories.Warframe, "Vauban Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Volt", WFSubcategories.NA),
    i(WFCategories.Warframe, "Volt Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Warframe, "Wukong", WFSubcategories.NA),
    i(WFCategories.Warframe, "Zephyr", WFSubcategories.NA),
    #sentinels
    i(WFCategories.Sentinel, "Carrier", WFSubcategories.NA),
    i(WFCategories.Sentinel, "Carrier Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    i(WFCategories.Sentinel, "Dethcube", WFSubcategories.NA),
    i(WFCategories.Sentinel, "Diriga", WFSubcategories.NA),
    i(WFCategories.Sentinel, "Djinn", WFSubcategories.NA, special=WFSpecials.Bio_lab),
    i(WFCategories.Sentinel, "Helios", WFSubcategories.NA, special=WFSpecials.Energy_lab),
    i(WFCategories.Sentinel, "Shade", WFSubcategories.NA),
    i(WFCategories.Sentinel, "Shade Prisma", WFSubcategories.NA, special=WFSpecials.Prisma),
    i(WFCategories.Sentinel, "Wyrm", WFSubcategories.NA),
    i(WFCategories.Sentinel, "Wyrm Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    #Companion Kubrow
    i(WFCategories.Companions, "Chesa Kubrow", WFSubcategories.Kubrow),
    i(WFCategories.Companions, "Huras Kubrow", WFSubcategories.Kubrow),
    i(WFCategories.Companions, "Raksa Kubrow", WFSubcategories.Kubrow),
    i(WFCategories.Companions, "Sahasa Kubrow", WFSubcategories.Kubrow),
    i(WFCategories.Companions, "Sunika Kubrow", WFSubcategories.Kubrow),
    i(WFCategories.Companions, "Helminth Charger", WFSubcategories.Kubrow),
    #Companion Kavat
    i(WFCategories.Companions, "Adarza Kavat", WFSubcategories.Kavat),
    i(WFCategories.Companions, "Smeeta Kavat", WFSubcategories.Kavat),
    #Archwings
    i(WFCategories.Archwing, "Amesha", WFSubcategories.NA, special=WFSpecials.Tenno_lab),
    i(WFCategories.Archwing, "Elytron", WFSubcategories.NA, special=WFSpecials.Tenno_lab),
    i(WFCategories.Archwing, "Itzal", WFSubcategories.NA, special=WFSpecials.Tenno_lab),
    i(WFCategories.Archwing, "Odonata", WFSubcategories.NA),
    i(WFCategories.Archwing, "Odonata Prime", WFSubcategories.NA, special=WFSpecials.Prime),
    #Misc
    i(WFCategories.Things, "Forma", WFSubcategories.NA)

]

def index(raw_data):
    product = {}
    position2id = {}
    id2position = {} #pylint: disable=W0621
    dojo = {} #going to rely heavily on Python's by-ref here
    for pos, thing in enumerate(raw_data):
        cat_name = thing["category"].name
        #got that goddamn song in my head now
        scat_name = thing["subcategory"].name if thing["subcategory"] is not None else "Standard"
        scat_val = thing["subcategory"].value if thing["subcategory"] is not None else 0


        #could be refactored to defaultdict but meh?
        if cat_name not in product:
            product[cat_name] = {}

        if scat_name not in product[cat_name]:
            product[cat_name][scat_name] = []

        if cat_name != "Dojo":
            thing['id'] = "{0}{1:02d}{2:03d}".format(thing["category"].value, scat_val, pos)
            #Order SHOULD have dojo stuff at bottom but
            #if something goes wrong then the index won't have the id set yet
            if thing['is_dojo'] is True:
                dojo[thing['name']] = thing

            position2id[pos] = thing['id']
            id2position[thing['id']] = pos


        elif thing['category'] == WFCategories.Dojo:
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
