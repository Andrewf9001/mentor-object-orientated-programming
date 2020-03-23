class Website:
    def __init__(self, title):
        self.title = title # instance atribute, and attribute that belongs to this instance
        attribute belongs to the class

ws = Website('My Website Title')
print(ws.title)
# print(ws.__dict__) # returns {'title': 'My Website Title' }

ws_two = Website('Second Title')
print(ws_two.__dict__) # returns { 'title': 'Second Title' }

class DifferentWebsite:
    title = 'My Class Title'


dw = DifferentWebsite()
print(dw.__dict__) # returns {}
print(dw.title) # prints 'My Class Title'

# Class attribute is a attribute that belongs to the class definition
# Hard coded into the class and you can call it whenever you need it

# Instance attribute belongs to the instance Website('My Website Title')