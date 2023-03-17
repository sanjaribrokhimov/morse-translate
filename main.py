from preloaded import MORSE_CODE

def decode_morse(morse_code):
    list=morse_code.split(" ")
    res = []
    for i in list:
        for j  in MORSE_CODE:
            if i == j:
                res.append(MORSE_CODE[i])
            if i == "":
                res.append(" ")
    txt = "".join(res)
    
    a=txt.split()
    apn=[]
    for i in a:
         apn.append(f"{i} ")
    return "".join(apn)[:-1]
