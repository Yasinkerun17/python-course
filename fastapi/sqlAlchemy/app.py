import random

from sqlalchemy import and_, func, not_, or_
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

#----Create Data-------------
""" user = User(name="john doe", age=30)
    session.add(user)
    session.add_all([user_1, user_2])
"""

session = Session()
#name="John doe"

users = session.query(User).filter_by(name="John Wick").all()

#-----Read data-------
""" for user in users:
     print(f"user_id: {user.id}, username: {user.name}, age: {user.age}")
     print("----------------------------------------")
"""
    
#----update data---------
#  user.name = "John wick"

#----delete data---------
# session.delete(user)

users = session.query(User).order_by(User.age.desc()).all()

users = session.query(User).filter(User.id > 4).all()

users = session.query(User).where(not_(User.age > 25)).all()


users = (
    session.query(User).where(
        or_(
            not_(User.name =="Tony Stark"),
            
            and_(User.age > 35,
                 User.age < 60
            )
        )
    )
).all()

users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all()
)

# for age, count in users_tuple:
#     print(f"age: {age} - {count} users")

users = session.query(User)

only_Tony_Stark = True
only_group_by_age = True

if only_Tony_Stark:
    users = users.filter(User.name == "Tony Stark")
    
if only_group_by_age:
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f" User age: {user.age} name: {user.name}")

