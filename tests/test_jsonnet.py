import json

from _jsonnet import evaluate_file


def test_jsonnet() -> None:
    filename = "tests/fixtures/people.jsonnet"

    data = json.loads(evaluate_file(filename))
    assert data["person1"]["welcome"] == "Hello Alice!"
    assert data["person2"]["welcome"] == "Hello Bob!"
