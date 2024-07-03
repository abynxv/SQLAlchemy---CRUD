# SQLAlchemy-CRUD

This project implements a CRUD (Create, Read, Update, Delete) API for managing students and colleges using SQLAlchemy, a powerful ORM (Object-Relational Mapping) library for Python. 
The project provides endpoints to interact with a relational database, allowing users to perform operations such as creating, retrieving, updating, and deleting records for students and colleges.

# SQLAlchemy Project Configuration

a)File Structure

    sqlalchemy_config.py:
        Configuration file for SQLAlchemy setup.
        Contains functions to initialize the database session and engine.

    initialize_db.py:
        Script to initialize or migrate database schema.
        Sets up database tables and relationships.

b)Database Setup

    Database Engine:
        Configure SQLAlchemy engine to connect to the database.
        Specify database URL (sqlite:///example.db for SQLite, postgresql://username:password@localhost/dbname for PostgreSQL, etc.).

    Session Management:
        Use SQLAlchemy session for database interactions.
        Handle transactions and session lifecycle.

c)Project Structure

    Models:
        Define SQLAlchemy models (College, Student) with relationships (students = relationship("Student", back_populates="college")).

    Serializers:
        Use DRF serializers (CollegeSerializer, StudentSerializer) for API input/output validation.

d)Setup Instructions

    Installation:
        Clone the project and set up a virtual environment.
        Install dependencies from requirements.txt.

    Run the Project:
        Start the server (python manage.py runserver).
        Access API endpoints (/api/colleges/, /api/students/).

e)Database Migration

    Initialization:
        Run initialize_db.py to create database schema and tables.
        Ensure consistency across different databases (SQLite, PostgreSQL, etc.).


# Setup Instructions

  -> Create a directory, open cmd in directory path  and clone Vendor-Navigator project
  
      git clone https://github.com/abynxv/SQLAlchemy-CRUD.git

  -> Install Virtual environment
  
      pip install virtualenv

  -> Create virtual environment within the directory. 
  
      python -m venv venv_name  # On Windows
      python3 -m venv venv_name  # On macOS/Linux

  -> Activate virtual environmant    
  
      venv_name\Scripts\activate       # On Windows           
      source venv_name/bin/activate     # On macOS/Linux

  -> Install requirements.txt
  
      pip install -r requirements.txt

  -> Open Project in VScode
 
      code .

  -> Open terminal in vscode, navigate to project directory, Run the server and follow link

      cd sqlalchemy_project
      py manage.py runserver


# SQLAlchemy Project: API Endpoints

Colleges

1.List all Colleges

    Endpoint   : `/api/colleges/`
    Method     : GET
    Description: Retrieve details of all colleges.

2.Retrieve a College

    Endpoint   : `/api/colleges/{id}/`
    Method     : GET
    Description: Retrieve details of a specific college by ID.

3.Create a College

    Endpoint   : `/api/colleges/`
    Method     : POST
    Data       : JSON - `{"name": "string", "address": "string"}`
    Description: Create a new college.

4.Update a College

    Endpoint   :`/api/colleges/{id}/`
    Method     : PUT
    Data       : JSON - `{"name": "string", "address": "string"}`
    Description: Update details of a specific college.

5.Delete a College

    Endpoint   : `/api/colleges/{id}/`
    Method     : DELETE
    Description: Delete details of a specific college.

Students

1.List all Students

    Endpoint   : `/api/students/`
    Method     : GET
    Description: Retrieve details of all students.

2.Retrieve a Student

    Endpoint   : `/api/students/{id}/`
    Method     : GET
    Description: Retrieve details of a specific student by ID.

3.Create a Student

    Endpoint   : `/api/students/`
    Method     : POST
    Data       : JSON - `{"name": "string", "age": integer, "college_id": integer}`
    Description: Create a new student.

4.Update a Student

    Endpoint   : `/api/students/{id}/`
    Method     : PUT
    Data       : JSON - `{"name": "string", "age": integer, "college_id": integer}`
    Description: Update details of a specific student.

5.Delete a Student

    Endpoint   : `/api/students/{id}/`
    Method     : DELETE
    Description: Delete details of a specific student.
  
