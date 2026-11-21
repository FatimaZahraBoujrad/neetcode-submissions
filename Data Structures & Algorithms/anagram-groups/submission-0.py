class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=[]
        sorted_strs={}
        for i,s in enumerate(strs):
            sorted_str=''.join(sorted(s))
            sorted_strs[sorted_str]=sorted_strs.get(sorted_str,[])+[s]

        anagrams=[anagram for anagram in sorted_strs.values()]
        return anagrams