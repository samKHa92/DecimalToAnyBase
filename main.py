'''
use the function baseconv(base, x, c), where 'base' is system base where you want to convert the decimal number, 'x' is the
decimal number to be converted and 'c' is the index of the digit on which you want to approximate the converted number. 
'''


dict = {}
for i in range(0,10):
    dict[str(i)] = str(i)
for i in range(10,36):
    dict[str(i)]=chr(55+i)
print("Calculating...")

def get_key_from_value(d, val):
    return [k for k, v in d.items() if v == val]

def lsttostr(lst):
    stri = ""
    for x in lst:
        stri += str(x)
    return stri

def normalize(base, x):
    c = 0
    for d in str(x):
        if d != "0":
            break
        else:
            c += 1
    if c > 1:
        return str(x)[c:] + " * "+str(base)+"^(-"+str(c)+")"
    return str(x)

def baseconvfloatwperiod(base, x):
    fr = str(x).split('.')[1]
    exp = len(fr)
    res = ""
    y = x
    pcl = []
    pcl.append(y)
    while y != 0:
        y *= base
        res += dict[str(int(y))]
        t = False
        if len(str(y).split('.')[1]) > exp:
            if int(str(y).split('.')[1][exp]) == 9:
                t = True
        if t:
            zs = ""
            for i in range(exp):
                zs += "0"
            y += float("0."+zs+"1")
        y = float("0."+str(y).split('.')[1][:exp])
        if y in pcl:
            i = pcl.index(y)
            return res[:i]+"{"+res[i:]+"}"
        pcl.append(y)
    return res

def baseconvfloat(base, x, c):
    cc = c
    fr = str(x).split('.')[1]
    exp = len(fr)
    res = ""
    y = x
    pcl = []
    pcl.append(y)
    while c > -1:
        y *= base
        res += dict[str(int(y))]
        t = False
        if len(str(y).split('.')[1]) > exp:
            if int(str(y).split('.')[1][exp]) == 9:
                t = True
        if t:
            zs = ""
            for i in range(exp):
                zs += "0"
            y += float("0."+zs+"1")
        y = float("0."+str(y).split('.')[1][:exp])
        # if y == 0:
        #     return res[:cc], False
        c -= 1
    counter = 0
    lst = []
    for x in res:
        lst.append(str(x))
    for d in range(len(res)-1, -1, -1):
        if int(get_key_from_value(dict,res[d])[0]) >= base - 1:
            counter += 1
            lst[d] = "0"
            lst[d - 1] = dict[str(int(get_key_from_value(dict, res[d - 1])[0]) + 1)]
            res = lsttostr(lst)
        elif int(get_key_from_value(dict,res[d])[0]) >= base // 2:
            # lst[d] = dict[str(int(get_key_from_value(dict,res[d])[0])+1)]
            if d >= cc:
                lst[d] = "0"
                lst[d-1] = dict[str(int(get_key_from_value(dict, res[d-1])[0])+1)]
            res = lsttostr(lst)
            lst = lst[:len(lst)-counter]
            # return lsttostr(lst)[:cc], False
        else:
            return lsttostr(lst)[:cc], False
    return "0", True

def baseconv(base, x, c):
    y = abs(x)
    z = int(str(y).split(".")[0])
    res = ""
    while z != 0:
        r = z % base
        z //= base
        res = dict[str(r)] + res
    if len(str(y).split(".")) == 2:
        flop = baseconvfloatwperiod(base,float("0."+str(x).split(".")[1]))
        flo = baseconvfloat(base,float("0."+str(x).split(".")[1]),c)
        res1 = res
        lfl = [x for x in flop if x != "{" and x != "}"]
        flopp = lsttostr(lfl)
        if flo[1]:
            res1 = str(int(res)+1)
        if x < 0:
            print("Exact conversion: " + "-"+res+"."+flop)
            print("Rounded conversion: " + "-" + res1 + "." + flo[0])
            print("Normalized conversion: " + "-" + res + " + " + normalize(base, flopp))

        else:
            print("Exact conversion: " + res + "." + flop)
            print("Rounded conversion: " + res1 + "." + flo[0])
            print("Normalized conversion: " + res + " + " + normalize(base, flopp))

    else:
        if x < 0:
            print("Exact conversion: " + "-"+res)
            print("Rounded conversion: " + "-" + res)
            print("Normalized conversion: " + "-"+res)

        else:
            print("Exact conversion: " + res)
            print("Rounded conversion: " + res)
            print("Normalized conversion: " + res)


baseconv(16, 37.001, 3)
