# Copy here code of line function from previous exercise and use it in your solution
def line(count, string):
    if string != "":
        output = string[0] * count
        print(output[:count])
    else:
        print("*" * count)


def triangle(size, filler):
    # You should call function line here with proper parameters
    for _ in range(size):
        line(_ + 1, filler)


def rectangle(width, height, filler):
    for _ in range(height):
        line(width, filler)


def shape(width, triangle_filler, height, rectangle_filler):
    triangle(width, triangle_filler)
    rectangle(width, height, rectangle_filler)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
