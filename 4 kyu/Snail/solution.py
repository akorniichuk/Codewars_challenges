def snail(snail_map):
    
    if len(snail_map) == 1:
        if len(snail_map[0]) == 1:
            return snail_map[0]

        else:
            return []
    
    else:
        n_min = 0 # row
        m_min = 0 # column

        n_max = len(snail_map) - 1
        m_max = len(snail_map) - 1

        n = 0
        m = 0

        result = []
        while m_min != m_max:
            while m <= m_max: # go right
                result.append(snail_map[n][m])
                if m == m_max:
                    n += 1
                    n_min += 1
                    break
                else:
                    m += 1

            while n <= n_max: # go down
                result.append(snail_map[n][m])
                if n == n_max:
                    m -= 1
                    m_max -= 1
                    break
                else:
                    n += 1

            while m >= m_min: # go left
                result.append(snail_map[n][m])
                if m == m_min:
                    n -= 1
                    n_max -= 1
                    break
                else:
                    m -= 1

            while n >= n_min: # go up
                result.append(snail_map[n][m])
                if n == n_min:
                    m += 1
                    m_min += 1
                    break
                else:
                    n -= 1

        if len(snail_map) % 2 == 0:
            return result

        else:
            result.append(snail_map[n][m])
            return result