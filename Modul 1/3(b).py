def jumlahhurufkonsonan(a):
    v="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    konsonan=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            konsonan+=1
    return (jumlahhuruf,konsonan)
