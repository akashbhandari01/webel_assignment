def matchPat(str1,str2):
    if str1=='':
        return True
    elif str2=='':
        return False
    elif str1[0]==str2[0]:
        return matchPat(str1[2],str2[len(str1)-1])
    else: return True

