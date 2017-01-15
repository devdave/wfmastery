#pylint: disable=R0903

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import create_engine

#Intended for use outside of this file
from sqlalchemy import func as f


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


from contextlib import contextmanager

#Domain helper dependancies
import json

class BaseExt(object):
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=BaseExt)



@contextmanager
def scope(NewTRX):
    session = NewTRX()

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()




def boostrap(sqlite_path, create_all=False, nuke_it=False):
    """
        Params:
            sqlite_path (str): Valid posix path to sqlite
            create_all (bool): If true creates any/all missing tables
            nuke_it (bool): IF create_all is True and this is True, deletes everything (for debugging)
    """

    engine = create_engine(sqlite_path)
    Base.metadata.bind = engine

    NewTRX = sessionmaker(bind=engine)

    if create_all is True:

        if nuke_it is True:
            Base.metadata.drop_all(engine)

        Base.metadata.create_all(engine)


    return engine, NewTRX



class EquipmentCategory(Base):
    __tablename__ = "equipment_categories"


    name = Column(String(250), unique=True, nullable=False)
    display_order = Column(Integer, nullable=False)
    #TODO sanity check a backpopulate from category to equipment

    children = relationship("Equipment",
                            order_by="Equipment.display_pos",
                            back_populates="category")

class EquipmentSubcategory(Base):
    __tablename__ = "equipment_subcategories"
    name = Column(String(250), unique=True, nullable=False)


class SpecialIdentifier(Base):
    __tablename__ = "special_identifiers"
    name = Column(String(250), unique=True, nullable=False)
    pretty_name = Column(String(250), nullable=True)



class RelicTier(Base):
    __tablename__ = "relic_tiers"
    name = Column(String(250), unique=True, nullable=False)

class RelicName(Base):
    __tablename__ = "relic_names"
    name = Column(String(250), unique=True, nullable=False)


class Rarity(Base):
    __tablename__ = "rarities"
    name = Column(String(250), unique=True, nullable=False)

class Location(Base):
    __tablename__ = "locations"
    parent_id = Column(Integer, ForeignKey("components.id"), nullable=False)
    parent = relationship("Component", back_populates="locations")

    #For prime stuff
    tier_id = Column(Integer, ForeignKey("relic_tiers.id"))
    tier = relationship(RelicTier)

    relic_id = Column(Integer, ForeignKey("relic_names.id"))
    relic = relationship(RelicName)

    rarity_id = Column(Integer, ForeignKey("rarities.id"))
    rarity = relationship(Rarity)



class Component(Base):
    __tablename__ = "components"
    parent_id = Column(Integer, ForeignKey("equipment.id"), nullable=False)
    parent = relationship("Equipment", back_populates="components")
    name = Column(String(250))
    required_number = Column(Integer, default=1)
    locations = relationship("Location", back_populates="parent")





class Equipment(Base):
    __tablename__ = "equipment"
    """
        id - data_id
        position - index_id
    """

    data_id = Column(Integer, nullable=False)
    index_id = Column(Integer, nullable=False)

    display_pos = Column(Integer)

    category_id = Column(Integer, ForeignKey("equipment_categories.id"))
    category = relationship(
        EquipmentCategory,
        order_by=EquipmentCategory.display_order)

    subcategory_id = Column(Integer, ForeignKey("equipment_subcategories.id"))
    subcategory = relationship(EquipmentSubcategory)

    special_id = Column(Integer, ForeignKey("special_identifiers.id"))
    special = relationship(SpecialIdentifier)


    name = Column(String(250), nullable=False)
    pretty_name = Column(String(250))
    wiki_url = Column(String(250), nullable=True)


    components = relationship("Component", back_populates="parent")


    hidden = Column(Boolean, default=False)



    note = Column(String(250))



class Transaction(Base):
    __tablename__ = "transactions"
    when = Column(DateTime)
    where = Column(String(250), nullable=False)
    what = Column(String(250), nullable=False)
