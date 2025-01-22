print("Fizz-Buzz Game!")
print("Enter the number, 'Fizz', 'Buzz', or 'Fizz-Buzz' when appropriate.")
print("Game ends if you type the wrong answer. Let's begin!\n")

score = 0

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        correct = "Fizz-Buzz"
    elif num % 3 == 0:
        correct = "Fizz"
    elif num % 5 == 0:
        correct = "Buzz"
    else:
        correct = str(num)
    
    answer = input(f"{num}: ").strip()
    
    if answer == correct:
        score += 1
    else:
        print(f"Wrong! The correct answer was '{correct}'.")
        break

print(f"Game Over! Your score: {score}")
