input_string = input("Syötä luku: ")
if input_string != "":
    max_num = min_num = int(input_string)

    while input_string != "":
        input_string = input("Syötä luku: ")
        if input_string != "":
            number = int(input_string)
            if number > max_num:
                max_num = number
            if number < min_num:
                min_num = number

    print(f"Pienin numero: {min_num}, suurin numero: {max_num}")
else:
    print("Ei lukuja syötetty")

'''
max_num = min_num = int(input("Syötä luku: "))

while True:
    input_string = input("Syötä luku: ")
    if input_string == "":
        break
    number = int(input_string)
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f"Pienin numero: {min_num}, suurin numero: {max_num}")
'''