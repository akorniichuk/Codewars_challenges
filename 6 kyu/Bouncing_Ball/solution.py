def bouncing_ball(h, bounce, window):
    
    if h == 0 or (bounce <= 0 or bounce >= 1) or window >= h:
        return -1

    else:

        count = 0
        
        while h > window:

            h2 = h * bounce

            if h2 > window:
                count += 2

            if h2 <= window:
                count += 1

            h = h2

        return count