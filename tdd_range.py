def get_ranges(samples):
    ranges = []
    current_range = []
    for i in range(len(samples)):
        if i == 0:
            current_range.append(samples[i])
        elif (samples[i] == samples[i - 1] + 1) or (samples[i] == samples[i-1]):
            current_range.append(samples[i])
        else:
            ranges.append(current_range)
            current_range = [samples[i]]
       
    ranges.append(current_range)
    
    range_counts = [(str(r[0]) + "-" + str(r[-1]), len(r)) for r in ranges if len(r) > 1]
    return range_counts

