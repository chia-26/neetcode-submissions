class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        ans = []
        for i in strs:
            sort = ''.join(sorted(i))
            if sort in dic:
                dic[sort].append(i)
            else:
                dic[sort] = [i]
        
        for key in dic:
            ans.append(dic[key])
        
        return ans