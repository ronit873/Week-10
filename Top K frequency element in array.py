class Solution:
    def topKFrequent(self, arr, k):
        dict={}
        for i in arr:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        arr=[]   
        d=sorted(dict.keys())[::-1]
        max1=max(dict.values())
        while(k>0):
           for i in d:
                if dict[i]==max1:
                    if k>0:
                        arr.append(i)
                    k-=1
           max1=max1-1
        
        return arr

