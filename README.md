
<h1 style="color:white; font-weight:bold;">ZenPlay - Django Project Setup Guide</h1>

Welcome to **ZenPlay**, a Django-based project! This guide outlines how to set up and run the project on a Windows machine.

---

## Prerequisites

Before setting up ZenPlay, ensure you have the following installed:

1. **Python 3.7+**  
   [Download Python](https://www.python.org/downloads/)

2. **Pip** (Python's package manager)  
   Check if pip is installed:
   ```cmd
   pip --version
   ```

3. **Git** (for cloning the repository)  
   [Download Git](https://git-scm.com/)

4. **Virtualenv** (optional but recommended)  
   Install it globally:
   ```cmd
   pip install virtualenv
   ```

---

## Installation Steps

### Step 1: Clone the Repository
Clone the ZenPlay repository from GitHub:
```cmd
git clone https://github.com/silomaben/zenplay.git
```

Navigate into the project directory:
```cmd
cd zenplay
```

### Step 2: Set Up a Virtual Environment
Create a virtual environment:
```cmd
python -m venv venv
```

Activate the virtual environment:
```cmd
venv\Scriptsctivate
```

### Step 3: Install Dependencies
Install the required Python packages:
```cmd
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
Run the following commands to prepare the database:
```cmd
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Development Server
Start the Django development server:
```cmd
python manage.py runserver
```

Visit the app in your browser at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Additional Commands

### Creating a Superuser
To create an admin account:
```cmd
python manage.py createsuperuser
```

### Collecting Static Files
If your project uses static files, collect them with:
```cmd
python manage.py collectstatic
```

---

Happy coding! 🚀
