# check if two strings are anagrams 



s1 = "mango"
s2 = "nmaog"


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for k in freq1:
        if k not in freq2 or freq1[k] != freq2[k]:
            return False
    
    return True


if (are_anagrams(s1,s2)):
    print("The two strings are anagrams")
else:
    print("The two strings are not anagrams")