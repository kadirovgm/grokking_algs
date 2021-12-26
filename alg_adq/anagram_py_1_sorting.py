# O(n*logn)
def areAnagram (str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1!=n2:
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, n1):
        if str1[i]!=str2[i]:
            return False

    return True

# TEST
str1 = "test"
str2 = "ttse"

if areAnagram(str1, str2):
    print("there are an anagram")
else:
    print("not an anagram")

    





