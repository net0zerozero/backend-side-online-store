# backend side online store

Frontend side of this project - [Frontend](https://github.com/net0zerozero/Frontend-side-of-the-online-store)

Backend Side of the Online Store
This is the backend side of the online store project. It uses Django and Django REST Framework (DRF) to provide the necessary APIs for the online store.

## Prerequisites
Before you start using the project, make sure you have the following prerequisites installed:

Python 3.10: You can download Python from the official website: python.org

## Installation

Clone the repository from GitHub:

```sh
git clone https://github.com/net0zerozero/backend-side-online-store.git
```

Navigate to the project directory:

```sh
cd backend-side-online-store
```

Create a virtual environment (optional but recommended):

```sh
python -m venv venv
```

Activate the virtual environment:

For Windows:

```sh
venv\Scripts\activate
```

For Unix or Linux:

```sh
source venv/bin/activate
```

Install the required dependencies:

```sh
poetry install
```
This will install all the dependencies specified in the pyproject.toml file using Poetry.

Generate the requirements.txt file:

```sh
poetry export --output requirements.txt --without-hashes
```
This command will generate the requirements.txt file based on the installed dependencies. It's useful if you want to deploy the project in an environment that doesn't use Poetry.



## Starting the Development Server

To start the development server, run the following command:

```sh
python manage.py runserver
```

The development server will start running at http://localhost:8000.

