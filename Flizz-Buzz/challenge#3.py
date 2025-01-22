print("Fizz-Buzz Game with Lives!")
print("You have 3 lives. Each mistake costs 10 points. Let's begin!\n")

score = 0
lives = 3

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
        print("Correct!")
    else:
        lives -= 1
        score -= 10
        print(f"Wrong! The correct answer was '{correct}'.")
        print(f"Lives left: {lives}")
        if lives == 0:
            break

print(f"\nGame Over! Final Score: {score}")
