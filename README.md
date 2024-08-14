# DishDesign

## A Django-based Recipe Web Application

## Introduction

DishDesign is a web application built using the Django framework that allows users to create, manage, and search recipes. This project was developed as part of an achievement in a Python for Web Developers course.

## Features

The key features of the DishDesign application include:

1. **User Authentication**: Users can log in and log out of the application.
2. **Recipe Management**: Users can create, read, update, and delete recipes. Each recipe contains information such as ingredients, cooking time, and difficulty level, etc.
3. **Recipe Search**: Users can search for recipes based on their desired ingredients.
4. **Admin Dashboard**: An admin panel is provided for managing the application's database, including recipes and user accounts.
5. **Data Visualization**: The application includes an analytics dashboard that provides visualizations of site statistics, such as the most commonly searched recipes, calorie content, and ingredient distribution.

## Technologies Used

The DishDesign application is built using the following technologies:

- **Python 3.6+**
- **Django 3.x**
- **MySQL/SQLite Database**
- **HTML, CSS, and JavaScript** for the user interface
- **Matplotlib** and **Pandas** for data visualization

## Getting Started

To get started with the DishDesign application, follow these steps:

1. **Clone the repository**: `git clone https://github.com/ffferchavez/recipe-app.git`
2. **Create a virtual environment**: `python -m venv venv`
3. **Activate the virtual environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. **Install the required packages**: `pip install -r requirements.txt`
5. **Create a MySQL/SQLite database and update the settings.py file with the database credentials**
6. **Apply the database migrations**: `python manage.py migrate`
7. **Create a superuser account**: `python manage.py createsuperuser`
8. **Start the development server**: `python manage.py runserver`
9. **Access the application in your web browser**: `http://127.0.0.1:8000/`

You can also use the following test user credentials to log in:

- Username: `test`
- Password: `user1234`

## Deployment

To deploy the DishDesign application, you can use a cloud hosting platform like Heroku or PythonAnywhere. The application is configured to use a PostgreSQL database in production.

## Contributing

If you would like to contribute to the DishDesign project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your branch to your forked repository
5. Create a pull request to the main repository

## License

This project is licensed under the [MIT License](LICENSE).
