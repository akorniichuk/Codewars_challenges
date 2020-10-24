def solution(roman):
    rom = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    edges = {"I" : ["V", "X"], "X" : ["L", "C"], "L" : ["C", "D"], "C" : ["D", "M"]}
    num = 0
    i = 0
    while i < len(roman):
        if i < len(roman) - 1:
            if roman[i] in edges.keys():
                if roman[i+1] in edges[roman[i]]:
                    num -= rom[roman[i]]
                    i += 1
                else:
                    num += rom[roman[i]]
                    i += 1
            else:
                num += rom[roman[i]]
                i += 1
        else:
                num += rom[roman[i]]
                i += 1
    return num