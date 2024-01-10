#initialize: set values to starting value. Constructor
class User:
    def __init__(self, user_id, username):
        print("new user created")
        self.id = user_id
        self.username = username
        

user_1 = User("001","Johnathon")
user_2 = User("002", "Mary")

user_1.username = "Johnathon"

user_1.username = "Mary"

print(user_1.username) 
print(user_2.username) 
print(user_1.id) 
print(user_2.id) 


