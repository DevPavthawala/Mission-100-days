# numbers = [1,2,3,4]
#
# for num in numbers:
#     if num == 3:
#         break
#     print(num)

numbers = [1,2,3,4]
index = 0

print(numbers[0])

while index < len(numbers):
    if numbers[index] == 2:
        # break
        continue

    print(numbers[index])
    index+=1