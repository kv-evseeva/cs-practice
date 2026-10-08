def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    winner_name, max_score = names[0], scores[0]
    for i in range(1, len(names)):
        if scores[i] > max_score:
            max_score = scores[i]
            winner_name = names[i]
    return winner_name


def average(scores: list[float]) -> float:
    if not scores:
        return float(f"{0:.2f}")
    scores_sum, count = 0.0, 0
    for score in scores:
        scores_sum += score
        count += 1
    return float(f"{scores_sum / count:.2f}")


def ranking(names: list[str], scores: list[float]) -> list[str]:
    if not names:
        return []
    tupled_list = list(zip(names, scores))
    tupled_list.sort(key=lambda item: item[1], reverse=True)
    rank = [item[0] for item in tupled_list]
    return rank


def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg_score = average(scores)
    names_above_avg = [names[i] for i in range(len(names)) if scores[i] > avg_score]
    return names_above_avg
