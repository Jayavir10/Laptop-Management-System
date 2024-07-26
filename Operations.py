from Read import laptop_table, read_laptops
from Write import purchase_bill_print_and_generation, sale_bill_print_and_generation

# Sale function which will perform the sale task
def sale_laptop():

    # Assign the return value of read_laptops() function to a variable
    laptops_list = read_laptops()

    # Use while loop to take valid name of the customer
    while True:
        user_name = input("Enter the name of the customer: ")
        print("\n")
        # If the input is empty
        if user_name == "":
            print("Customer name cannot be empty. Please enter the name of the customer")
            print("\n")
        # Breaks the while loop
        else:
            break
    
    while True:
        try:
            user_number = int(input("Enter the phone number of the customer: "))
        # Handle non_numeric value in the phone number
        except ValueError:
            print("\n")
            print("### ERROR! Please enter a valid Phone-number ###")
            print("\n")
            continue
        print("\n")

        # Break the loop if the phone numer is 10 digit
        if len(str(user_number)) == 10:
            break

        # Continue the loop
        else:
            print("## INVALID phone number. Please enter a valid 10-digit phone number ##")
            print("\n")

    # Call laptop_table function
    laptop_table()
    
    # Declare an empty list to store the sold laptop details
    sold_laptops = []

    # Ask the id of the laptop to sale
    sale = True
    while sale:
        try:
            user_buy_id = int(input("Enter the ID for the laptop you want to sell : "))
        except ValueError:
            print("\n")
            print("### ERROR! Please enter a valid laptop ID. ###")
            print("\n")
            continue
        print("\n")
        
        # Iterate over the each element in laptops_list 
        for eachlaptop in laptops_list:
            # If the id in the list matches with the input id
            if int(eachlaptop[0]) == user_buy_id:
                sale_confirmation = True
                # Confirmation of sale
                while sale_confirmation:
                    choice =  input(f"Do you want to sell {eachlaptop[1]} (yes/no): ").lower()
                    print("\n")
                    if choice == 'yes':
                        # Ask the quantity
                        while True:
                            try:
                                user_quantity = int(input("Enter the number of laptop you want to sell: "))
                            except ValueError:
                                print("\n")
                                print("### ERROR! Please enter a valid laptop quantity ###")
                                print("\n")
                                continue
                            print("\n")

                            # If the input quantity is less than or equal to zero
                            if user_quantity <= 0:
                                print("INVALID QUANTITY! Please enter a valid numerical quantity.")
                                print("\n")
                                continue
                            
                            # If the input quantity is less than the available quantity
                            elif user_quantity <= int(eachlaptop[4]):
                                #Update Quantity (Decrease):
                                eachlaptop[4] = str(int(eachlaptop[4]) - user_quantity)

                                # Overwrite each line in the file laptops.txt which will also add the updated quantity
                                filer = open("laptops.txt","w")
                                for writer in laptops_list:
                                    filer.write(writer[1]+","+writer[2]+","+writer[3]+","+ writer[4]+","+writer[5]+","+writer[6]+"\n")
                                filer.close()
                                
                                # Store the details of sold laptops to the list
                                sold_laptops.append([eachlaptop[0],eachlaptop[1],eachlaptop[2],eachlaptop[3],user_quantity,eachlaptop[5],eachlaptop[6]])
                                
                                # Ask to sell more laptops
                                while True:
                                    sale_again = input("Do you want to sell more laptops? (yes/no): ").lower()
                                    print("\n")
                                    if sale_again == "yes":
                                        # Ask to sell the laptops to same or new customer
                                        while True:
                                            new_old_user = input("Do you want to sell laptops to the same or new customer? (same/new): ")
                                            print("\n")
                                            if new_old_user == "same":
                                                laptop_table()
                                                break
                                            elif new_old_user == "new":
                                                print("**BEFORE SELLING THE LAPTOPS TO THE NEW CUSTOMER PLEASE GENERATE THE BILL AND COMPLETE YOUR CURRENT SALE**")
                                                print("\n")
                                                # Call the sale_bill_print_and_generation() function to generate the bill
                                                sale_bill_print_and_generation(user_name, user_number, sold_laptops)
                                                print("\n")
                                                sale = False
                                                sale_laptop()
                                                break
                                            else:
                                                print("INVALID INPUT! Please enter SAME or NEW")
                                                print("\n")
                                        break
                                    elif sale_again == "no":
                                        # Call the sale_bill_print_and_generation() function to generate the bill
                                        sale_bill_print_and_generation(user_name, user_number, sold_laptops)
                                        print("Thank you for using our system. See you!")
                                        print("\n")
                                        # Execute the main function
                                        main()
                                        sale_confirmation = False
                                        sale = False
                                        break
                                    else:
                                        print("INVALID INPUT! Please enter YES or NO")
                                        print("\n")
                                break    
                            else:
                                print("SORRY! the quantity you are looking for is not available. Please enter a valid quantity.")
                                print("\n")
                                continue
                        break
                    elif choice == "no":
                        print("SALE CANCELLED! Please enter the valid laptop ID again.")
                        print("\n")
                        break
                    else:
                        print("### INVALID INPUT. Please enter YES or NO")
                        print("\n")
                        continue
                break
        else:
            print("Seems like the ID you chose is not availabe please enter a valid ID")
            print("\n")
        continue

# Purchase function which will perform the purchase task
def purchase_laptop():
    # Store the read_laptops function to a variable
    existing_laptops = read_laptops()

    # Declare a variable with empty list to store purchased laptops
    purchased_laptops = []


    buy_new_laptop = True
    # Ask to buy new or existing laptops
    while buy_new_laptop:
        new_or_existing_laptop = input("Do you want to purchase New or Existing laptop? (n/e): ").lower()
        print("\n")
        if new_or_existing_laptop == "n":
            # Execute the buy_new_laptops_table function to display the laptops in tabular format
            buy_new_laptops_table()

            #Store the new laptop details in a 2D list
            new_laptops = [['1', 'Nitro 5', 'Acer', '1100', 'i5 11th Gen', 'RTX 3050'],
                           ['2', 'Predator', 'Acer', '2800', 'i9 13th Gen', 'RTX 4080'],
                           ['3', 'Legion', 'Lenovo', '1300', 'i7 11th Gen', 'RTX 3050'],
                           ['4', 'Asus TUF', 'Asus', '1450', 'i5 12th Gen', 'RTX 3060']]

            # Ask the id to purchase
            ask_id = True
            while ask_id:
                try:
                    new_laptop_id = int(input("Enter the ID of the laptop you want to buy: "))
                    print("\n")
                except:
                    print("\n")
                    print("ERROR! INVALID INPUT! Please enter a valid numerical input")
                    print("\n")
                    continue
                
                # Iterate over the each line in the new_laptops list
                for eachnewlaptop in new_laptops:
                    # if the Id of the laptop in the list matches with the input ID
                    if int(eachnewlaptop[0]) == new_laptop_id:
                        # Confirm purchase
                        while True:
                            confirm_new = input (f"Do you want to buy {eachnewlaptop[1]}? (yes/no): ").lower()
                            print("\n")
                            if confirm_new == "yes":
                                # Ask Quantity
                                while True:
                                    try:
                                        new_quantity = int(input("Enter the quantity of laptop you want to buy: "))
                                        print("\n")
                                    except:
                                        print("\n")
                                        print("ERROR! INVALID INPUT! Please enter a valid numerical input")
                                        print("\n")
                                        continue
                                    # If the quantity input is greater than 0
                                    if new_quantity > 0:
                                        
                                        # Append the selected_laptops list with the details of the purchased laptops
                                        selected_laptop = ([len(existing_laptops) + 1, eachnewlaptop[1], eachnewlaptop[2], int(eachnewlaptop[3]), new_quantity, eachnewlaptop[4], eachnewlaptop[5]])
                                        # Append the selected_laptops to existing_laptops list
                                        existing_laptops.append(selected_laptop)
                                        # Append the purchased_laptops list with the details of the purchased laptops
                                        purchased_laptops.append([eachnewlaptop[1], eachnewlaptop[2], int(eachnewlaptop[3]), new_quantity, eachnewlaptop[4], eachnewlaptop[5]])

                                        break
                                    else:
                                        print("INVALID QUANTITY! Please enter a valid numerical quantity which is greater than 0")
                                        continue
                                # Ask to buy more
                                while True:
                                    buy_new_more = input("Do you want to buy more new laptops? (yes/no): ").lower()
                                    print("\n")
                                    if buy_new_more == "yes":
                                        buy_new_laptops_table()
                                        break
                                    elif buy_new_more == "no":
                                        # Print the bill
                                        purchase_bill_print_and_generation(purchased_laptops)

                                        #Update and increase the price by 100$ in laptops.txt file
                                        selling_price_of_selected_laptop = int(eachnewlaptop[3]) + 100

                                        #Updates the laptops.txt file by overwriting the each line in the file
                                        filer = open("laptops.txt","w")
                                        for writer in existing_laptops:
                                            if writer[1] == selected_laptop[1] and writer[2] == selected_laptop[2] and writer[3] == int(eachnewlaptop[3]):
                                                writer[3] = selling_price_of_selected_laptop
                                            filer.write(writer[1]+","+writer[2]+","+str(writer[3])+","+ str(writer[4])+","+writer[5]+","+writer[6]+"\n")
                                        filer.close()
                                        # Execute the main() function
                                        main()
                                        ask_id = False
                                        buy_new_laptop = False
                                        break
                                    else:
                                        print("INVALID INPUT! Please enter YES or NO")
                                        print("\n")
                                break
                            elif confirm_new == "no":
                                break
                            else:
                                print("INVALID INPUT! Please enter YES or NO.")
                                print("\n")
                        break
                else:
                    print("Seems like the ID you chose is not available. Please enter a valid laptop ID")
                    print("\n")
                continue
        # if the input is existing laptops
        elif new_or_existing_laptop == "e":
            # Execute/call the laptop_table function
            laptop_table()
            print("NOTE: BUYING PRICE OF YOUR EXISTING LAPTOP'S WILL BE 100$ LESS THAN YOUR CURRENT SELLING PRICE THAT IS SHWON IN THE ABOVE TABLE")
            print("\n")
            ask_existing_id = True
            # ASk the Id of the laptop
            while ask_existing_id:
                try:
                    existing_id = int(input("Please enter the ID of the laptop you want to buy: "))
                    print("\n")
                except ValueError:
                    print("\n")
                    print("### Error! INVALID INPUT! Please enter a valid Laptop ID.")
                    print("\n")
                    continue
                # Iterate over the each line of the exisiting_laptops list
                for eachlaptop in existing_laptops:
                    # If the laptop Id in the list matches with the input laptop Id
                    if int(eachlaptop[0]) == existing_id:
                        buy_confirm = True
                        # Confirm buy
                        while buy_confirm:
                            confirm = input(f"Do you want to buy {eachlaptop[1]}? (yes/no/cancel): ").lower()
                            print("\n")
                            if confirm == "yes":
                                # Ask quantity
                                while True:
                                    try:
                                        quantity = int(input(f"Enter the number of {eachlaptop[1]} you want to buy: "))
                                        print("\n")
                                    except ValueError:
                                        print("\n")
                                        print("### Error ! INVALID INPUT! Please enter a valid numerical input.")
                                        print("\n")
                                        continue
                                    # if quantity is zero and less than zero
                                    if quantity == 0 or quantity < 0:
                                        print("INVALID QUANTITY! Please enter a valid quantity")
                                        print("\n")
                                        continue
                                    # set the buying price of the laptop
                                    while True:
                                        buying_price_of_laptop = (int(eachlaptop[3])) - 100
                                        # Confirm quantity
                                        quantity_confirmation = input(f"Do you wany to buy {quantity} {eachlaptop[1]} each for {buying_price_of_laptop}? (yes/no): ")
                                        print("\n")

                                        if quantity_confirmation == "yes":
                                            
                                            # Update Quantity(Increase):
                                            eachlaptop[4] = str(int(eachlaptop[4]) + quantity)

                                            # Update the each line in the file by overwriting the file
                                            filer = open("laptops.txt","w")
                                            for writer in existing_laptops:
                                                filer.write(writer[1]+","+writer[2]+","+writer[3]+","+writer[4]+","+writer[5]+","+writer[6]+"\n")
                                            filer.close()

                                            # Append the purchased_laptops list with the details of the purchased laptops
                                            purchased_laptops.append([eachlaptop[1], eachlaptop[2], buying_price_of_laptop, quantity, eachlaptop[5], eachlaptop[6]])

                                            # Ask to buy more laptops
                                            while True:
                                                buy_again = input("Do you want to buy more exisiting laptops? (yes/no): ")
                                                print("\n")

                                                if buy_again == "yes":
                                                    laptop_table()
                                                    print("NOTE: BUYING PRICE OF YOUR EXISTING LAPTOP'S WILL BE 100$ LESS THAN YOUR CURRENT SELLING PRICE SHOWN IN THE ABOVE TABLE")
                                                    print("\n")
                                                    buy_confirm = False
                                                    break

                                                elif buy_again == "no":
                                                    # Print the bill
                                                    purchase_bill_print_and_generation(purchased_laptops)
                                                    print("Thankyou for using our system. Visit again!")
                                                    print("\n")
                                                    main()
                                                    buy_confirm = False
                                                    ask_existing_id = False
                                                    ask_id = False
                                                    buy_new_laptop = False
                                                    break
                                                
                                                else:
                                                    print("INVALID INPUT! Please enter YES or NO")
                                                    print("\n")
                                            break
                                        elif quantity_confirmation == "no":
                                            buy_confirm = False
                                            break
                                        else:
                                            print("INVALID INPUT! Please enter YES or NO")
                                            print("\n")
                                    break
                            elif confirm == "no":
                                print(f"Purchase of {eachlaptop[1]} cancelled !!")
                                print("\n")
                                break
                            
                            elif confirm == "cancel":
                                print("Purchase of existing laptop cancelled !!")
                                print("\n")
                                purchase_laptop()
                            
                            else:
                                print("### INVALID INPUT ! Please enter YES, NO or CANCEL ###") 
                                print("\n")
                        break
                else:
                    print("Seems like the ID you chose is not available. Please enter a valid laptop ID")
                    print("\n")
                    continue
        else:
            print("### INVALID OPTION ! Please enter new or existing ###")
            print("\n")

# Declare a function and print the details of the new laptops to display
def buy_new_laptops_table():
    print("These are the new laptops that are available right now")
    print("-----------------------------------------------------------------------------------")
    print("ID        Name          Brand        Price         Generation         Graphics")
    print("-----------------------------------------------------------------------------------")
    print("1         Nitro 5       Acer         1100$         i5 11th Gen        RTX 3050   ")
    print("2         Predator      Acer         2800$         i9 13th Gen        RTX 4080   ")
    print("3         Legion        Lenovo       1300$         i7 11th Gen        RTX 3050   ")
    print("4         Asus TUF      Asus         1450$         i5 12th Gen        RTX 3060   ")
    print("\n")

# Main funtion of the program
def main():
    # Displaying welcome message
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|                                                WELCOME TO JB ELECTRONICS, MAHARJGUNJ, KATHMANDU                                                  |")
    print("|                                                      Phone No: +977 9812345678, 01-1234567                                                       |")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    # Displaying the options
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Please select the option below to continue: ")
    print("\n")
    print("Press 1 to Sale laptops to the customers")
    print("Press 2 to Purchase the laptops from the manufacturers")
    print("Press 3 to Exit the system")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    try:
        # Getting the user input
        user_choice = int(input("Enter the valid option : "))
        print("\n")
        # Call sale function if input is 1
        if user_choice == 1:
            sale_laptop()

        # Call purchase function if input is 2
        elif user_choice == 2:
            purchase_laptop()

        # Exit the system if input is 3
        elif user_choice == 3:
            print("THANKYOU FOR USING OUR SYSTEM. SEE YOU.")
            print("\n")
            exit()

        # Show invalid message if input is other than 1,2,3
        else:
            print("### INVALID OPTION! Please enter a valid option ###")
            print("\n")
            main()
    # Handle the error, if the integer input is non_numeric value
    except ValueError:
        print("\n")
        print("### ERROR! INVALID OPTION! Please enter a valid numerical input ###")
        print("\n")
        main()

