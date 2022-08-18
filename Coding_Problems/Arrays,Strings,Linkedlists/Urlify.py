def urlify(str, x):
    m = len(str)
    url = "%20"
    str2 = ""
    for i in range(0, x):
        if str[i] == " ":
            str2 += url
        else:
            str2 += str[i]
    return str2


print(urlify("mr john smith    ", 13))
