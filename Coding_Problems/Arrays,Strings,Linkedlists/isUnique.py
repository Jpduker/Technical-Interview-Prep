def IsUnique(string):
    for i in range(0, len(string)-1, 1):
        for j in range(len(string)-1, 0, -1):
            if string[i] == string[j]:
                return False


print(IsUnique("aple"))
