#In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
#You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

text = ""
text += "hello "
text += "world"


імена = ["Rostyslav", "Andriy", "Orest"]
second_name = імена[1]  

print("Список чисел:", numbers)
print("Рядок зі словами:", text)
print("Друге ім'я:", second_name)
