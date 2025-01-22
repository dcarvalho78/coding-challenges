#1 Counting in 5
for i in range(0, 501, 5):  
    print(i)
    
# Counting down
for i in range(100, -1, -1):  
    print(i)

#times tables

for i in range(1, 11):  
    result = i * 12  
    print(f"{i} x 12 = {result}")
    
#alphabet

for i in range(ord('A'), ord('Z') + 1): 
    print(chr(i), end=" ")
    
  # Iterative Sum  
    

number = int(input("Please enter a positive integer: "))


sum = 0


for i in range(1, number + 1): 
    sum = sum + i

print("Iterative Sum for", number, "=", sum)

#factorial

number = int(input("Please enter a positive integer: "))


factorial = 1


for i in range(1, number + 1): 
    factorial = factorial * i  # Multiply the current value of factorial by i

print(f"The factorial of {number} is {factorial}")