'''
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
'''

from itertools import cycle

n = input("enter number:")
l = len(n)
half = int(l/2)
string = cycle(n)
sum = 0
new_list = []
for i in string:
    if len(new_list) < int(l+half):
        new_list.append(i)
    else:
        break
for i in range(len(new_list)):
    if i < len(new_list)-half:
        if new_list[i] == new_list[i+half]:
            sum = sum + int(new_list[i])
print(sum)
