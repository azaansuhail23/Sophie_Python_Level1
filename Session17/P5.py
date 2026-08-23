def Present(list, target):

    for i in range(len(list)):
        if list[i] == target:
            return True

    return False


list = [10, 1, 99, 14, 5, 7, 8, 6]

res = Present(list, 14)
print(res)


#Linear Search 