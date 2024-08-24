import.math
#name = "x"


name = input("What is you name? \n")

print("hi " + name)

# age = "7"

age = input("What is your age? \n")

#print("your age is " + age)



#age = "7"
#käyttäjän syöte on aina merkkijono
age = input("Anna ikäsi: ")
print("Ikäsi on " +  age)

#muutetaan merkkijono str kokonaisluvuksi int ja lisätään 1
age = int(age) + 1
#esitellään uusi muuttuja, johon sijoitetaan numeroarvo merkkinä int
age_string= str(age)
print("Ikäsi on vuoden päästä " + age_string)
age = age + 1

print("Ikäsi on kahden vuoden päästä " + str(age))

# Käyttäjän pituus metreinä, liukuluku (float)
#height = 1.8
height = input("Anna pituus: ")
#kysytään käyttäjän pituus ja muutetaan samantien liukluvuksi
height = float(height)
#kasvatetaan käyttäjää 10cm
height = height + 0.1
print(f"Nimi: {name}, Ikä: {age}, Pituus: {height:.2f}.")




