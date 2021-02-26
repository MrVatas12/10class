def tumba(a,w,l):
    if len(w)==l:
        if w.count("ШШ")==1 or w.count("ЫЫ")==1 or w.count("ЧЧ")==1 or w.count("ОО")==1:
            print(w)
        return    
    else:
        for c in a:
            tumba(a,w+c,l)
tumba("ЫШЧО","",4)
