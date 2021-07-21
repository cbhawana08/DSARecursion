def func(s,st,e):
    if st==e:
        return(1)
    if(s[st]==s[e]):
        st+=1
        e-=1
        func(s,st,e)
        return(1)
    else:
        return(0)
print(func("aabaa",0,4))
print(func("geeks",0,4))
