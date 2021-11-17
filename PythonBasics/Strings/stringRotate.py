def rotate(input, x):
    Lfirst = input[0:x]
    Lsecond = input[x:]
    Rfirst = input[0:len(input)-x]
    Rsecond = input[len(input)-x:]

    print("Left Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))

# Driver program
if __name__ == "__main__":
    input = 'AkhilaShiva'
    x=2
    rotate(input,x)