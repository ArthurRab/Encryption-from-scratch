chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,.'\" !?"
h = "0123456789abcdef"
POWER = 80


def getBinaryArry(num):
    arr = [0 for i in range(8)]
    b = bin(num)
    for i in range(-1, -9, -1):
        if b[i] == 'b':
            break
        else:
            arr[i] = b[i]
    return arr


def getCharID(char, chars=chars):
    index = chars.index(char)
    if index == -1:
        print("Char not found")
        return 0
    return index


def getCharBin(char):
    return getBinaryArry(getCharID(char))


def strToBinArr(string):
    arr = []
    for char in string:
        arr += char
    return arr


def ancrypt(string, key, startPos=0, toBin=strToBinArr, fromBin=None):
    arr = toBin(string)
    instrs = strToBinArr(key)

    for i in range((len(arr)+len(instrs))*POWER):
        instr = get(instrs, i*2, i*2 + 2)
        if instr == "00":
            set(arr, str(int(not int(get(arr, i)))), i)
        elif instr == "01":
            set(arr, get(arr, i, i+2).reverse(), i, i+2)
        elif instr == "10":
            set(arr, get(arr, i-1, i+1).reverse(), i-1, i+1)
        else:
            set(arr, get(arr, i-1, i+2).reverse, i-1, i+2)


def get(arr, start, stop=-1):
    if stop == -1:
        stop = start+1
    out = []
    for i in range(start, stop):
        out.append(arr[i % len(arr)])
    return out


def set(arr, val, start, stop=-1):
    if stop == -1:
        stop = start+1
    assert len(val) == start - stop + 1, "WRONG LENGTH"
    for i in range(start - stop):
        arr[(i+start) % len(arr)] = val[i]


def binArrToHexStr(arr):
    hArr = []
    
    first4, rest = arr[0:5], arr[5:]
