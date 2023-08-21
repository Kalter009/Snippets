# Snippets_2108
## Инструкция по развертыванию проекта

1. `python3 -m venv venv_name` - создание venv
2. `source venv_name/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`

## Запуск терминала в контексте django
`python manage.py shell_plus --ipython`