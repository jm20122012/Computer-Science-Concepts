# This program reads a user input of space separated integers, assigns them to an 
# array, then performs the selection sort algorithm for descending order.

user_input = input() 
# print(f"User input: {user_input} - Type: {type(user_input)}")
numbers = [int(i) for i in user_input.split(' ')]
# print(numbers)


# print("Starting sort")
for i in range(len(numbers) - 1):
    min = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[min]:
            min = j
    temp = numbers[i]
    numbers[i] = numbers[min]
    numbers[min] = temp
    print(numbers)