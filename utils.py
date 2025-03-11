import json
from structures import InputItem, OutputItem


def load_inputs(file_path="inputs.json"):
    with open(file_path, "r") as file:
        return [InputItem(**item) for item in json.load(file)]


def save_labeled_data(output_item: OutputItem, file_path="labeled_data.json"):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append({
        "ID": str(output_item.ID),
        "labeled_data": [
            {"word": w.word, "labels": [lbl.name for lbl in w.label], "position": w.position,
             "sentence_id": w.sentence_id}
            for w in output_item.labeled_data
        ]
    })

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
