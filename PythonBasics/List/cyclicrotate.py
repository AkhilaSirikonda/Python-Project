# Program to cyclically rotate an array by one
def cyclicRotate(input):
    print([input[-1]] + input[0:-1])

if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    cyclicRotate(input)