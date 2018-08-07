"""given uppercase convert to lower case"""

def lowercase(s):
	ans = []
    for i in str:
        if (65 <= ord(i) <= 90):
            ans.append(chr(ord(i)+32))
        else:
            ans.append(i)

    return("".join(ans))
    