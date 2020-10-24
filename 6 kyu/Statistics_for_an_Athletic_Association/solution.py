def stat(strg):
    print(strg)
    import math

    # write a fnc that returns time in seconds:
    def in_seconds(lst): 
            time_in_sec = (lst[2] + 
                        lst[1]*60 + 
                        lst[0]*3600)

            return time_in_sec

    def sec_to_time(secs):
        hours = math.floor(secs/3600)
        minutes = math.floor(secs/60) - hours*60
        seconds = math.floor(secs) - hours*3600 - minutes*60

        return [hours, minutes, seconds]
        
    # getting all the data points (i.e. hours, minutes and second as int)
    times = strg.split(',')
    elements_int = []
    for time in times:
        elements = time.strip().split('|')
        
        for element in elements:
            elements_int.append(int(element))
    
    # this will give us the indivudaual times for ewach team member
    indiv_times = []
    j = 0
    for i in range(3,len(elements_int)+1, 3):
        time = elements_int[j:i]
        indiv_times.append(time)
        j = i

    # now i need to sort:
    times_sorted = indiv_times.copy()
    times_sorted.sort()

    # RANGE:
        # transform first and last element to total seconds:

    total_sec_min = in_seconds(times_sorted[0])
    total_sec_max = in_seconds(times_sorted[-1])

    range_in_sec = total_sec_max - total_sec_min
    
    team_range = sec_to_time(range_in_sec)

    # AVERAGE:
    team_time_in_sec = 0

    for indiv in times_sorted:
        team_time_in_sec += in_seconds(indiv)
    
    team_avg_in_sec = int(team_time_in_sec/len(times_sorted))

    team_avg = sec_to_time(team_avg_in_sec)

    # MEDIAN:

    if len(times_sorted)%2 == 1:
        median = times_sorted[math.floor(len(times_sorted)/2)]
    
    else: # here u need average
        median = sec_to_time(int((in_seconds(times_sorted[int(len(times_sorted)/2-1)]) + in_seconds(times_sorted[int(len(times_sorted)/2)]))/2))

    result = ("Range: %0*d"%(2,team_range[0])+"|%0*d"%(2,team_range[1])+"|%0*d"%(2,team_range[2])+" Average: %0*d"%(2,team_avg[0])+"|%0*d"%(2,team_avg[1])+"|%0*d"%(2,team_avg[2])+" Median: %0*d"%(2,median[0])+ "|%0*d"%(2,median[1])+"|%0*d"%(2,median[2]))

    return result