country_list = []
#countries = input("Listaa 5 kaupunkia: ")
iterator = 0
while iterator < 5:
    countries = input("Listaa 5 kaupunkia: ")
    country_list.append(countries)
    iterator += 1

for i in range(len(country_list)):
    print(country_list[i])


#print(country_list)