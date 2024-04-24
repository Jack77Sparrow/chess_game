from figure import text
print(ord("a"))
some = text


index1, index2 = some[0].lower(), some[1]

U = []

for i in range(8):
    row = []
    for j in range(8):
        row.append((i, j))
    U.append(row)
    
for k in U:
    print(k)


print(U[ord(index1)-96][int(index2)])