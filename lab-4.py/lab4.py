# Функція list_benefits повертає список рядків
def list_benefits():
    return [
        "Більш упорядкований код",
        "Більш читабельний код",
        "Легше повторне використання коду",
        "Дозволяє програмістам ділитися та з’єднувати код разом"
    ]

# Функція build_sentence отримує рядок і повертає речення
def build_sentence(benefit):
    return benefit + " це перевага функцій!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
