def tumba(a,w,l):
    if len(w)==l:
        if w.count("Ш")==2 or w.count("Ы")==2 or w.count("Ч")==2 or w.count("О")==2:
            print(w)
        return    
    else:
        for c in a:
            tumba(a,w+c,l)
tumba("ЫШЧО","",4)
