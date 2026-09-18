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
