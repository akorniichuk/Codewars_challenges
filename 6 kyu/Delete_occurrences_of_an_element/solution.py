def delete_nth(order,max_e):
    final = []
    status = {}

    for item in order:
        if status.get(item):
            status[item] += 1
            if status[item] <=max_e:
                final.append(item)
        else:
            status[item] = 1
            final.append(item)
    return final