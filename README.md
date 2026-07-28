# Coaching Management System

A full-stack **Coaching Institute Management System** built with:

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (Django Templates)
- **Database:** SQLite (default, easy to switch to MySQL/Postgres)

## Features

- Admin login/logout (secure session-based auth)
- Dashboard with live statistics (students, teachers, courses, batches, fees collected)
- Student management (add / edit / delete / list / photo upload)
- Teacher management (add / edit / delete / list)
- Course management (add / edit / delete / list)
- Batch management (add / edit / delete / list, linked to Course + Teacher)
- Attendance marking and history per student
- Fee payment tracking with receipts list
- Search & filter on student list
- Responsive UI with custom CSS (no external framework needed)
- Client-side validation & UX enhancements with JavaScript

## Project Structure

```
coaching_management_system/
├── manage.py
├── requirements.txt
├── README.md
├── coaching_management_system/     # Project settings package
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── coaching/                       # Main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
├── templates/                      # HTML templates
│   ├── base.html
│   ├── registration/
│   │   └── login.html
│   └── coaching/
│       ├── dashboard.html
│       ├── student_list.html
│       ├── student_form.html
│       ├── teacher_list.html
│       ├── teacher_form.html
│       ├── course_list.html
│       ├── course_form.html
│       ├── batch_list.html
│       ├── batch_form.html
│       ├── attendance_list.html
│       ├── attendance_form.html
│       ├── fee_list.html
│       ├── fee_form.html
│       └── confirm_delete.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── media/                          # Uploaded student photos
```

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create an admin (superuser) account:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser at `http://127.0.0.1:8000/` and log in with the
   superuser credentials you created.

## Notes

- Django's built-in admin panel is also available at `/admin/`.
- Media (student photos) are served from `/media/` in development.
- All CRUD screens are protected by login (`@login_required` / `LoginRequiredMixin`).
