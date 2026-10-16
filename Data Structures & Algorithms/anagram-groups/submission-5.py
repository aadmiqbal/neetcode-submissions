
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #to find anangram length equal and occurences of each letter the same, using 2 dictionaries for each word

        sorteddict = defaultdict(list)

        strs.sort(key = len)

        for i in range(len(strs)):
            sorteddict["".join(sorted(strs[i]))].append(strs[i])
        newlist = []
        for x in sorteddict.values():
            newlist.append(x)
        return newlist


    def checkAnagram(x,y):
        xdict, ydict = {}, {}
        for i in range(len(x)):
            xdict[x[i]] = 1 + xdict.get(x[i],0)
            ydict[y[i]] = 1 + ydict.get(y[i],0)
        return xdict == ydict
