def solution(t):
    seen=[]
    for i in range(len(A)):
        for j in t:
            if j in range(1,100000+1):
                seen.append(j)
    return seen
t=[10,12,45,78]
solution(t)

#def solution(A):
    #for num in A:
       # if num > 0:
           # seen.add(num)