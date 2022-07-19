###Roman to Integer from Leet Code 22/07/19 ##

##my solution
def romanToInt(s: str) -> int:
    c=dict()

    RtIdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4,
               'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    i = -1
    while True:
        if i > -1 * len(s) and RtIdict[s[i]] > RtIdict[s[i - 1]]:
            word = s[i-1] + s[i]
            if word not in c:
                c[s[i - 1] + s[i]] = 1
            else:
                c[s[i - 1] + s[i]] += 1
            i -= 2
        else:
            if s[i] not in c:
                c[s[i]] = 1
            else:
                c[s[i]] += 1
            i -= 1

        if i < -1 * len(s):
            break
    print('c : ',c)
    out = 0
    for key in c.keys():
        out += c[key] * RtIdict[key]

    return out

print(romanToInt(s="MCMXIV"))

##best solution##   생각할 수 있었는데 이걸못하네... 한번 더 생각하자
def romanToInt(self, s: str) -> int:
    RtIdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    out = 0
    for i in range(len(s) - 1):
        if RtIdict[s[i]] < RtIdict[s[i + 1]]:
            out -= RtIdict[s[i]]
        else:
            out += RtIdict[s[i]]

    return out + RtIdict[s[-1]]