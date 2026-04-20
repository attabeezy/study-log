# Write your solution here


def spruce(n):
    print("a spruce!")
    for i in range(n):
        spaces = n - 1 - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

    print(" " * (n - 1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
