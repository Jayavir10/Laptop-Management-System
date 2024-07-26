from Operations import purchase_laptop, sale_laptop

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

# Call main function
main()