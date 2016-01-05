from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('puppy_id', Integer, ForeignKey('puppy.id')),
                          Column('adopter_id', Integer, ForeignKey('adopter.id'))
                          )


class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)
    maximum_capacity = Column(Integer)
    current_occupancy = Column(Integer)


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    picture = Column(String)
    description = Column(String)
    special_needs = Column(String)
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship('puppy', back_populates="profile")


class Adopter(Base):
    __tablename__ = 'adopter'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    adopted_puppies = relationship(Puppy, secondary=association_table, back_populates="adopters")


class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable=False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))
    profile = relationship(Profile, uselist=False, back_populates="puppy")
    adopters = relationship(Adopter, secondary=association_table, back_populates="adopted_puppies")









engine = create_engine('sqlite:///puppyshelter.db')
 

Base.metadata.create_all(engine)
