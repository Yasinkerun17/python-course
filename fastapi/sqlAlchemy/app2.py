from models2 import User, session
# creating users
user1 = User(username="John smith")
user2 = User(username="Jane smith")
user3 = User(username="Jack smith")

user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

session.add_all([user1, user2, user3])

session.commit()

print(f"{user1.following = }")
print(f"{user2.following = }")
print(f"{user3.following = }")