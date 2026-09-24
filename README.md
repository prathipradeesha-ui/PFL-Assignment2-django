# ProjectHub - Django

ProjectHub is a student project blog developed as part of the Programming Frameworks & Languages (PFL) Assessment 2.

The application provides a platform for Software Engineering students to share their final-year project ideas, experiences, and information.

## Framework

- **Framework:** Django
- **Language:** Python
- **Database:** SQLite
- **Frontend:** Django Templates, HTML, CSS
- **Testing:** Django Automated Testing Framework

## Features

The Django implementation includes the following features:

- View the latest three blog posts
- Create a new blog post
- View individual blog posts
- Edit existing blog posts
- Delete blog posts
- Search blog posts
- Filter posts by category
- Sort posts by:
  - Newest
  - Oldest
  - Title A-Z
- Add cover images using image URLs
- Persistent data storage using SQLite
- Responsive user interface

## Blog Post Fields

Each blog post contains:

- Title
- Author
- Category
- Content
- Cover Image URL
- Created Date and Time

## Search

Search is implemented as the common additional feature for the ProjectHub implementations.

Users can search across:

- Post titles
- Authors
- Categories
- Post content

The search results are displayed on the homepage.

## Category Filtering

Users can select a category from the category dropdown to display posts belonging to that category.

## Sorting

Posts can be sorted using:

- **Newest** - displays the most recently created posts first
- **Oldest** - displays the oldest posts first
- **Title A-Z** - sorts posts alphabetically by title

## Cover Images

Posts can include a cover image using a direct image URL.

The cover image is displayed on the post card when a valid image URL is provided.

## Project Structure

```text
PFL-Assignment2-django/
│
├── blog/
│   ├── migrations/
│   ├── static/
│   │   └── blog/
│   │       └── style.css
│   ├── templates/
│   │   └── blog/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
