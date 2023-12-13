# Imagine a question: Do you like ice cream?
user_response = input("Do you like ice cream? (yes/no): ")

# Use the bool() function to convert the user's response into a True or False value
liked_ice_cream = bool(user_response.lower() == 'yes')

# Now, let's see what the Bool Machine says!
if liked_ice_cream:
    print("Yay! You like ice cream! 🍦")
else:
    print("Oh no! You don't like ice cream? That's okay! 🙁")
