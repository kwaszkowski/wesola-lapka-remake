# Getting started

1. Install Python 3.13+
2. Install Poetry:
   ```curl -sSL https://install.python-poetry.org | python3 -```
3. Download project:
   ```git clone git@github.com:kwaszkowski/wesola-lapka-remake.git```
   ```cd wesola-lapka-remake```
4. Install dependencies:
   ```poetry install```
5. Make migration (database creation):
   ```poetry run python manage.py migrate```
6. Run livereload:
   ```poetry run python manage.py livereload```
7. Run django server:
   ```poetry run python manage.py runserver```
8. Open browser:
   ```http://localhost:8000```

## The inspiration for the website was a person that needed a website similar to wesolalapka.pl
