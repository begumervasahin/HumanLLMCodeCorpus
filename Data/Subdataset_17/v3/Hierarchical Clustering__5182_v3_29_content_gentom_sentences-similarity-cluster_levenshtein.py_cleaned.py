def edit_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    previous_row = list(range(len(s1) + 1))
    for i2, c2 in enumerate(s2):
        current_row = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                current_row.append(previous_row[i1])
            else:
                insertion_cost = previous_row[i1 + 1] + 1
                deletion_cost = current_row[i1] + 1
                substitution_cost = previous_row[i1] + 1
                current_row.append(min(insertion_cost, deletion_cost, substitution_cost))
        previous_row = current_row
    return previous_row[-1]
def alternative_distance(s1, s2):
    if len(s1) < len(s2):
        return alternative_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertion_cost = previous_row[j + 1] + 1
            deletion_cost = current_row[j] + 1
            substitution_cost = previous_row[j] + (c1 != c2)
            current_row.append(min(insertion_cost, deletion_cost, substitution_cost))
        previous_row = current_row
    return previous_row[-1]
if __name__ == "__main__":
    s1 = "kitten"
    s2 = "sitting"
    print(f"Edit distance between '{s1}' and '{s2}' using edit_distance function: {edit_distance(s1, s2)}")
    print(f"Edit distance between '{s1}' and '{s2}' using alternative_distance function: {alternative_distance(s1, s2)}")