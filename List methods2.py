# Declaring list from 1 to 20

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# Append operation (adds element at end)

lst.append(21)
print("\nAfter appending 21:")
print(lst)

# Insert operation (adds element at specific index)

lst.insert(0,0)
print("\nAfter inserting 0 at beginning:")
print(lst)

# Remove operation (removes first occurrence)

lst.remove(10)
print("\nAfter removing 10:")
print(lst)

# Sorting 

l = [7,8,1,3,2,4,6,5,10,12,9,11,14,16,13,15,17,19,16,20]
l.sort()
print("\nAfter sorting:")
print(l)

# Function: Sort list ascending and descending

l.sort(reverse=True)
print("\nAfter sorting in Descending order:")
print(l)


l.sort(reverse=False)
print("\nAfter sorting in Ascending order:")
print(l)

# List comprehension (squares of original list)

squares = [num ** 2 for num in lst]

print("\nSquares of numbers:")
print(squares)



def remove_duplicates(lst):
    
    # This function removes duplicate elements from a list
    # while preserving the original order of elements.
    
    unique_list = []  # Stores final result without duplicates

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


duplicate_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7]
print("\nList with duplicates:")
print(duplicate_list)

# Function: Remove duplicates while preserving order

list = remove_duplicates(duplicate_list)
print("\nAfter removing duplicates:")
print(list)