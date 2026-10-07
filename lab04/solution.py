def winner(names: list[str], scores: list[float]) -> str:
    if len(names) == 0:
        return ""
    winner_name, max_score = names[0], scores[0]
    for i in range(1, len(names)):
        if scores[i] > max_score:
            max_score = scores[i]
            winner_name = names[i]
    return winner_name
