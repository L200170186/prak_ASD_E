a = [2,12,23,45,52]
b = [3,8,34,43,65]

c = a+b
for i in range(len(c)): 
    min_idx = i 
    for j in range(i+1, len(c)): 
        if c[min_idx] > c[j]: 
            min_idx = j 
    
    c[i], c[min_idx] = c[min_idx], c[i]

print (c)
