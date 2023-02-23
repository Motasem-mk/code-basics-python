expenses_serger = [30, 45, 70, 90]
expenses_sunder = [30, 45, 70, 90]

total = 0

for expense in expenses_serger : 
    total+=expense 

print(f"total = {total}")

## same for the seconf person 

for expense in expenses_sunder: 
    total+=expense 

print(f"total = {total}")

## instead of repeating i can dreate a function 

def total_expenses (*expenses):
    '''
    This function to calculate the total 
    the param is expenses 
    return is the total
    '''
    total = 0
    for expense in expenses :
        total+=expense
    return total

print("Total expenses of serger is :",total_expenses(*expenses_serger))

## function to calculate the volume of the cylinder

def find_cylinder_volume (radius,height):
   print("Radius",radius)
   print("Height" , height)
   volume =3.14 * (height**2) * height
   return volume

print(f"Volume of the cylinder = {int(find_cylinder_volume(radius= 5, height= 10))} m3")

# (radius= 5, hight= 10) => called positional arguments

# exercices

# find the prime and odd number

# number = int(input ("Enter your number"))

# for n in range(2,number):
#      if number % n == 0 :
#          print("this is n0t a prime number ")
#          break
# else :
#     print("this is a prime numebr and odd ")

# num = int(input("Enter you number : "))
# if num % 2 ==0 :
#     for i in range(num):
#         for j in range (num-i):
#           print("*",end=" ")
#         print()  ### must be here to print new line after the fininsheing of the nested loop 

# else :
#     for i in range(num):
#         for j in range (i+1):
#           print("*",end=" ")
#         print() 

 

st = "Hi My Name is Motasem"
print(st)
st= (st).split()
print(st)
print(type(st))
n=len(st)
print(n)

r=n-1 # because it starts from 0 to n-1 .if n =5 then the indexes is 0,1,2,3,4 
      # print(st[(5-1=4)-0] st[4]) 
for i in range(n):
  print(st[r-i],end=" ")

# we gonna make it as a function 

def reverse_string(string):
    #string = input("Enter you sentence : ").strip().capitalize()
    string = string.split()
    l=len(string)
    n=l-1
    for i in range(l):
        print(f"{string[n-i].capitalize()}",end=" ")
string = input("\nEnter you sentence : ").strip().capitalize()
reverse_string(string)

# def pay_bill(expenses,percent_commission=0.098,special_offer_amount=None):

#     percent_commission = float(percent_commission)
#     Total_exp = 0
#     # expenses = int(expenses)
#     if len(expenses) == 1 :
#         Total_exp = expenses
#     else:   
     
#        for expense in expenses:
#           Total_exp +=expense
#     if Total_exp > special_offer_amount:
#         special_offer_amount = int(special_offer_amount)
#         extra_commission =  percent_commission + 0.12
#         total= Total_exp*extra_commission - Total_exp 
#     else:
#         total_discount=(Total_exp - percent_commission*Total_exp)
#         total= Total_exp -total_discount

#     return total
# expenses=[100, 30, 200]

# print(f"\nYour Total after commission : ${pay_bill(12, special_offer_amount=1000)}")


def pay_bill(expenses, percent_commission=0.098, offer_amount=None):
    
    # calculating the total bill amount
    total_bill_amount = 0
    for amount in  expenses:
        total_bill_amount += amount

    # calculate extra commision percentage
    extra_commission = 0
    if offer_amount:
        if total_bill_amount >= offer_amount:
            extra_commission = 0.012
            print(f"Congratulations! You earned 1.2% extra commission.")

    # Calculate final payable amount
    commission_amount = total_bill_amount * (percent_commission + extra_commission)
    final_amount = total_bill_amount - commission_amount
    return final_amount

print(f"\n{pay_bill(expenses=[100,200,12,23])}")
print(f"{pay_bill(100)}") # must be more than one number 