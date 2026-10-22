# To-do API
Небольшой REST API списка задач на FastAPI. 
Учебный проект для практической работы по CI/CD (GitHub Actions)
## Запуск
```bash
uv sync
uv run uvicorn main:app --reload
```

Интерактивная документация API: http://127.0.0.1:8000/docs

## Эндпоинты
| Метод | Путь | Описание |
|---|---|---|
| GET | /health | проверка работоспособности |
| GET | /tasks | список задач |
| POST | /tasks?title=... | добавить задачу |

## Тесты
```bash
uv run pytest -v
```

## CI/CD

Workflow .github/workflows/main.yml запускается при каждом push и pull request:
- запускает тесты;
- генерирует документацию API и публикует её на GitHub Pages (с ветки main): https://ShaunDier.github.io/pr2/
- автоматически сливает pull request из development и release в main, если тесты прошли.

Релизы публикуются по тегам vX.Y.Z на странице Releases.