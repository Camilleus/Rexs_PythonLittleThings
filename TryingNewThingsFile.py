def data_preparation(data):
    result = []

    for sublist in data:
        if len(sublist) > 2:
            sublist.remove(min(sublist))
            sublist.remove(max(sublist))
            result.extend(sublist)
        else:
            sublist.extend(sublist)

    result.sort(reverse=True)
    return result