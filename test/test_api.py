import pytest
import requests
from api.main import YandexUploader
from dotenv import load_dotenv
import os


load_dotenv()

folder_path = 'ip_info'
TOKEN = os.getenv("API_TOKEN")
BASE_URL = 'https://cloud-api.yandex.net/'
headers = {
        "Authorization": f"OAuth {TOKEN}",
    }
def test_token_exists():
    token = TOKEN
    assert token is not None, "Токен должен быть определён в .env"
    assert isinstance(token, str), "Токен должен быть строкой"
    assert len(token) > 0, "Токен не должен быть пустой строкой"


@pytest.mark.integration
def test_token_valid():

    if not TOKEN:
        pytest.skip("Токен не найден в .env, пропускаем интеграционный тест")

    headers = {
        "Authorization": f"OAuth {TOKEN}",
    }

    response = requests.get(f"{BASE_URL}v1/disk", headers=headers, timeout=10)


    # Если токен невалиден — будет 401 Unauthorized.
    assert response.status_code == 200, f"Токен невалиден: {response.status_code} {response.text}"



@pytest.fixture
def create_and_cleanup_folder():
    response = requests.put(f'{BASE_URL}v1/disk/resources', headers=headers, params={'path': folder_path})
    assert response.status_code in [201, 409], f"Ошибка при создании: {response.text}"
    yield folder_path


def test_create_folder_success():
    response = requests.put(f'{BASE_URL}v1/disk/resources', headers=headers, params={'path': folder_path})
    assert response.status_code in [201, 409]



def test_create_folder_invalid_path():
    path = "/bad:folder/name"
    resp = requests.put(f"{BASE_URL}?path={path}", headers=headers)
    assert resp.status_code not in (200, 201), f"Недопустимый путь не отвергнут: {resp.status_code}"
