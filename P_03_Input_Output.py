# ask the user for their name
username = input("What is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve and square the user's favourite number
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

# Greet the user

print(f"\nHi{username}, you favourite number is {fav_num}")

# Output the results of doubling, halfing and
# squaring their favourite integer
print(f"double {fav_num} is {double}.")
print(f"half {fav_num} is {half}")
print(f"{fav_num} squared is {square}")
print()
print("Have a nice day.")
