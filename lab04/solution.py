def winner(names: list[str], scores: list[float]) -> str:
    if len(names) == 0:
        return ""
    winner_name, max_score = names[0], scores[0]
    for i in range(1, len(names)):
        if scores[i] > max_score:
            max_score = scores[i]
            winner_name = names[i]
    return winner_name


def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return float(f"{0:.2f}")
    scores_sum, count = 0.0, 0
    for score in scores:
        scores_sum += score
        count += 1
    return float(f"{scores_sum / count:.2f}")
