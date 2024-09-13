class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currentStreak=0
        maxStreak=currentStreak
        hash={}
        arr=[]

        for i in range(0,len(s)):
            if s[i] in hash.keys():
                while True:
                    if arr[0]==s[i]: 
                        del hash[arr[0]]
                        arr.pop(0)
                        break
                    del hash[arr[0]]
                    arr.pop(0)
                
                currentStreak=len(arr)
                
            currentStreak+=1
            hash[s[i]]=True
            arr.append(s[i])
            if currentStreak>maxStreak:
                maxStreak=currentStreak

        return maxStreak
            