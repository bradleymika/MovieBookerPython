# Bradley Mika, 2/18/24, Class IS 601


# Movie information stored in a list of dictionaries
movies = [
    {"title": "Avengers: Endgame", "genre": "Action", "price": 20, "available_tickets": 50},
    {"title": "The Lion King", "genre": "Animation", "price": 15, "available_tickets": 30},
    {"title": "John Wick 3", "genre": "Action", "price": 18, "available_tickets": 25},
    {"title": "Kung Fu Panda 4" , "genre": "Action", "price": 15, "available_tickets": 10},
    {"title": "Indiana Jones: The Dial of Destiny" , "genre": "Action", "price":20, "available_tickets": 5}
]

#Coupons
coupons = { "SAVE5": 0.05, "SAVE10": 0.10, "SAVE15": 0.15}

# Welcome message and get user name
name = input("Hello there and Welcome to Your Ticket Window! What is your name? ") + " " + input("What is your last name? ")
print(f"Hey there, {name}! Let's find some movies for you to watch!")

# Display movie options
print("\nAvailable movies:")
for i, movie in enumerate(movies):
    print(f"{i+1}. {movie['title']} ({movie['genre']}) - ${movie['price']}")

# User can choose number for faster checkout
while True:
    try:
        movie_number = int(input("\nEnter the number of the movie you want to watch: "))
        if 1 <= movie_number <= len(movies):
            chosen_movie = movies[movie_number - 1]  # Adjust for zero-based indexing
            break  # Exit the loop if a valid number is chosen
        else:
            print("Please enter a valid movie number from the list.")
    except ValueError:
        print(f"Sorry, '{chosen_movie}' is not available. Please try again.")

# Apply Coupon Code
coupon_code = input("Enter a coupon code if you have one (or press enter to skip): ").upper()
discount = coupons.get(coupon_code, 0)  # Get discount percentage, default to 0 if coupon code is not found

# Display movie details and get number of tickets
print(f"\nYou chose '{chosen_movie['title']}' ({chosen_movie['genre']}) - ${chosen_movie['price']}")
num_tickets = int(input("How many tickets would you like to purchase? "))

# Check ticket availability and calculate total price
if num_tickets <= chosen_movie["available_tickets"]:
    chosen_movie["available_tickets"] -= num_tickets  # Update available tickets
    total_price = num_tickets * chosen_movie["price"]
    discount_amount = total_price * discount
    final_price = total_price - discount_amount
    print(f"\nCongratulations! You purchased {num_tickets} tickets for '{chosen_movie['title']}' at a total of ${final_price}.")
else:
    print(f"Sorry, only {chosen_movie['available_tickets']} tickets are available for '{chosen_movie['title']}'.")

# Thank you message
print(f"\nThank you for using Ticket Window, {name}. Please come Again!")
