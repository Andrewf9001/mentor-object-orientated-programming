# Classes are object mappers, essentially gives you an ability to create a blueprint
# for objects

class Invoice:

    def greeting(self):
        return 'Hi there'

# must perform instantiation
inv_one = Invoice()
# print(inv_one) # returns <__main__.Invoice instance at 0x1050d3680>
inv_two = Invoice()
# print(inv_two) # returns <__main__.Invoice instance at 0x1050d36c8>

print(inv_one.greeting()) # returns Hi there
print(inv_two.greeting()) # ^              ^

# self references the instance