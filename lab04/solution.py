'''
Принимает список имен участников и список их результатов.
Возвращает имя участника с наибольшим результатом;
при равенстве — тот, кто раньше в списке.
'''
def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    winner_name, max_score = names[0], scores[0]
    for i in range(1, len(names)):
        if scores[i] > max_score:
            max_score = scores[i]
            winner_name = names[i]
    return winner_name


'''
Принимает список результатов участников.
Возвращает средний результат, округлённый до сотых.
'''
def average(scores: list[float]) -> float:
    if not scores:
        return float(f"{0:.2f}")
    scores_sum, count = 0.0, 0
    for score in scores:
        scores_sum += score
        count += 1
    return float(f"{scores_sum / count:.2f}")


'''
Принимает список имен участников и список их результатов.
Возвращает список имен по убыванию результата;
при равенстве — в исходном порядке.
'''
def ranking(names: list[str], scores: list[float]) -> list[str]:
    if not names:
        return []
    tupled_list = list(zip(names, scores))
    tupled_list.sort(key=lambda item: item[1], reverse=True)
    rank = [item[0] for item in tupled_list]
    return rank


'''
Принимает список имен участников и список их результатов.
Возвращает имена тех, чей результат строго выше среднего;
порядок — как в списке.
'''
def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg_score = average(scores)
    names_above_avg = [names[i] for i in range(len(names)) if scores[i] > avg_score]
    return names_above_avg


if __name__ == "__main__":
    names = ["Юля", "Саша", "Ваня", "Настя", "Оля"]
    scores = [7.0, 9.5, 9.5, 6.7, 5.6]
    print("Победитель:", winner(names, scores))
    print("Средний результат:", average(scores))
    print("Рейтинг по убыванию:", ranking(names, scores))
    print("Результат выше среднего:", above_average(names, scores))
    print(average([]))
