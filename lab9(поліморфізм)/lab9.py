class MyClass:

    def __init__(self, name, secnd, age):
        self.name = name
        self.secnd = secnd
        self.age = age

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name, self.secnd)

    @property
    def about_me(self):
        return '{} {}'.format(self.name, self.secnd)

    @about_me.setter
    def about_me(self, title):
        name, secnd = title.split(' ')
        self.name = name
        self.secnd = secnd

    @about_me.deleter
    def about_me(self):
        print("DELETE name!")
        self.name = None
        self.secnd = None


user1 = MyClass("Rostyslav", "Shyian", 29)

user1.secnd = "Shyian"

print(user1.email)
print(user1.about_me)

del user1.about_me

print(user1.email)