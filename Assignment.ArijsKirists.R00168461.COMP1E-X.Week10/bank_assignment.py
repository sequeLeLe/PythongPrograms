import random

data_file = open("bank.txt")
account = []
balance = []
names = []

while True:
    line = data_file.readline()
    if line == "":
        break
    line_list = line.split()
    account.append((line_list[0]))
    balance.append((line_list[1]))
    names.append(line_list[2])
data_file.close()

print(account)
print(balance)
print(names)
print()


def random_account_generator():
    min_number = 0
    max_number = 99999
    digits = str(random.randint(min_number, max_number))
    while True:
        digits = str(random.randint(min_number, max_number))
        # Generates random number from 0-99999
        if digits in account[:]:
            # if random number comes up as the same as one in existence in list account[:], regenerates another one
            digits = str(random.randint(min_number, max_number))
        else:
            break
    return digits


def menu():
    menu_options =("1.Open an Account\n"
                   "2.Close an Account\n"
                   "3.Withdraw Money\n"
                   "4.Deposit Money\n"
                   "5.Generate a report for management\n"
                   "6.Quit")
    print(menu_options)
    loop = True
    while loop:
        choice = int(input("Please enter option 1-6: "))
        if choice == 1:
            new_account_name = input("Enter your name: ")
            import random
            new_account_number = random_account_generator()
            new_account_balance = 0

            print("Account Number: " + str(new_account_number))
            print("Name: " + str(new_account_name))
            print("Balance: €" + str(new_account_balance))

            account.append(new_account_number)
            balance.append(new_account_balance)
            names.append(new_account_name)

            data_file = open('bank.txt', 'a') # Appends new information to bank.txt
            data_file.write("\n")
            data_file.write(new_account_number)
            data_file.write(" " + str(new_account_balance))
            data_file.write(" " + new_account_name)
            data_file.close()
            print(account)
            print(balance)
            print(names)



            # while True:
            #     specified_product = input("What product price you want to know: ")
            #     if specified_product not in product[:]:
            #         print("Enter a valid product name  !!! ")
            #         continue
            #     else:
            #         break
            # location = product.index(specified_product)
            # print("Price of " + str(specified_product) + " is: €" + str(price[location]))
            # print()
            # print(menu_options)
        elif choice == 2:
            print("2")
        elif choice == 3:
            print("3")
        elif choice == 4:
            print("4")
        elif choice == 5:
            print("5")
        elif choice == 6:
            loop = False
            break
        else:
            print(menu_options)


def main():
    menu()


main()
