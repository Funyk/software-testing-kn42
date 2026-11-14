[![Manual and scheduled testing](https://github.com/Funyk/software-testing-kn42/actions/workflows/manual-testing.yml/badge.svg)](https://github.com/Funyk/software-testing-kn42/actions/workflows/manual-testing.yml)

# Тестування програм та програмних комплексів

**Костюк Артем, КН-42**

Навчальний репозиторій ІТ коледжу Львівської політехніки.

## Роботи

1. [Загальне тестування та юніт-тести](testing/1_lab/README.md)
2. [Тестування з бібліотекою pytest](testing/2_lab/README.md)
3. [Покриття коду](testing/3_lab/README.md)
4. [Інтеграційне тестування](testing/4_lab/README.md)
5. [Автоматизація запуску тестів через GitHub Actions](testing/5_lab/README.md)

## Запуск

Потрібні Python 3.13 і Poetry. Команди виконуються з кореня репозиторію.

```bash
poetry install
make test
make unit
make integration
make coverage
```

Каталог `example/testing` містить виконані вправи з методичок. У `testing` збережені звіти та виконані приклади із занять.

[Методичні матеріали](https://github.com/BobasB/it_college) · [Вихідні матеріали занять](https://github.com/BobasB/2025_kn33_oop/tree/fd26a93cfd01e34ad774061100d2fbfaeb1b48fa/testing)
