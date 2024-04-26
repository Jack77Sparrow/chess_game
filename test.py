from figure import record_audio_and_recognize

loh = record_audio_and_recognize()

print(loh)
def recurs(some):
    index1, index2 = some[0].lower(), some[-1]

    U = []

    for i in range(8):
        row = []
        for j in range(8):
            row.append((i, j))
        U.append(row)
        
    for k in U:
        print(k)
    print((U[ord(index1)-97][int(index2)-1]))

try: 
    recurs(loh)
    
except IndexError or ValueError:
    print("try again")
    recurs(loh)
    