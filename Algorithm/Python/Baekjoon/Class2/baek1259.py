import sys

while True:
    number = str(sys.stdin.readline().strip())
    if number == "0":
        break
    else:
        if number == number[::-1]:
            print("yes")
        else:
            print("no")