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


# Main routine goes here
for item in range(0, 2):
    width = num_check("width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("height: ")
    print(height)
