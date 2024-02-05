def count_intersections(radians, identifiers):
    #creating a list of tuples and sorting them based on the starting radians
    chords = sorted([(radians[identifiers.index('s_' + str(i))], radians[identifiers.index('e_' + str(i))]) for i in range(1, len(radians) // 2 + 1)])

    intersection_count = 0

    #iterating through chords and comparing them to check for intersections
    for i in range(len(chords)):
        for j in range(i + 1, len(chords)):
            start_i, end_i = chords[i]
            start_j, end_j = chords[j]

            if (start_i < start_j < end_i < end_j) or (start_j < start_i < end_j < end_i):
                intersection_count += 1

    return intersection_count