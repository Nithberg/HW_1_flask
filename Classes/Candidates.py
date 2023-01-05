import json


class Candidates:

    def __init__(self, data):
        with open(data, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def get_all_candidates(self):
        all_candidates = "<pre>\n"
        for i in self.data:
            all_candidates += f'<strong>{i["name"]}</strong>\n{i["position"]}\n{i["skills"]}\n\n'
        all_candidates += "</pre>"
        return all_candidates

    def get_candidate(self, uid):
        for i in self.data:
            if uid == i["id"]:
                candidate = f'<img src="{i["picture"]}">' \
                            f'<pre><strong>{i["name"]}</strong>\n{i["position"]}\n{i["skills"]}\n\n</pre>'
                return candidate

    def get_skill(self, skill):
        sorted_candidate = "<pre>\n"
        for i in self.data:
            candidate_skill = i["skills"].split(", ")
            candidate_skill = [s.lower() for s in candidate_skill]
            if skill in candidate_skill:
                sorted_candidate += f'<strong>{i["name"]}</strong>\n{i["position"]}\n{i["skills"]}\n\n'
            else:
                return f"<h1><strong>Такой страницы не существует!</strong></h1>"
        sorted_candidate += "</pre>"
        return sorted_candidate

# DATA_SOURCE = "../candidates.json"
