def fordb(name,data,fields):
    res='{"'+name+'":['
    if len(data[0])==len(fields):
        for d in data:
            s="{"
            for (j,k) in zip(d,fields):
                s+=f'"{k.name}":"{j}",'
            res+=s+"},"   
    res+="]}"
    print(res)
    return res