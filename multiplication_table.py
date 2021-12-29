

# print("----------------------------")
# print("             1              ")
# print("         1 x 1 = 1          ")
# print("         1 x 2 = 2          ")
# print("         1 x 3 = 3          ")
# print("         1 x 4 = 4          ")
# print("         1 x 5 = 5          ")
# print("----------------------------")
# print("----------------------------")
# print("             1              ")
# print("         1 x 1 = 1          ")
# print("         1 x 2 = 2          ")
# print("         1 x 3 = 3          ")
# print("         1 x 4 = 4          ")
# print("         1 x 5 = 5          ")
# print("----------------------------")

boundary = 32
space = ' '
for i in range(1, 13):
    print("1234567890x1234567890=1234567890")
    print(boundary*"-")
    table_number = f'{i}'
    spaces_left = round((boundary - len(table_number))/2)
    spaces_right = boundary - spaces_left + len(table_number)
    print(f'{spaces_left*space}{table_number}{spaces_right*space}')

    test = ""
    for j in range(1, 13):

        sub_boundary = 10

        spaces_left_1 = round((sub_boundary - len(str(i)))/2)
        spaces_right_1 = sub_boundary - spaces_left_1 - len(str(i))

        spaces_left_2 = round((sub_boundary - len(str(j)))/2)
        spaces_right_2 = sub_boundary - spaces_left_2 - len(str(j))

        spaces_left_3 = round((sub_boundary - len(str(i*j)))/2)
        spaces_right_3 = sub_boundary - spaces_left_3 - len(str(i*j))

        output = f'{spaces_left_1*space}{i}{spaces_right_1*space}x{spaces_left_2*space}{j}{spaces_right_2*space}={spaces_left_2*space}{i*j}{spaces_right_2*space}'

        print(output)
        test = spaces_right_1*space

    print(boundary*"-")
    
# i = 22
# print(len(str(i)))
