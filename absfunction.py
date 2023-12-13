# Get a number from the user
user_input = input("Enter a number: ")

# Convert the user input to a float (in case they enter a decimal number)
try:
    number = float(user_input)

    # Use the abs() function to get the absolute value
    absolute_value = abs(number)

    # Display the result
    print(f"The absolute value of {number} is {absolute_value}")

except ValueError:
    print("Please enter a valid number.")
