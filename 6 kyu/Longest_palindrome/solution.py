def longest_palindrome (s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    else:
        cuts = {}
        final = 0
        length = len(s) - 1
        for i in range(len(s)):
            x = 0
            while x < len(s):
                temp = s[i-1:i+x] #>> s[i-1: i+2/+3...len(s)-1]
                cuts[temp] = temp[len(temp)::-1]
                x += 1
        
        for key, value in cuts.items():
            if key == value:
                if len(value) > final:
                    final = len(value)

        return final