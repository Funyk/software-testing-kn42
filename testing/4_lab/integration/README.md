## Інтеграційний тест для перевірки роботи SQL-запитів у нашому додатку.

> просто запуск програми, яка виконує SQL-запити та перевіряє їх результати.
```bash
poetry install
cd testing/4_lab/integration
PYTHONPATH=src poetry run python -m integration
```

> запуск тестів через pytest із кореня репозиторію.
```bash
poetry run pytest testing/4_lab/integration/tests -v
```
