# College project for Information Technology and Society course 

The page is available at [digitalk.herokuapp.com](https://digitalk.herokuapp.com/)


## Table of contents:
* [Project description](#project-description)
	* [Assignment](#assignment)
	* [Tech stack](#technology-stack)
* [Screenshots](#screenshots)
* [Running project locally](#running-the-project-locally)
* [License](#license)

---


## Project description:
**Topic:** Algorithms for speech recognition

### Assignment:
It involves creating a website in one of the content management systems (CMS). The use of Wordpress or Django is recommended, but not required. The content of the website should be directly related to the chosen topic.   

</br>

**Functionalities and features of the site:**
- [x] simple and modern design
- [x] responsive design
- [x] design of graphic elements
- [x] sending queries/emails
- [x] user registration
- [x] publishing content
- [x] content editing and categorization
- [x] sharing content on social media
- [x] posting comments
- [x] voice assistant


</br>

**Key features of the Alan AI voice assistant are::**
-   **Voice dialing**
	> Hey | Hello Alan
-   **Page Information**
	> Who is the creator of this site | Tell me something about Digi Talk
-   **Page navigation**
	> open `page name`  
	home | about | blog | contact | careers | registration page

</br>

### Technology stack:
<p>
<img src="https://img.shields.io/badge/Django%20-%23092e20.svg?&style=for-the-badge&logo=django&logoColor=white"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/python%20-%234b8bbe.svg?&style=for-the-badge&logo=python&logoColor=ffd43b"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/javascript%20-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/html5%20-%23e34f26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/CSS3-1572B6?&style=for-the-badge&logo=css3&logoColor=white"/>
</p>

**A tool used to create graphic elements - [Canva](https://www.canva.com/)**   
**More about voice assistant ***Alan AI*** you can find at [alan.app](https://alan.app/)**  
**Hosting: [Heroku](https://www.heroku.com/home)**  

---

## Screenshots: 
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="1604" alt="screenshot of desktop view 1 - home page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/desktop01.png"> | <img width="1604" alt="screenshot of desktop view 2 - blog page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/desktop02.png"> | <img width="1604" alt="screenshot of desktop view 3 - login page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/desktop03.png">|
|<img width="1604" alt="screenshot of mobile view 1 - about us page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/mobile01.jpg"> | <img width="1604" alt="screenshot of mobile view 2 - careers page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/mobile02.jpg"> | <img width="1604" alt="screenshot of mobile view 3 - nav menu" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/mobile03.jpg">|

---

## Running the Project Locally

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

To create virtual environment use `venv` command:
```bash
py -m venv env
```
here we creates a virtual environment in a folder named *env*, but you can specify any name for the folder.

Now activate the virtual environment with:
```bash
.\env\Scripts\activate
```

To install Django and all necessary requirements, run the following command:
```bash
pip install -r requirements.txt
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
---
## License
The project is released under the [MIT License](https://github.com/vladocodes/PMF-ITAS-project/blob/master/LICENSE).
