#tuple

marukos_tuple = (3,5,7)

print(len(marukos_tuple))

x = marukos_tuple[1]

print(x)                    #print the position of the second elemnt of the tupple (comp. start at 0)


#YOU CANNOT CHANGE THE OBJECTS INSIDE A TUPLE!!!!!!


tuple_2 = ('apple',"banna","orange")

merged_tuples = marukos_tuple + tuple_2    #merged tuplle

print(merged_tuples.count(5))               #count how often elemnt 5 appears in tupples

index = merged_tuples.index("orange")       #search the "tupple position of "orange"

print(index)
