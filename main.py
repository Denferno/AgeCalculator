import time

today = time.localtime() #The number of seconds since epoch
yearNow = today.tm_year
monthNow = today.tm_mon
dayNow = today.tm_mday
birthDay = int(input("Vul hier jouw geboortedag in (getallen!!): "))
birthMonth = int(input("Vul hier jouw geboortemaand in (getallen!!): "))
birthYear = int(input("Vul hier jouw geboortejaar in (getallen!!): "))


dag = birthDay - dayNow
age = yearNow - int(birthYear)
if birthMonth > 12 or birthDay > 31:
    print("Ga niet liegen")
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

