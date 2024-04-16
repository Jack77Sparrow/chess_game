
def linear_search(masive, target):
    for i in range(len(masive)):
        if masive[i] == target:
            return f"found {target} in index {i}"

    return -1

mas = [1,2,3,4,5]
target = 3
result = linear_search(mas, target)
print(result)