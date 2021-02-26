def tumb(a,w,l):
    if len(w)==l:
        print(w)
        return
    if len(w)==1:
        w+="Ы"
        tumb(a,w,l)
    else:
        for c in a:
            tumb(a,w+c,l)
tumb("ЫШЧО","",4)
