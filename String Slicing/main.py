# Ask the user for the username
username = input("Please enter your school username: ")

# Check if the username is valid (at least 6 characters and contains "_")
if len(username) < 6 or "_" not in username:
    print("Invalid username. The username must be at least 6 characters long and contain an underscore ('_').")
else:
    # Slice the username into parts
    year_group = username[:2]    # First two characters for year group
    initial = username[2:3]      # The third character for the initial
    lastname = username[3:-2]    # Everything between the initial and the role (excluding last two characters)
    role_code = username[-2:]    # Last two characters for role

    # Check if year group is a valid two-digit number
    if not year_group.isdigit() or int(year_group) < 0 or int(year_group) > 99:
        print("Invalid username. Year group should be a two-digit number.")
    # Check if role is valid
    elif role_code not in ['_S', '_T', '_A']:
        print("Invalid username. Role must be '_S' for student, '_T' for teacher, or '_A' for admin.")
    else:
        # Output based on role
        if role_code == "_S":
            print(f"Student Info: Year {year_group}, Initial: {initial}, Lastname: {lastname}")
            print("Role: Student")
        elif role_code == "_T":
            print(f"Teacher Info: Initial: {initial}, Lastname: {lastname}")
            print("Role: Teacher")
        elif role_code == "_A":
            print(f"Admin Info: Initial: {initial}, Lastname: {lastname}")
            print("Role: Admin")
