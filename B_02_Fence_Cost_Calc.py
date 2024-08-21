# ask user for width and loop until they
# enter a number that is more than zero


def num_check(question):
    error = "Please enter an number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine starts here...

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("width: ")
    length = num_check("length: ")
    cost = num_check("cost: ")

    # Calculate perimeter and price for the fence
    area = width * length
    perimeter = 2 * (width + length)
    price = 2 * (width + length)

    # Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the fence calculator. ")
