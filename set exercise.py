userInput = input("Enter Ints separated by commas: ")

x = userInput.split(",")

lst = []

for i in x:
    l = int(i)
    lst.append(l)

my_set = set(lst)

half_len = len(my_set) // 2
set_1 = set(list(my_set)[:half_len])
set_2 = set(list(my_set)[half_len:])

union_set = set_1.union(set_2)
intersection_set = set_1.intersection(set_2)
difference_set = set_1.difference(set_2)

print("Union set: ", union_set)
print("Intersection set: ", intersection_set)
print("Difference set: ", difference_set)





