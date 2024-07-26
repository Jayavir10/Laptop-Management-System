# This function will read the laptop from laptops.txt file and store it in a list and returns the list
def read_laptops():
    # Open the file in read mode
    file = open("laptops.txt","r")
    laptops_list = []
    serial_num = 1
    for line in file:
        laptop_split = line.strip().split(",")
        laptops_list.append([serial_num] + laptop_split)
        # Increment the value by 1
        serial_num += 1
    # Close the file
    file.close()
    return laptops_list

# This function will display the available laptops in tabular format
def laptop_table():
    print("These are the number of laptops and its information that are available right now:")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("ID\tLaptop Name\t\tCompany Name\t\tPrice\t\tQuantity\tGeneration\t\tGraphics")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    
    # Open the file laptops.txt in read mode
    file = open("laptops.txt","r")
    a = 1
    for line in file:
        laptop_name, company_name, price, quantity, generation, graphics = line.strip().split(",")
        # Add specified characters spaces in between each of the variable 
        print("{:<6}\t{:<16}\t{:<16}\t{:<8}\t{:<8}\t{:<16}\t{}".format(str(a), laptop_name, company_name, price+" $", quantity, generation, graphics))
        # Increment the value of a by 1 after each ine is processed
        a += 1
    # Close the file
    file.close()
    print("\n")
