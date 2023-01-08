import json


def load_candidates():
    """
    Открывает json файл. Создает словарь словарей кандидатов.
    :return: list of candidates
    """

    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates_dict = json.load(file)

        candidates = {}
        for candidate in candidates_dict:
            candidates[candidate["id"]] = candidate

        return candidates
