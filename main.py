from helper import doBreakdown

# calc = 24 * 60 * 60
# years = 'old'
#
# myInput = input("Enter\n")
#
# if not myInput.isdigit():
#     print("no")
# try:
#     int(myInput)
# except ValueError:
#     "not possible"
#
# def days_unit(num):
#     return num * 2


# days_unit(10)
# print(days_unit(myInput))
# arr = [1, 2, "ab", 3, 3]

# arr.pop(3)
# print(arr[7])

# try:
#     print(arr[7])
# except IndexError:
#     print("nope")
#
#
# for i in set(arr):
#     print(f"{i}")
# print(len(arr))


myEntry = ""


while myEntry != "exit":
    myEntry = input("Please enter in format \"xx:yy\"\n")
    if not myEntry.__contains__(":"):
        print("incorrect input")
    arr = ""
    try:
        arr = myEntry.split(":")
    except ValueError:
        "INVALID FORMAT"
    if not arr[0].isdigit():
        print(f"{arr[0]} is not a number")

    doBreakdown(arr)
