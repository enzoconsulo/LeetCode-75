def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if s == "":
        return True

    result = 0
    for letter in s:
        if letter in t:
            index = t.index(letter)
            t = t[index+1:] 
            result += 1
        else:
            result = 0
            break
        
    return result == len(s)

s="abc" 
t="ahbgdc"
print(isSubsequence(s, t))