number = input("Enter a number: ")

even_position_sum = 0
odd_position_sum = 0


for index, digit in enumerate(number, start=1):
    if index % 2 == 0:
        even_position_sum += int(digit)
    else:
        odd_position_sum += int(digit)


print("Sum of digits at odd positions:", odd_position_sum)
print("Sum of digits at even positions:", even_position_sum)
