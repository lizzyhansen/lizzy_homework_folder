#3.4

for i in range(2):
    for i in range (0, 7, 1):
        print('@', end='')
    print()


#3.9 

number = int(input ("please enter a seven to ten digit number:"))

original_number = number

if number <= 0:
    print("Please enter a positive number")
else:
    original_number = number

divisor = 1
while number // divisor >= 10:
    divisor *= 10

print(f"the digits of {original_number} from left to right are:")

    
while divisor >=1: 
    digit = number // divisor 

    print(digit)

    number = number % divisor 

    divisor = divisor // 10

# i don't know where this if statement should go 
#     if number < 7 or number >10:
#         print("please enter a number between seven and ten digits:")
#     else:
#         digits = []


# 3.11

# set up sentinal 
total_miles = 0
total_gallons = 0


while True:
    miles_driven = float(input("enter miles driven(type -1 to quit)"))

    if miles_driven == -1:
        break
    gallons_used = float(input("enter gallons used for this tank:"))

    single_mpg = miles_driven/gallons_used
    print(f"mpg for this tank:{single_mpg:.2f}")

    total_miles += miles_driven
    total_gallons += gallons_used 

if total_gallons > 0: 
    combined_mpg = total_miles / total_gallons
    print("Combined miles per gallon", combined_mpg)
else:
    print("no valid data entered")



#  3.12 
number = int(input ("enter a five digit number:"))
first_num = number // 10000
last_num = number % 10
second_num = (number - first_num * 10000) // 1000
fourth_num = ((number % 1000) % 100) // 10

if first_num == last_num:
    if second_num == fourth_num:
        print("palindrome!!!!")
else:
    print ("not palindrome!")



#3.14
# numerator is always 4, denominator is always odd, starts at 1 
numerator = 4 
denominator = 1
total = 0

#loop 
for i in range(3000 +1):
    if i % 2 == 0:
        total -= numerator/denominator
    elif i % 2 != 0:
        total += numerator/denominator 
   
    denominator += 2 
    print("i:", i, "total:", total)

print("total:", total)
