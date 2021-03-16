yearNow = 2020
monthNow = 11
dayNow = 25
birthYear = int(input("Vul hier jouw geboortejaar in: "))
birthMonth = int(input("Vul hier jouw geboortemaand in: "))
birthDay = int(input("Vul hier jouw geboortedag in: "))

dag = birthDay - dayNow
age = yearNow - int(birthYear)
if birthMonth > 12 or birthDay > 31:
    print("Ga niet lullen")
elif birthMonth > monthNow:
    age -= 1
    print("Je bent " + str(age) + " jaar")
elif birthMonth == monthNow:
    if birthDay > dayNow:
        age -= 1
        print("Je bent " + str(age) + " jaar")
    else:
        print("Je bent " + str(age) + " jaar")
else:
    print("Je bent " + str(age) + " jaar")

