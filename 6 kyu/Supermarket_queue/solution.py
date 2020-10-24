def queue_time(customers, n):
    
    if len(customers) == 0:
        return 0

    if n >= len(customers):
        return max(customers)

    tills = {}

    for i in range(n):
        tills[i] = [0,[]]

    for i in range(len(customers)):
        till = 0
        summ = tills[0][0]
        for key, value in tills.items():
            x = value[0]
            if value[0] < summ:
                till = key
                summ = value[0]

        tills[till][1].append(customers[i])
        tills[till][0] = sum(tills[till][1])
        
    duration = tills[0][0]
    for value in tills.values():
        if value[0] > duration:
            duration = value[0]
        
    return duration