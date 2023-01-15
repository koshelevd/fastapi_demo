1. Установить Docker
2. Склонировать репозиторий
3. Переименовать файл .env.example в .env
4. Запустить команду `docker-compose up -d`
5. Создать виртуальное окружение `python -m venv venv`
6. Активировать виртуальное окружение `source venv/Scripts/activate`
7. Установить зависимости `pip install -r requirements.txt`
8. Перейти в папку `cd src`
8. Создать миграции (если не созданы) `alembic revision --autogenerate -m 01_initial-db`
9. Запустить миграции `alembic upgrade head`
10. Запустить сервер `uvicorn main:app --reload`
