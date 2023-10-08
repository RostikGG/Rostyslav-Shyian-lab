# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

# додаємо Джейка
phonebook["Jake"] = 938273443

# Видаляємо Джилл з телефонної книги 
if "Jill" in phonebook:
    del phonebook["Jill"]

if "Jake" in phonebook:
    print("Джейка знайденно в телефонній книзі.")
    
if "Jill" not in phonebook:
    print("Джилл не знайденно в телефонні книзі.")

print("Оновленна телефонна книга:", phonebook)