# DiagramConstructionSystem

Для того, чтобы заполнить db.sqlite3 данными необходимо после клонирования репозитория выполнить следующее:

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py loaddata initial.json