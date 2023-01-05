from flask import Flask
from Classes.Candidates import Candidates

app = Flask(__name__)

DATA_SOURCE = "candidates.json"

candidates = Candidates(DATA_SOURCE)


@app.route("/")
def page_index():
    return candidates.get_all_candidates()


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    return candidates.get_candidate(uid)


@app.route("/skill/<skill>")
def page_skills(skill):
    return candidates.get_skill(skill.lower())
