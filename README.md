# Django Job Portal Web Application (NSDA Level-4)

A multi-user Job Portal web application built with Python and Django according to the NSDA Level-4 Web Application Development specifications[cite: 1]. This application connects recruiters and jobseekers across various domains, enabling job postings, application tracking, skill-matched dashboards, and custom user profile management[cite: 1].

---

## Features

### Multi-User Authentication & Roles
* Dual-User System: Supports distinct user roles for Recruiters and Jobseekers[cite: 1].
* Registration & Login: Secure authentication handling usernames, passwords, display names, email addresses, and user types[cite: 1].

### Recruiter Capabilities
* Profile Management: Set up and manage company information and recruiter details[cite: 1].
* Job Postings: Create and publish openings with parameters for Title, Number of Openings, Category, Skills Required, and Job Description[cite: 1].
* Application Tracking: Monitor candidate submissions across key recruitment statuses (Total Posted, Total Applications, Pending, Shortlisted, and Rejected).

### Jobseeker Capabilities
* Profile & Resume Upload: Manage skillset profiles and upload CV/Resume files[cite: 1].
* Job Search & Discovery: Browse and apply for open job postings tailored to user skills[cite: 1].
* Applied Job History: Track application statuses in real time.

### Dashboard & Skill Matching
* Interactive dashboard with real-time metric cards for recruitment and application insights[cite: 1].
* Skill-matching logic connecting candidate skill sets with recruiter job criteria[cite: 1].

---

## Project Directory Structure

JOB_PORTAL/
│
├── Job_App/                    # Main Django Application
│   ├── templates/              # HTML Templates
│   │   ├── base/               # Global Layouts (base.html, nav.html)
│   │   └── pages/              # Application Pages (dashboard.html, authform.html, baseform.html, etc.)
│   │
│   ├── static/                 # Static Assets
│   │   └── css/
│   │       └── style.css       # Custom Form, Card, and Navigation CSS
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                # Django Form Definitions
│   ├── models.py               # Database Schemas (User, Profile, Job, Application)
│   ├── urls.py                 # App Route Handlers
│   └── views.py                # Business Logic & Controllers
│
├── Job_Portal/                 # Project Configuration Directory
│   ├── settings.py             # Global Project Settings & Static Config
│   ├── urls.py                 # Root URL Dispatcher
│   ├── asgi.py
│   └── wsgi.py
│
├── .gitignore                  # Git Exclusion Rules
├── LICENSE                     # Project License
├── manage.py                   # Django CLI Utility
└── README.md                   # Documentation

---

## Tech Stack

* Backend Framework: Python / Django
* Frontend: HTML5, CSS3, Bootstrap 5
* Database: SQLite (Default / Development)[cite: 1]
* Templating Engine: Django Template Language (DTL)

---

## Quick Start & Setup Guide

### 1. Prerequisites
Ensure Python 3.10+ and Git are installed on your environment.

### 2. Clone the Repository
git clone https://github.com/your-username/Job-Portal.git
cd JOB_PORTAL

### 3. Create & Activate a Virtual Environment
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

### 4. Install Dependencies
pip install django

### 5. Configure Static & Media Settings (Job_Portal/settings.py)
Ensure settings.py includes static and media directory paths:

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'Job_App' / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

### 6. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

### 7. Create Superuser (Admin Access)
python manage.py createsuperuser

### 8. Run Development Server
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the portal.

---

## License

Developed for academic evaluation and certification purposes under the NSDA Level-4 Web Application Development (Python/Django) framework[cite: 1].
