data_file = open("bank.txt")
product = []
price = []
while True:
    line = data_file.readline()
    if line == "":
        break
    line_list = line.split()
    product.append(line_list[0])
    price.append(int(line_list[1]))
data_file.close()
print(product)
print(price)
print()


def menu():
    menu_options =("1.Display price of product specified\n"
                   "2.Edit price of product\n"
                   "3.Print Table of price and Products\n"
                   "4.Quit Program\n")
    print(menu_options)
    loop = True
    while loop:
        choice = int(input("Please enter option 1-4: "))
        if choice == 1:
            while True:
                specified_product = input("What product price you want to know: ")
                if specified_product not in product[:]:
                    print("Enter a valid product name  !!! ")
                    continue
                else:
                    break
            location = product.index(specified_product)
            print("Price of " + str(specified_product) + " is: €" + str(price[location]))
            print()
            print(menu_options)
        elif choice == 2:
            print("2")
        elif choice == 3:
            print("3")
        elif choice == 4:
            loop = False
            break
        else:
            print(menu_options)


def main():
    menu()


main()
