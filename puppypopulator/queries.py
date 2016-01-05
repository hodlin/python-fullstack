from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy
import datetime
from sqlalchemy.sql.functions import count

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# shelters = session.query(Shelter).all()
# puppies = session.query(Puppy).order_by(Puppy.name).all()
# today = datetime.date.today()
# young_puppies = session.query(Puppy).\
#     filter(Puppy.dateOfBirth > today - datetime.timedelta(days=30*6)).order_by(Puppy.dateOfBirth.desc())
shelters = session.query(Shelter.name, count(Puppy.id)).join(Puppy).group_by(Puppy.shelter_id).all()
#
# for shelter in shelters:
#     print(shelter.name)
#
# for puppy in puppies:
#     print(puppy.name)

# for puppy in young_puppies:
#     print(puppy.name)
#     print(today - puppy.dateOfBirth)
#
# print(today - datetime.timedelta(days=30*6))

for shelter in shelters:
    print("{0} : {1}".format(shelter[0], shelter[1]))

print(shelters)
