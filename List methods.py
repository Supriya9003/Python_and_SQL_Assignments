# Function to remove duplicate elements
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# Function to find the index of the maximum value
def find_max(lst):
    max_value = lst[0]
    max_index = 0

    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i

    return max_index


# Function to filter even numbers
def filter_even(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


# Function to calculate the sum of all elements
def sum_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total


# Function to double the values using list comprehension
def double_values(lst):
    return [num * 2 for num in lst]



print("===== Testing remove_duplicates() =====")
list1 = [1, 2, 2, 3, 4, 4, 5, 6]
print("Original List:", list1)
print("After Removing Duplicates:", remove_duplicates(list1))

print("\n===== Testing find_max() =====")
list2 = [15, 8, 22, 5, 19]
print("List:", list2)
print("Maximum Value:", max(list2))
print("Index of Maximum Value:", find_max(list2))

print("\n===== Testing filter_even() =====")
list3 = [11, 12, 13, 14, 15, 16]
print("Original List:", list3)
print("Even Numbers:", filter_even(list3))

print("\n===== Testing sum_elements() =====")
list4 = [10, 20, 30, 40, 50]
print("List:", list4)
print("Sum of Elements:", sum_elements(list4))

print("\n===== Testing double_values() =====")
list5 = [2, 4, 6, 8]
print("Original List:", list5)
print("Doubled Values:", double_values(list5))