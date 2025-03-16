import requests


def test_json_parser_returns_list():
    url = "https://olimp.miet.ru/ppo_it/api"
    response = requests.get(url)

    assert response.status_code == 200 