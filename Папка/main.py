name = input("Яке твоє ім'я?")
secondname = input("Яке твоя прізвище?")
birthyear = input("Якого року ти народження?")
birthdate = input("Якого місяця та дня ти народження?")
yearsold = input("Скільки тобі років?")
address = input("Де ти живеш?")
education = input("Де ти зараз навчаєшся?")
specialty = input("На яку спеціальність ти навчаєшся?")
hobby = input("Яке твоє улюблене хоббі?")
languages = input("Чи говориш ти на мовах крім Україньскої? (Пишіть 'Так' чи 'Ні')")
character = input("Які твої сильні риси характеру?")
charweak = input("Які твої слабі риси характеру?")
university = input("Чи плануєш вступ до університету в майбутньому? (Пишіть 'Так' чи 'Ні')")

print("Привіт, " + name + " " + secondname + "!")
print("Тобі " + yearsold + " років!")
print("Ти народився в місяці " + birthdate + ", та в дні " + birthyear)
print("Ти живеш в " + address)
print("Ти зараз навчаєшся в " + education + ", на спеціальність " + specialty)
print("Твоє улюблене хоббі є " + hobby + "!")
print("Твої сильні риси характеру є " + character)
print("Твої слабі риси характеру є " + charweak )

if languages == "Так":
    print("Ти говориш більше чим на одній мові!")
else:
    print("Ти володієш тільки Україньскою мовою")
if university == "Так":
    print("Ти плануєш вступ до університету в майбутньому")
else:
    print("Ти не плануєш вступ до університету в майбутньому")