# Write your solution here
my_list = []

while True:
    print(f"The list is now {my_list}")
    option = input("a(d)d, (r)emove or e(x)it: ")

    if option == "d":
        my_list.append(len(my_list) + 1)
    elif option == "r":
        my_list.pop()
    elif option == "x":
        print("Bye!")
        break
