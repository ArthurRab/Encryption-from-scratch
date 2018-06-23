import string

# chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,.'\" !?"
chars = string.printable
POWER = 100


def getBinaryArr(num):
    arr = ['0' for i in range(8)]
    b = bin(num)
    for i in range(-1, -9, -1):
        if b[i] == 'b':
            break
        else:
            arr[i] = b[i]
    return arr


def getCharID(char, chars=chars):
    index = chars.index(char)
    assert index != -1, "Char not found"
    return index


def getCharBin(char):
    return getBinaryArr(getCharID(char))


def strToBinArr(string):
    arr = []
    for char in string:
        arr += getCharBin(char)
    return arr


def get(arr, start, stop=-1):
    assert len(arr) > 0, "Array length is 0"
    if stop == -1:
        return arr[start % len(arr)]

    out = []
    for i in range(start, stop):
        out.append(arr[i % len(arr)])
    assert len(out) == stop-start
    return out


def set(arr, val, start, stop=-1, shift=0, negateShift=False):
    if negateShift:
        shift *= -1
    if stop == -1:
        arr[start % len(arr)] = val
        return
    assert len(val) == stop-start, "WRONG LENGTH; len(val): " + \
        str(len(val))+", len of interval: "+str(stop-start)
    for i in range(stop-start):
        arr[(i+start) % len(arr)] = val[(i-shift) % len(val)]


def binArrToHexStr(arr):
    h = ""
    assert len(arr) % 4 == 0, str(len(arr))+" NOT DIVISBLE BY 4"
    while len(arr) > 0:
        first4, arr = arr[0:4], arr[4:]
        h += hex(int("".join(first4), 2))[2:]
    return h


def binArrToStr(arr, chars=chars):
    out = ""
    assert len(arr) % 8 == 0, str(len(arr)) + " NOT DIVISILE BY 8"
    while len(arr) > 0:
        first8, arr = arr[0:8], arr[8:]
        out += chars[int("".join(first8), 2)]
    return out


def hexToBinArr(h):
    a = list(bin(int(h, 16))[2:])
    a = ['0' for i in range((-len(a)) % 8)] + a
    return a


def acrypt(string, key, decrypt=False):
    if decrypt:
        arr = hexToBinArr(string)
    else:
        arr = strToBinArr(string)
    instrs = strToBinArr(key)

    r = (len(arr)+len(instrs))*POWER
    if decrypt:
        start = r - 1
        end = -1
        step = -1
    else:
        start = 0
        end = r
        step = 1

    for i in range(start, end, step):
        instr = "".join(get(instrs, i*2, i*2 + 2))
        if instr == "00":
            set(arr, str(int(not int(get(arr, i)))), i)
        elif instr == "01":
            set(arr, get(arr, i-4, i+2)[::-1], i-4, i+2, i)
        elif instr == "10":
            set(arr, get(arr, i-1, i+7)[::-1], i-1, i+7, i)
        else:
            set(arr, get(arr, i-1, i+2)[::-1], i-1, i+2, i)

    if decrypt:
        return binArrToStr(arr)
    else:
        return binArrToHexStr(arr)


def hash(s):
    return acrypt(string="AAAAAAAAAA", key=s)


string = "Sunset is the time of day when our sky meets the outer space solar winds. There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons caught in a blender. The sun moves slowly to hide behind the line of horizon, while the moon races to take its place in prominence atop the night sky. People slow to a crawl, entranced, fully forgetting the deeds that still must be done. There is a coolness, a calmness, when the sun does set."
key = "U(*u1sd98u898as8dj9238j9238dj(A*SJd98j3s"

print('Original:\n', string, '\n')
print('Original in hex:\n', binArrToHexStr(strToBinArr(string)), '\n')
a = acrypt(string, key)
print('Encrypted hex:\n', a, '\n')
print('Decrypted:\n', acrypt(a, key, decrypt=True), '\n')


print("Hashed: \n", hash(string))
