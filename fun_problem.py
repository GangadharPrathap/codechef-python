def fun(t,s,stop):
    if s>stop:
        return
    print(t,'X',s,'=',t*s)
    fun(t,s+1,stop)
fun(3,1,10)    