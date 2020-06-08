def pair_sum(arr,k):

    if len(k) < 2:
        return

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num,target)))

    return len(output)
    print '\n'.join(map(str, list(output)))

