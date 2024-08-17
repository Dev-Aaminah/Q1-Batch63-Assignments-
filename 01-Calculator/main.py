print("""
       _____________________
      |  _________________  |
      | |              0. | |
      | |_________________| |
      |  ___ ___ ___   ___  |
      | | 7 | 8 | 9 | | + | |
      | |___|___|___| |___| |
      | | 4 | 5 | 6 | | - | |
      | |___|___|___| |___| |
      | | 1 | 2 | 3 | | x | |
      | |___|___|___| |___| |
      | | . | 0 | = | | / | |
      | |___|___|___| |___| |
      |_____________________|
      
                   __  __       ___       _  _               _    _   
          / \     |  \/  |     |_ _|     | \| |     / \     | |__| |  
         / _ \    | |\/| |      | |      | .` |    / _ \    | |__| |  
        /_/ \_\   |_|  |_|     |___|     |_|\_|   /_/ \_\   |_|  |_|  

      """)
input1_from_user:int = int(input("Enter first number : "))
input2_from_user:int = int(input("Enter second number : "))

# arithematic operators (+,-,*,/,%,**,//)
sum:int = input1_from_user+input2_from_user
difference:int = input1_from_user-input2_from_user
product:int = input1_from_user*input2_from_user
quotient:int = input1_from_user/input2_from_user
remainder:int = input1_from_user%input2_from_user
power:int = input1_from_user**input2_from_user
floor_division:int = input1_from_user//input2_from_user


print(f"Sum of {input1_from_user} and {input2_from_user} is {sum}")
print(f"Difference of {input1_from_user} and {input2_from_user} is {difference}")
print(f"Product of {input1_from_user} and {input2_from_user} is {product}")
print(f"Quotient of {input1_from_user} and {input2_from_user} is {quotient}")
print(f"Remainder of {input1_from_user} and {input2_from_user} is {remainder}")
print(f"Power of {input1_from_user} and {input2_from_user} is {power}")
print(f"Floor division of {input1_from_user} and {input2_from_user} is {floor_division}")