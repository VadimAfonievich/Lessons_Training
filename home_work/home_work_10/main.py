from flask import Flask
from utils import load_candidates

app = Flask(__name__)

candidates_list = load_candidates()


@app.route("/")
def page_candidates():
    """
    Страница выводит список всех кандидатов.
    """

    str_candidate = "<pre>"

    for candidate in candidates_list.values():
        str_candidate += f"<img src={candidate['picture']}>\n" \
                         f"Имя кандидата - {candidate['name']}\n" \
                         f"Позиция кандидата: {candidate['position']}\n" \
                         f"Навыки через запятую: {candidate['skills']}\n\n"
    str_candidate += "</pre>"

    return str_candidate


@app.route("/candidate/<int:id>/")
def page_profile(id):
    """
    Страница выводит одного кандидата по id
    :arg: id
    """

    candidate = candidates_list[id]
    candidates_description = f"<img src={candidate['picture']}>\n\n" \
                             f"Имя кандидата - {candidate['name']}\n" \
                             f"Позиция кандидата: {candidate['position']}\n" \
                             f"Навыки через запятую: {candidate['skills']}\n"

    return f"<pre>{candidates_description}<pre>"


@app.route("/skill/<skill>/")
def page_skills(skill):
    """
    Страница выводит тех кандидатов, у которых среди навыков имеются необходимые.
    :arg: skill
    """

    candidates_description = "<pre>"
    for candidate in candidates_list.values():
        candidate_skills_dict = candidate["skills"].split(", ")
        candidate_skills_dict = [i.lower() for i in candidate_skills_dict]

        if skill in candidate_skills_dict:
            candidates_description += f"Имя кандидата - {candidate['name']}\n" \
                                      f"Позиция кандидата: {candidate['position']}\n" \
                                      f"Навыки через запятую: {candidate['skills']}\n\n"
    candidates_description += "</pre>"

    return f"{candidates_description}"


app.run()
