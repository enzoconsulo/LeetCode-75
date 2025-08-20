class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        i = 0
        tmp = ""
        while True:
            
            if i < len(word1):
                if word1[i] != "":
                    result += word1[i]

            if i < len(word2):
                if word2[i] != "":
                    result += word2[i]


            if result == tmp:
                break

            i+= 1
            tmp = result

        return result