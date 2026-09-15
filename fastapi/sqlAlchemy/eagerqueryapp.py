from sqlalchemy import select
from sqlalchemy.orm import defaultload, joinedload, selectinload, subqueryload, immediateload

from eagerqueryoptions import Detail, Post, User, session

query = session.query(User)
print(query)

query = session.query(User).options(joinedload(User.posts)).all()
# print(query)

users = session.query(User).all()

for user in users:
    print(f"{user.name}'s Posts")
    # print(user.posts)
    for x in range(len(user.posts)):
        print(user.posts[x].Detail.content)