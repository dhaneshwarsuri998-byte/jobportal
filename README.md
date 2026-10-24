 Job Portal – Django Project

## Overview

This is a **Job Portal Web Application** built using the Django framework.
The system allows students to search for jobs and recruiters to post job openings.
An admin panel is used to manage recruiters and users.

The project demonstrates Django authentication, database management, and CRUD operations.

---

## Features

### Admin

* Admin login
* View registered students
* View all recruiters
* Accept or reject recruiter registrations
* Delete users and recruiters
* Manage the system

### Recruiter

* Recruiter signup
* Recruiter login
* Add job postings
* Edit job details
* View jobs posted by recruiter

### Student/User

* User signup
* User login
* View latest job listings
* View job details

---

## Technologies Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite Database

---

## Project Structure

```
jobportal/
│
├── job/                    # Django app
│   ├── models.py
│   ├── views.py
│   ├── templates/
│
├── jobportal/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── media/                  # Uploaded images
├── manage.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## Installation Steps

1. Clone the repository

```
git clone https://github.com/yourusername/jobportal.git
```

2. Move into the project folder

```
cd jobportal
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Apply migrations

```
python manage.py migrate
```

5. Run the development server

```
python manage.py runserver
```

6. Open the project in your browser

```
http://127.0.0.1:8000/
```

---

## Database

The project uses **SQLite** as the default database.

---

## Author

Developed by **Dhaneshwar Suri**
