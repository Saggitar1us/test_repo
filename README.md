# UI Autotests (Pytest + Playwright)

Небольшой проект UI-автотестов на `pytest` и `playwright`.

## Структура

- `tests/` — тесты
- `pages/` — Page Object'ы
- `fixtures/` — фикстуры
- `reports/` — отчеты (`pytest-html`, `junit.xml`)

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Настройки

Проект читает переменные из файла `.env`:

- `BASE_URL`
- `HEADLESS`
- `BROWSERS`
- `LOGIN_USERNAME`
- `LOGIN_PASSWORD`

Пример уже есть в `.env`.

## Запуск тестов

```bash
pytest
```

Запуск по маркеру:

```bash
pytest -m smoke
```

## CI (GitLab)

В `.gitlab-ci.yml` настроены:

- job `ui_tests` — запуск тестов и сохранение `reports/` и `allure-results/`
- job `pages` — генерация Allure-отчета в `public/`
