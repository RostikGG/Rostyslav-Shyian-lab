class MyTetsClass:

    num_of_users = 0
    age_in_2016 = -7

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.fullinfo='My name ' + self.name + ', age ' + '.'
        MyTetsClass.num_of_users += 1

    def about_me(self):
        print(self.fullinfo)
        return self.fullinfo

    def what_age_in_2016(self):
        self.age = int(self.age + self.age_in_2016)
        print(self.age)

info = MyTetsClass("Rostyslav", 20)
info1 = MyTetsClass("Max", 12)
info2 = MyTetsClass("Volodymyr", 17)

info.what_age_in_2016()
info1.what_age_in_2016()
info2.what_age_in_2016()

print('Ë³÷èëüíèê îáºêò³â = ' + str(MyTetsClass.num_of_users))

