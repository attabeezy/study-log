# Copy here code of line function from previous exercise
def line(count, string):
    if string != "":
        output = string[0] * count
        print(output[:count])
    else:
        print("*" * count)


def triangle(size):
    # You should call function line here with proper parameters
    for _ in range(size):
        line(_ + 1, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
