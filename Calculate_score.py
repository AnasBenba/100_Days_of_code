def calculate_score(list = []):
    i = 0
    score = 0
    while len(list) > i:
        score += list[i]
        i += 1
    return score