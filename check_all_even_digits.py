number = input("Enter a number: ")

all_even = True

for digit in number:
    if int(digit) % 2 != 0:
        all_even = False
        break

if all_even:
    print("All digits are even.")
else:
    print("Not all digits are even.")