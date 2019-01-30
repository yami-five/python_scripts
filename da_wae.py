letters='ABCDEFG'
strings=[]
for i in letters:
        string=i
        for j in letters:
                if j not in string:
                        string+=j
                        for k in letters:
                                if k not in string:
                                        string+=k
                                        for l in letters:
                                                if l not in string:
                                                        string+=l
                                                        for m in letters:
                                                                if m not in string:
                                                                        string+=m
                                                                        for n in letters:
                                                                                if n not in string:
                                                                                        string+=n
                                                                                        for o in letters:
                                                                                                if o not in string:
                                                                                                        string+=o
                                                                                                        strings.append(string)
                                                                                                string=string[:6]
                                                                                string=string[:5]
                                                                string=string[:4]
                                                string=string[:3]
                                string=string[:2]
                string=string[:1]

weights=[[0,12,32,24,9,21,17],[12,0,10,14,30,2,20],[32,10,0,5,12,10,16],[24,14,5,0,22,31,4],[9,30,12,22,0,12,24],[21,2,10,31,12,0,7],[17,20,16,4,24,7,0]]

da_wae=1000
points=''
for i in range(0,len(strings)-1):
        sum=0
        string=strings[i]
        for x in range(0,len(string)-1):
                if x==len(string)-1:
                        letter1=letters.find(string[x])
                        letter2=letters.find(string[0])
                else:
                        letter1=letters.find(string[x])
                        letter2=letters.find(string[x+1])
                sum+=weights[letter1][letter2]
        if sum<da_wae:
                da_wae=sum
                points=string
print(da_wae)
print(points)
