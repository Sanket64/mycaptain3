string1="missisippi"
def frequent():
    fre={}
    for i in string1:
        if i in fre:
            fre[i]=fre[i]+1
        else:
            fre[i]=1
    print(str(fre))
frequent()
			

