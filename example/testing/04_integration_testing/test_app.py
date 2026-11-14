import json
import sqlite3
from contextlib import closing

import pytest

if __package__:
    from .app import create_app, export_tasks
else:
    from app import create_app, export_tasks


pytestmark = pytest.mark.integration


@pytest.fixture
def resources(tmp_path):
    db_path = tmp_path / "tasks.db"
    export_path = tmp_path / "tasks.json"
    app = create_app(db_path, export_path)
    return app.test_client(), db_path, export_path


def test_create_task(resources):
    client, db_path, export_path = resources

    response = client.post("/tasks", json={"title": "Вивчити pytest"})

    assert response.status_code == 201
    assert response.get_json()["title"] == "Вивчити pytest"
    with closing(sqlite3.connect(db_path)) as connection:
        row = connection.execute("SELECT title FROM tasks").fetchone()
    assert row == ("Вивчити pytest",)
    assert json.loads(export_path.read_text(encoding="utf-8"))[0]["title"] == "Вивчити pytest"


def test_get_tasks(resources):
    client, _, _ = resources
    client.post("/tasks", json={"title": "Перше завдання"})
    client.post("/tasks", json={"title": "Друге завдання"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.get_json()] == [
        "Перше завдання",
        "Друге завдання",
    ]


def test_create_task_requires_title(resources):
    client, _, export_path = resources

    response = client.post("/tasks", json={})

    assert response.status_code == 400
    assert not export_path.exists()


def test_empty_list_export(resources):
    client, db_path, export_path = resources
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []
    export_tasks(db_path, export_path)
    assert json.loads(export_path.read_text(encoding="utf-8")) == []


def test_export_repairs_corrupt_json(resources):
    client, _, export_path = resources
    export_path.write_text("{", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        json.loads(export_path.read_text(encoding="utf-8"))

    response = client.post("/tasks", json={"title": "Відновлення експорту"})
    assert response.status_code == 201
    assert json.loads(export_path.read_text(encoding="utf-8")) == [response.get_json()]


def test_two_tasks_ordered_in_database(resources):
    client, db_path, export_path = resources
    first = client.post("/tasks", json={"title": "Перше"})
    second = client.post("/tasks", json={"title": "Друге"})
    assert first.status_code == second.status_code == 201
    expected = [first.get_json(), second.get_json()]
    with closing(sqlite3.connect(db_path)) as connection:
        rows = connection.execute("SELECT id, title FROM tasks ORDER BY id").fetchall()
    assert rows == [(task["id"], task["title"]) for task in expected]
    assert client.get("/tasks").get_json() == expected
    assert json.loads(export_path.read_text(encoding="utf-8")) == expected


@pytest.mark.parametrize("payload", [{}, {"title": "  "}, {"title": 1}, ["title"]])
def test_invalid_post_leaves_database_and_file_unchanged(resources, payload):
    client, db_path, export_path = resources
    response = client.post("/tasks", json=payload)
    assert response.status_code == 400
    assert response.get_json() == {"error": "Поле title є обов'язковим"}
    with closing(sqlite3.connect(db_path)) as connection:
        assert connection.execute("SELECT COUNT(*) FROM tasks").fetchone() == (0,)
    assert not export_path.exists()


def test_delete_task_updates_database_and_file(resources):
    client, db_path, export_path = resources
    first = client.post("/tasks", json={"title": "Видалити"}).get_json()
    second = client.post("/tasks", json={"title": "Зберегти"}).get_json()

    response = client.delete(f"/tasks/{first['id']}")

    assert response.status_code == 204
    with closing(sqlite3.connect(db_path)) as connection:
        assert connection.execute("SELECT id, title FROM tasks").fetchall() == [
            (second["id"], second["title"]),
        ]
    assert json.loads(export_path.read_text(encoding="utf-8")) == [second]
    assert client.get("/tasks").get_json() == [second]
    assert client.delete(f"/tasks/{first['id']}").status_code == 404
