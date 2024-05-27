class UserGroup:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class User:
    query = None

    def __init__(self, username, group):
        self.username = username
        self.group = group

    def save(self):
        pass


# Create user groups
customer_1 = UserGroup("Customer 1")
customer_2 = UserGroup("Customer 2")
customer_3 = UserGroup("Customer 3")

# Create users and assign them to groups
user1 = User("user1", customer_1)
user2 = User("user2", customer_2)
user3 = User("user3", customer_3)

customer_1.add_user(user1)
customer_2.add_user(user2)
customer_3.add_user(user3)
