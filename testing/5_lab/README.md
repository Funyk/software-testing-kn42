# Звіт до роботи 5

**Виконав Костюк Артем, група КН-42**

## Тема

Автоматизація запуску тестів через GitHub Actions

### Мета роботи

Створити workflow з шаблону та вручну, запустити програму і тести, перевірити ручний запуск з параметром, запуск за розкладом та умовне виконання кроку.

---

### Виконання роботи

1. У вкладці **Actions** вибрано **Python application → Configure**. Шаблон збережено без редагування у [першому коміті](https://github.com/Funyk/software-testing-kn42/commit/11a8f022d53050125e78651250f81ecd6bb9ccf5). Він отримує код через `checkout`, готує Python через `setup-python`, встановлює пакети, виконує статичну перевірку `flake8` і запускає `pytest`.
2. У [python-app.yml](../../.github/workflows/python-app.yml) налаштовано Python 3.13 і встановлення залежностей через Poetry. З шаблону збережено перевірку `flake8`, у якій синтаксичні помилки та невизначені імена зупиняють збірку, а зауваження до стилю залишаються у журналі. Крок `Run Python` запускає `game.py` з роботи №1. Далі `pytest -v` запускає весь набір тестів. Окремий крок роботи №3 перевіряє поріг 90% для `app.py` і зберігає `coverage.xml` як артефакт `coverage-report`.
3. У [manual-testing.yml](../../.github/workflows/manual-testing.yml) налаштовано `workflow_dispatch` з текстовим параметром `name` та `schedule` із часом `57 1 * * 6`. Це субота о 01:57 UTC. Два завдання запускають груповий сценарій Bash і програму Python з роботи №1. Крок `Send greeting` виконується лише за ручного запуску, якщо передано ім’я, відмінне від `Executer`.

[Перший запуск шаблону](https://github.com/Funyk/software-testing-kn42/actions/runs/43540733689) завершився кодом `5`, тому що в репозиторії ще не було тестів. Журнал `pytest` показав `collected 0 items`.

У матеріалах групи є демонстрація помилки запуску. [`action.sh`](action.sh) завершився з кодом `0`, а [`action.py`](action.py) вивів повідомлення про помилку та через `SystemExit` завершився з кодом `1`. [Вивід Bash](results/05-group-bash.txt) · [Вивід Python](results/05-group-python.txt).

### Результати

| Запуск | Результат |
| --- | --- |
| [Python application](https://github.com/Funyk/software-testing-kn42/actions/runs/43541828276) | 118 тестів і 12 підтестів пройдено. Один навчальний тест позначено `skip`. Окрема перевірка `app.py` показала 100% при порозі 90%. |
| [Ручний запуск з `name=Артем`](https://github.com/Funyk/software-testing-kn42/actions/runs/43541871473) | Завдання Bash і Python пройшли. Крок `Send greeting` вивів `Привіт, Артем!`. |

Вираз `57 1 * * 6` перевірено в [CronTab Guru](https://crontab.guru/#57_1_*_*_6). Для GitHub Actions час у виразі задано в UTC. [Перевірка виразу](pictures/cron-expression.png).

![Два workflow у вкладці Actions](pictures/workflows.png)

![Результат двох завдань ручного запуску](pictures/manual-jobs.png)

![Крок Send greeting із заданим іменем](pictures/manual-greeting.png)

---

### Висновок

Workflow з шаблону автоматизує перевірки проєкту й контролює поріг покриття. Другий workflow демонструє незалежні завдання, ручний параметр і умову виконання окремого кроку.

### Джерела

[Методичка](https://github.com/BobasB/it_college/tree/f04f70102c2fe3cef4a27e32135a6689c14bf5d3/notes/08_github_actions) · [Матеріали занять](https://github.com/BobasB/2025_kn33_oop/tree/fd26a93cfd01e34ad774061100d2fbfaeb1b48fa/testing/5_lab)
