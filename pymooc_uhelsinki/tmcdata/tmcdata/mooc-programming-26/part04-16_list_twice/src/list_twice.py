# Write your solution here
list = []
list_ordered = []

while True:
    num = int(input("New item: "))
    if num == 0:
        print("Bye!")
        break
    list.append(num)
    print(f"The list now: {list}")
    list_ordered = sorted(list)
    print(f"The list in order: {list_ordered}")
