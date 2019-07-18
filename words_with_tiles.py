class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        dic={}
        for index in range(len(tiles)):
            if tiles[index] in dic:
                dic[tiles[index]]+=1
            else:
                dic[tiles[index]]=1

        for key in len(dic):
            

        print(dic)

sol=Solution()
sol.numTilePossibilities("ABCC")
