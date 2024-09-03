##Input we need from user  
# Total rent 
# Total food order for snacking 
# Electricity units spend
# Charge per unit
# Persons  living in roo/flat


##Output
#total amnt you have to pay is 

rent = int(input("Enter your hostel/Flat Rent = \n"))

food = int(input("Enter the amount of food ordered = \n"))

electricity_spend = int(input("Enter the total of electricity spend = \n"))

charge_per_Unit = int(input("Enter the charge per unit = \n"))

persons = int(input("Enter the Persons living in room/flat = \n"))


total_bill = electricity_spend * charge_per_Unit

output =   (food + rent + total_bill) / persons

print("Each persons will pay = ",output)