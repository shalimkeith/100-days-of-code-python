class User:
    def __init__(self, name, email, id, age):
        self.name = name
        self.email = email
        self.id = id
        self.age = age
        self.followers = 0
        self.following = 0
        print("New user is being created....")

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User("Shalim Keith", "shalimkeith@gmail.com", 70242, 22)
user2 = User("Dino Duck", "dinosduckeggs@gmail.com", 70243, 21)
user2.follow(user1)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
