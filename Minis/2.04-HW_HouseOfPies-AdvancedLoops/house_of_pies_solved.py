# List of Pies
pies = ["Pecan", "Apple Crisp","Bean", "Bannoffee","Black Bun", "Blueberry", "Buko","Burek", "Tamale","Steak"]

greeting = ("Welcome to the House of Pies! Here are our pies:  ---------------------------------------------------------------------   \n(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak")

order_count = 0

new_order = "Y"

while "Y":
    
    order_form = int(input(f' {greeting} \n Enter Pie No. to place order. '))
    
    #start the count
    if order_form in range(1,11):
        print( f"\n Great! We'll have that {pies[order_form-1]} right out for you.")
        order_count += 1        
              
    elif order_form == 0 or order_form > 10:
        print("\nTo order, enter the correct pie number.") 
    
    new_order = input("Do you want to order another pie? Y/N ").upper()
    
    if new_order == "N":
        print(f"\nThe total number of pies ordered is {order_count} .")
        break