# Inheritance is the ability to create specilized versions of classes

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'


class AdminUser(User):
    def active_users(self):
        return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')
kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
# print(kristine.active_users()) # returns an error User object has no attribute active_users
print(tiffany.greeting()) # returns Hi Tiffany Hudgens This is possible because of inheritance