# Write your solution here
def greatest_number(num1, num2, num3):
    def greatest(a, b):
        if a > b:
            return a
        else:
            return b

    return greatest(greatest(num1, num2), num3)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
