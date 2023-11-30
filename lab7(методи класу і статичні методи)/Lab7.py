
import datetime

class MyTetsClass:
    num_of_users = 0
    age_in_2016 = -5
    defoult_age = 20

    def __init__(self, name, age, nation):
        self.name = name
        self.age = age
        self.nation = nation
        self.fullinfo = 'My name ' + name + ', nationality - ' + nation + '.'
        MyTetsClass.num_of_users += 1

    def about_me(self):
        print(self.fullinfo)
        return self.fullinfo

    def what_age_in_2016(self):
        self.age = int(self.age + self.age_in_2016)
        print(self.age)

    @classmethod
    def plus_input_years(cls, plus_years):
        cls.defoult_age = cls.defoult_age + plus_years

    @classmethod
    def new_user(cls, user):
        name, age, nation = user.split('/')
        return cls(name, age, nation)

    @staticmethod
    def with_day(day):
        if day.weekday() == 5:
            print("�������� ����!!! - ������")
            return False
        elif day.weekday() == 6:
            print("�������� ����!!! - �����")
            return False
        else:
            print("����� ����")
            return True

info = MyTetsClass("Rostyslav", 20, "ua")
info1 = MyTetsClass("Max", 12, "us")
info2 = MyTetsClass("Volodymyr", 17, "uk")

MyTetsClass.about_me(info)
MyTetsClass.about_me(info1)
MyTetsClass.about_me(info2)

MyTetsClass.what_age_in_2016(info)
MyTetsClass.what_age_in_2016(info1)
MyTetsClass.what_age_in_2016(info2)

print('˳������� ����� = ' + str(MyTetsClass.num_of_users))

print("��������� �������� defoult_age:", MyTetsClass.defoult_age)
MyTetsClass.plus_input_years(30)
print("���� �������� defoult_age:", MyTetsClass.defoult_age)

# ����/��������� ������ ������ ����� classmethod
user_1 = "Alla/31/ua"
user_2 = "John/18/bl"

new_user1 = MyTetsClass.new_user(user_1)
new_user2 = MyTetsClass.new_user(user_2)
print(new_user1.fullinfo)
print(new_user2.fullinfo)

# C�������� �����
date = datetime.date(2001, 9, 15)
MyTetsClass.with_day(date)