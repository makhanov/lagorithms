def lengthOfLongestString(s):
    hashmap = {}
    temp = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[j] not in temp:
                temp.append(s[j])
            else:
                break
        hashmap[i] = temp
        temp = []

    maximum = 0
    for i in range(len(s)):
        if len(hashmap[i])>maximum:
            maximum = len(hashmap[i])
    return maximum
    print(maximum)

#return 3
lengthOfLongestString('pwwkew')