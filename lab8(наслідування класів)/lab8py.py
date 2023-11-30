
class Citizen_of_Ukraine:
  percentage_of_taxes = 0.18

  def __init__(self, name, pay, position):
      self.name = name
      self.pay = pay
      self.position = position
      self.fullinfo = 'Name ' + name + ', payment ' + str(pay) + ', position - ' + position + '.'

  def fullname(self):
      return '{} - {}'.format(self.name, self.position)

  def about_me(self):
      print(self.fullinfo)
      return self.fullinfo

  def percentage(self):
      self.pay = int(self.pay - (self.pay * self.percentage_of_taxes))


class citizen_of_another_state(Citizen_of_Ukraine):
  percentage_of_taxes = 0.25

  def __init__(self, name, pay, position, nation):
      super().__init__(name, pay, position)
      self.nation = nation


class Directors(Citizen_of_Ukraine):

  def __init__(self, name, pay, position, users=None):
      super().__init__(name, pay, position)
      if users is None:
          self.users = []
      else:
          self.users = users

  def fullname(self):
      return '{} - {}'.format(self.name, self.position)

  def add_loc(self, loc):
      if loc not in self.users:
          self.users.append(loc)

  def remove_loc(self, loc):
      if loc in self.users:
          self.users.remove(loc)

  def print_loc(self):
      for loc in self.users:
          print('-->', loc.fullname())


user1 = Citizen_of_Ukraine("Rostyslav", 1000, "developer")
user2 = Citizen_of_Ukraine("Max", 1200, "graphic designer")
user3 = Citizen_of_Ukraine("Volodymyr", 2900, "product manager")
user4 = citizen_of_another_state("Nazar", 1800, "php-developer", "pl")

Citizen_of_Ukraine.about_me(user1)
Citizen_of_Ukraine.about_me(user2)
Citizen_of_Ukraine.about_me(user3)

print("Pay Max:",user2.pay)
user2.percentage()
print("Pay with taxes:", user2.pay)

print("National Nazar:",user4.nation)
print("Pay Nazar:",user4.pay)
user4.percentage()
print("Pay foreigner with taxes:", user4.pay)

loc_5 = Directors("Lana", 4000, "director", [user1])

print(loc_5.fullname())
loc_5.add_loc(user4)
loc_5.print_loc()

print(isinstance(loc_5, Citizen_of_Ukraine))
print(isinstance(loc_5, citizen_of_another_state))
print(isinstance(user4, Directors))

print(issubclass(citizen_of_another_state, Citizen_of_Ukraine))
print(issubclass(citizen_of_another_state, Directors))
print(issubclass(Citizen_of_Ukraine, Directors))
print(issubclass(Directors, citizen_of_another_state))

print(loc_5.fullname())
loc_5.remove_loc(user1)
loc_5.print_loc()