def GetLeastNumbers_Solution(tinput, k):
        x = []
        j = 0
        mid = 0
        if len(tinput) < k or k == 0:
            return []
        for i in range(k):
            x.append(0)
        
        max_ = tinput[0]
        for i in range(len(tinput)):
            if j < k:
                x [j] = tinput[i]
                j = j+1
                if max_ < tinput[i]:
                    max_ = tinput[i]
                    mid = i
                continue
            if tinput[i] < max_:
                x[mid] = tinput[i]
                max_ = x[mid]
                for y in range(k):
                    if max_ < x[y]:
                        max_ = x[y]
                        mid = y
        for i in range(k):
            for j in range(i,k):
                if x[i] > x[j]:
                    t = x[i]
                    x[i] = x[j]
                    x[j] = t
                
        return x
print(GetLeastNumbers_Solution([5,8,7,4,1,2], 5))