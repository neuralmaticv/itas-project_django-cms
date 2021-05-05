# College project for Information Technology and Society course 

# Running the Project Locally

First, to clone the repository to your local machine, run the following command:
```bash
git clone https://github.com/vladocodes/PMF_ITAS_CMS
```

If you don't have Python download the installers for the latest versions of Python from the [Python website](https://www.python.org/downloads/windows/)

To verify the version of Python that is available (everything above Python 3 is ok), run the following command:
```bash
py --version
```

To verify the version of pip that is available, run the following command:
```bash
py -m pip --version
```

To install Django and all necessary requirements, run the following command:
```bash
pip install -r requirements.txt
```

To create virtual environment use `venv` command:
```bash
py -m venv env
```
here we creates a virtual environment in a folder named *env*, but you can specify any name for the folder.

Now activate the virtual environment with:
```bash
.\env\Scripts\activate
```

To set up your models, run the Django migrations with the following command:
```bash
py manage.py migrate
```

Run the development server:
```bash
py manage.py runserver
```

The project will be available at http://localhost:8000/

To quit the local web server press `CTRL + BREAK`.

If you want to stop using the virtual environment and go back to your global Python, run the following command:
```bash
deactivate
```

# License
The project is released under the [MIT License].(https://github.com/vladocodes/PMF-ITAS-project/blob/master/LICENSE).
