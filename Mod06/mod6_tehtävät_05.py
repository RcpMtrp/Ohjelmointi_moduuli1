def lukujensumma():
    number_list = []
    numbers = input("Anna kokonaislukuja ja paina enter lopettaaksesi.")
    while numbers != "":
        number_list.append(int(numbers))
        numbers = input("Anna seuraava luku tai lopeta painamalla Enter: ")
    number_list.append(numbers)
    del number_list[-1]


    for i in number_list:
        if i % 2 == 0:
            number_list.remove(i)
            print(number_list)
            return number_list



    #print(summed_list)

tulos = lukujensumma()
print(tulos)