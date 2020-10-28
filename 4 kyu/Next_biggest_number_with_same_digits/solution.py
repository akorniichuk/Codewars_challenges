def next_bigger(n):

    '''
    Here is the idea:
        condition: x < y (x vs y)
        checking digits - second to last vs last; third to last vs second to last etc.
        once the condition is met, the intire right side of the number is seperated.
        Left side is used as is and stored.
        For the correct output the right side should be reorganized as followed:
            take next largest number than x (that satisfied the condition above) as a leading number, 
            and sort the remaining in descending order
            
        Output: Left side (unchanged) + leading number (next largest to x) + sorted remainder.
        
        EX: n = 48459853
        
            left side = 484
            right side = 59853
            x = 5
            next largest = 8 (leading number)
            remaining numbers = 5953 >> sorted: 3559
            Output = 48483559
    
    '''
    
    m = str(n)

    i = len(m) - 1
    j = len(m) - 2

    result = ''
    slicer = -2
    while j >= 0:

        if int(m[j]) < int(m[i]):
            result = m[:slicer]
            leftover = m[slicer:]
            lst = [int(z) for z in leftover]
            lst.sort(reverse = True)
            starting_index = lst.index(int(m[j]))
            first = lst[starting_index - 1]
            del lst[starting_index - 1]
            lst.sort()
            middle = ''.join([str(x) for x in lst])
            result = result + str(first) + middle
            return int(result)

        else:
            slicer -=1
            i -= 1
            j -= 1

    if result == '':
        return -1

    else:
        return eval(result)