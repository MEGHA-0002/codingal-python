#conditional statements
num = 3
if num > 0:
    print(num, "is a positive number.")


num = -1
if num > 0:
    print(num, "is a positive number.")


    #profit loss
    actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))
 
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!")


    #greater or smaller
    i = int(input("enter a number : "))
if (i < 15):
    print ("i is smaller than 15")
    print ("i'm in if Block")
else:
    print ("i is greater than 15")
    print ("i'm in else Block")
print ("i'm not in if and not in else Block")

#odd or even
number = int(input("Enter Number to check"))
print("Number to be checked :", number)

if number%2==0 :
  print("This is an even number")

else:
  print("This is an odd number")
