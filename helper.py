def convertToSeconds(num, conversion):
    if conversion == "hours":
        return num * 60 * 60
    elif conversion == "min":
        return num * 60
    else:
        return f"cannot convert {conversion} to seconds"


def doBreakdown(arr):
    if not len(arr) == 2:
        return
    num = ""
    try:
        num = int(arr[0])
    except ValueError:
        "INVALID FORMAT"

    time = arr[1]
    print(convertToSeconds(num, time))
