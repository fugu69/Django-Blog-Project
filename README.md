# Django Blog Project

## Description
This is a **Django-based blog application** built following Corey Schafer's tutorial series. It includes **user authentication**, **profile management**, **post creation**, and other essential blogging features. The project is designed to help developers understand Django's core functionalities while building a practical web application.

## Features
- **User authentication** (Login, Logout, Registration)
- **Profile management** with user avatars
- **Create, update, and delete blog posts**
- **Pagination** for post listings
- **Password reset functionality**
- **Responsive design** using Bootstrap

## Technologies Used
- Python 3.x
- Django Framework
- Bootstrap for styling
- SQLite (default database)
- Pillow (for image handling)
- Crispy Forms (for better form styling)

## Installation & Usage
1. Clone the repository:
	git clone https://github.com/yourusername/django-blog.git
	
2. Navigate to the project directory:
	cd django-blog

3. Create a virtual environment and activate it:
	python -m venv env
	source env/bin/activate  # On Windows: env\Scripts\activate

4. Install dependencies:
	pip install -r requirements.txt

5. Apply migrations:
	python manage.py migrate

6. Create a superuser:
	python manage.py createsuperuser

7. Run the development server:
	python manage.py runserver

8. Open http://127.0.0.1:8000/ in your browser to explore the blog.

## Author
- Corey Schafer (Original tutorial)
- Maximus Brutalis implementation

## License
This project follows Corey Schafer’s tutorial but can be modified and extended freely.
