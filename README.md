# Business Website

A small business website built with Django.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the homepage. Replace the starter business name, copy, contact address, and image with details for your project.