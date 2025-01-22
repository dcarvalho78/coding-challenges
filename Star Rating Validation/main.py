rating = -1
while rating < 0 or rating > 5:
    rating = input("Please enter a star rating (0-5): ")
    
    if rating == '0' or rating == '1' or rating == '2' or rating == '3' or rating == '4' or rating == '5':
        rating = int(rating)
        print(f"Thank you! You rated: {rating} star(s).")
    else:
        print("Error: Invalid input. Please enter a number between 0 and 5.")
