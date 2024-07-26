from datetime import datetime
#This function will generate the bill for sale purpose
def sale_bill_print_and_generation(customer_name, customer_number, sold_laptops):
    # Shipping charge amount
    shipping_charge = 10

    # Ask wwhether to include shipping in the bill
    while True:
        shipping = input("Do you want to include shipping in the bill? (Shipping Charge: 10$)? (yes/no): ").lower()
        print("\n")

        # If shippin is included
        if shipping == "yes":
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("|                                                      JB ELECTRONICS, MAHARJGUNJ, KATHMANDU                                                       |")
            print("|                                                      Phone No: +977 9812345678, 01-1234567                                                       |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Name of the customer         :  ",customer_name)
            print("| Phone number of the customer :  ",customer_number)
            print("| Date of purchase             :  ",datetime.now())
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            # Add specified character spaces between each strings using format
            print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            
            total_price = 0
            # iterate over the sold_laptops list and Assign each index with the varibale name
            for eachsoldlaptops in sold_laptops:
                laptop_name = eachsoldlaptops[1]
                laptop_brand = eachsoldlaptops[2]
                laptop_price = eachsoldlaptops[3]
                laptop_quantity = eachsoldlaptops[4]
                laptop_generation = eachsoldlaptops[5]
                laptop_graphics = eachsoldlaptops[6]

                #Calculate total laptop price
                total_laptop_price = int(laptop_price)* int(laptop_quantity)
                # Add specified character spaces between each variables using format
                print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format(laptop_name, laptop_brand, laptop_price, laptop_quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            print("|")
            print("|")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Total Price                  :  ",total_price,"$")
            print("| 13% VAT                      :  ",vat,"$")
            print("| Shipping charge              :  ",shipping_charge,"$")
            print("| Grand Total                  :  ",grand_total+shipping_charge,"$")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")

            # Creates a new txt file and write the bill in it
            date_and_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file = open(f"{customer_number}_{date_and_time}.txt","w")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("|                                                      JB ELECTRONICS, MAHARJGUNJ, KATHMANDU                                                       |\n")
            file.write("|                                                      Phone No: +977 9812345678, 01-1234567                                                       |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Name of the customer         :  "+str(customer_name)+"\n")
            file.write("| Phone number of the customer :  "+str(customer_number)+"\n")
            file.write("| Date of purchase             :  "+str(datetime.now())+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            
            total_price = 0
            for eachsoldlaptops in sold_laptops:
                laptop_name = eachsoldlaptops[1]
                laptop_brand = eachsoldlaptops[2]
                laptop_price = eachsoldlaptops[3]
                laptop_quantity = eachsoldlaptops[4]
                laptop_generation = eachsoldlaptops[5]
                laptop_graphics = eachsoldlaptops[6]

                total_laptop_price = int(laptop_price)* int(laptop_quantity)
                file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format(laptop_name, laptop_brand, laptop_price, laptop_quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            file.write("|\n")
            file.write("|\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Total Price                  :  "+str(total_price)+" $"+"\n")
            file.write("| 13% VAT                      :  "+str(vat)+" $"+"\n")
            file.write("| Shipping charge              :  "+str(shipping_charge)+" $"+"\n")
            file.write("| Grand Total                  :  "+str(int(grand_total + shipping_charge))+" $"+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.close()
            break
        
        # if shipping is not included
        elif shipping == "no":
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("|                                                      JB ELECTRONICS, MAHARJGUNJ, KATHMANDU                                                       |")
            print("|                                                      Phone No: +977 9812345678, 01-1234567                                                       |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Name of the customer         :  ",customer_name)
            print("| Phone number of the customer :  ",customer_number)
            print("| Date of purchase             :  ",datetime.now())
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            
            total_price = 0
            for eachsoldlaptops in sold_laptops:
                laptop_name = eachsoldlaptops[1]
                laptop_brand = eachsoldlaptops[2]
                laptop_price = eachsoldlaptops[3]
                laptop_quantity = eachsoldlaptops[4]
                laptop_generation = eachsoldlaptops[5]
                laptop_graphics = eachsoldlaptops[6]

                total_laptop_price = int(laptop_price)* int(laptop_quantity)
                print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format(laptop_name, laptop_brand, laptop_price, laptop_quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            print("|")
            print("|")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Total Price                  :  ",total_price,"$")
            print("| 13% VAT                      :  ",vat,"$")
            print("| Grand Total                  :  ",grand_total,"$")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")

            date_and_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file = open(f"{customer_number}_{date_and_time}.txt","w")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("|                                                      JB ELECTRONICS, MAHARJGUNJ, KATHMANDU                                                       |\n")
            file.write("|                                                      Phone No: +977 9812345678, 01-1234567                                                       |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Name of the customer         :  "+str(customer_name)+"\n")
            file.write("| Phone number of the customer :  "+str(customer_number)+"\n")
            file.write("| Date of purchase             :  "+str(datetime.now())+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            
            total_price = 0
            for eachsoldlaptops in sold_laptops:
                laptop_name = eachsoldlaptops[1]
                laptop_brand = eachsoldlaptops[2]
                laptop_price = eachsoldlaptops[3]
                laptop_quantity = eachsoldlaptops[4]
                laptop_generation = eachsoldlaptops[5]
                laptop_graphics = eachsoldlaptops[6]

                total_laptop_price = int(laptop_price)* int(laptop_quantity)
                file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format(laptop_name, laptop_brand, laptop_price, laptop_quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            file.write("|\n")
            file.write("|\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Total Price                  :  "+str(total_price)+" $"+"\n")
            file.write("| 13% VAT                      :  "+str(vat)+" $"+"\n")
            file.write("| Grand Total                  :  "+str(int(grand_total))+" $"+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.close()            
            break
        
        else:
            print("### INVALID INPUT! Please enter YES or NO.")
            print("\n")


# This function will print the bill for purchase process and is similar to the sale bill generation
def purchase_bill_print_and_generation(purchased_laptops):
    
    shipping = 5                           
    name_of_the_distributor = "All in one electronics Manufacturer and Wholesaler"
    name_of_the_company = "JB Electronics"
    address = "Maharajgunj, Kathmandu"
    contact_number = "+977 9812345678 / 01-1234567"

    while True:
        shipping_ = input("Do you want to add shipping for your purchase (Shipping Charge: 5$)? (yes/no): ").lower()
        if shipping_ == "yes":
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("|                                                 All In One Electronics Manufacturer and Wholesaler                                               |")
            print("|                                                      Phone No: +977 9876543210, 01-6543210                                                       |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Name of the Distributor       :  ",name_of_the_distributor)
            print("| Name of the Company           :  ",name_of_the_company)
            print("| Address                       :  ",address)
            print("| Contact number of the company :  ",contact_number)
            print("| Date of purchase              :  ",datetime.now())
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            
            total_price = 0
            for eachpurhcasedlaptops in purchased_laptops:
                laptop_name = eachpurhcasedlaptops[0]
                laptop_brand = eachpurhcasedlaptops[1]
                laptop_price = eachpurhcasedlaptops[2]
                quantity = eachpurhcasedlaptops[3]
                laptop_generation = eachpurhcasedlaptops[4]
                laptop_graphics = eachpurhcasedlaptops[5]
                
                total_laptop_price = laptop_price*quantity
                print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format(laptop_name, laptop_brand, laptop_price, quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            print("|")
            print("|")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Total Price                   :  ",total_price,"$")
            print("| 13% VAT                       :  ",vat,"$")
            print("| Shipping charge               :  ",shipping,"$")
            print("| Grand Total                   :  ",grand_total + shipping,"$")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")

            date_and_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file = open(f"{name_of_the_company}_{date_and_time}.txt","w")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("|                                                 All In One Electronics Manufacturer and Wholesaler                                               |\n")
            file.write("|                                                      Phone No: +977 9876543210, 01-6543210                                                       |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Name of the Distributor       :  "+name_of_the_distributor+"\n")
            file.write("| Name of the company           :  "+name_of_the_company+"\n")
            file.write("| Address                       :  "+address+"\n")
            file.write("| Contact number of the company :  "+contact_number+"\n")
            file.write("| Date of purchase              :  "+str(datetime.now())+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            
            total_price = 0
            for eachpurhcasedlaptops in purchased_laptops:
                laptop_name = eachpurhcasedlaptops[0]
                laptop_brand = eachpurhcasedlaptops[1]
                laptop_price = eachpurhcasedlaptops[2]
                quantity = eachpurhcasedlaptops[3]
                laptop_generation = eachpurhcasedlaptops[4]
                laptop_graphics = eachpurhcasedlaptops[5]
                
                total_laptop_price = laptop_price*quantity
                file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format(laptop_name, laptop_brand, laptop_price, quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            file.write("|\n")
            file.write("|\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Total Price                   :  "+str(total_price)+" $"+"\n")
            file.write("| 13% VAT                       :  "+str(vat)+" $"+"\n")
            file.write("| Shipping charge               :  "+str(shipping)+" $"+"\n")
            file.write("| Grand Total                   :  "+str(int(grand_total+shipping))+" $"+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.close()
            break

        elif shipping_ == "no":
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("|                                                 All In One Electronics Manufacturer and Wholesaler                                               |")
            print("|                                                      Phone No: +977 9876543210, 01-6543210                                                       |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Name of the Distributor       :  ",name_of_the_distributor)
            print("| Name of the Company           :  ",name_of_the_company)
            print("| Address                       :  ",address)
            print("| Contact number of the company :  ",contact_number)
            print("| Date of purchase              :  ",datetime.now())
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            
            total_price = 0
            for eachpurhcasedlaptops in purchased_laptops:
                laptop_name = eachpurhcasedlaptops[0]
                laptop_brand = eachpurhcasedlaptops[1]
                laptop_price = eachpurhcasedlaptops[2]
                quantity = eachpurhcasedlaptops[3]
                laptop_generation = eachpurhcasedlaptops[4]
                laptop_graphics = eachpurhcasedlaptops[5]
                
                total_laptop_price = laptop_price*quantity
                print("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |".format(laptop_name, laptop_brand, laptop_price, quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            print("|")
            print("|")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("| Total Price                   :  ",total_price,"$")
            print("| 13% VAT                       :  ",vat,"$")
            print("| Grand Total                   :  ",grand_total,"$")
            print("|--------------------------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")

            date_and_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file = open(f"{name_of_the_company}_{date_and_time}.txt","w")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("|                                                 All In One Electronics Manufacturer and Wholesaler                                               |\n")
            file.write("|                                                      Phone No: +977 9876543210, 01-6543210                                                       |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Thankyou for purchasing the laptop. Visit Again!                                                                                                 |\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Name of the Distributor       :  "+name_of_the_distributor+"\n")
            file.write("| Name of the company           :  "+name_of_the_company+"\n")
            file.write("| Address                       :  "+address+"\n")
            file.write("| Contact number of the company :  "+contact_number+"\n")
            file.write("| Date of purchase              :  "+str(datetime.now())+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format("Laptop Name", "Brand", "Price", "Quantity", "Generation", "Graphics", "Total Price"))
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            
            total_price = 0
            for eachpurhcasedlaptops in purchased_laptops:
                laptop_name = eachpurhcasedlaptops[0]
                laptop_brand = eachpurhcasedlaptops[1]
                laptop_price = eachpurhcasedlaptops[2]
                quantity = eachpurhcasedlaptops[3]
                laptop_generation = eachpurhcasedlaptops[4]
                laptop_graphics = eachpurhcasedlaptops[5]
                
                total_laptop_price = laptop_price*quantity
                file.write("| {:<22} {:<18} {:<17} {:<20} {:<22} {:<20} {:<19} |\n".format(laptop_name, laptop_brand, laptop_price, quantity, laptop_generation, laptop_graphics, total_laptop_price))
                total_price += total_laptop_price
                vat = 0.13*total_price
                grand_total = total_price + vat
            file.write("|\n")
            file.write("|\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("| Total Price                   :  "+str(total_price)+" $"+"\n")
            file.write("| 13% VAT                       :  "+str(vat)+" $"+"\n")
            file.write("| Grand Total                   :  "+str(int(grand_total))+" $"+"\n")
            file.write("|--------------------------------------------------------------------------------------------------------------------------------------------------|\n")
            file.write("\n")
            file.close()
            break

        else:
            print("### INVALID INPUT! Please enter YES or NO")
