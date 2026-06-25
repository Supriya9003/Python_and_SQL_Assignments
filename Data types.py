#1. create data types using type() function
integer_var = 100
float_var = 99.99
string_var = "Hello Python"
list_var = [10, 20, 30, 40]
dictionary_var = {
    "name": "priya",
    "age": 22
}

print("Integer:", integer_var, "Type:", type(integer_var))
print("Float:", float_var, "Type:", type(float_var))
print("String:", string_var, "Type:", type(string_var))
print("List:", list_var, "Type:", type(list_var))
print("Dictionary:", dictionary_var, "Type:", type(dictionary_var))

#2.calculates the mean, median, and standard deviation, and returns these values as a dictionary.
import statistics

def calculate_statistics(numbers):
    result = {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "standard_deviation": statistics.stdev(numbers)
    }
    return result

data = [10, 20, 30, 40, 50]

stats = calculate_statistics(data)

print(stats)


#3. converts it into a list of words, and then uses a dictionary to count the occurrence of each word.

text = input("\nEnter a sentence: ")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Counts:")
print(word_count)


#4. Implement a class that represents a person with attributes like name (string), age (integer), and address (dictionary).
#  Create instances of this class and demonstrate how to access and modify their attributes.


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

person1 = Person(
    "Supriya",
    25,
    {"city": "Hyderabad", "state": "Telangana"}
)

person2 = Person(
    "Geethu",
    30,
    {"city": "Vijayawada", "state": "Andhra Pradesh"}
)


print("Person 1 Name:", person1.name)
print("Person 1 Age:", person1.age)
print("Person 1 Address:", person1.address)


person1.age = 26
person1.address["city"] = "Bangalore"

print("\nAfter Modification:")
print("Name:", person1.name)
print("Age:", person1.age)
print("Address:", person1.address)


print("\nPerson 2 Details:")
print("Name:", person2.name)
print("Age:", person2.age)
print("Address:", person2.address)
