while True:
    try:
        userInput = input("Which numbers would you like to round? Please separate by commas: ")
        lst = [float(d) for d in userInput.split(",")]
        break
    except ValueError:
        print("Please enter valid float numbers separated by commas!")

rounded_list = []
for num in lst:
    rounded_num = round(num)
    rounded_list.append(rounded_num)

print("The rounded numbers are:", rounded_list)