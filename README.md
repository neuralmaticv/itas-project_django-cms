# Projekat za predmet Informacione tehnologije i društvo

Stranica je dostupna na [digitalk.herokuapp.com](https://digitalk.herokuapp.com/)
<!-- Read this guide in [English](https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/README.en.md). -->


## Sadržaj:
* [Zadatak](#zadatak)
	* [Opis projekta](#opis-projekta)
	* [Tehnologije i  alati](#korištene-tehnologije-i-alati)
* [Screenshots](#screenshots)
* [Pokretanje](#pokretanje-projekta-lokalno)
* [Licenca](#licenca)

---


## Zadatak:
Podrazumijeva izradu web sajta u nekom od sistema za upravljanje sadržajem (CMS). Preporučena je, ali ne i obavezna, upotreba Wordpress-a ili Django sistema. Sadržaj web sajta treba da bude u direktnoj vezi sa izabranom temom.  

### Opis projekta:
**Tema projekta:** Algoritmi za prepoznavanje govora

**Funkcionalnosti i osobine sajta:**  
- [x] jednostavan i moderan dizajn
- [x] dizajn prilagođen veličini uređaja
- [x] dizajn grafičkih ele
- [x] slanje upita/mail-ova
- [x] registracija korisnika
- [x] objavljivanje sadržaja
- [x] uređivanje i kategorizacija sadržaja
- [x] dijeljenje sadržaja na društvenim mrežama
- [x] komentarisanje sadržaja
- [x] glasovni asistent

  
**Osnovne funkcionalnosti glasovnog asistenta Alan AI:**
-   **Glasovno pozivanje**
	> Hey | Hello Alan
-   **Informacije o stranici**
	> Who is the creator of this site | Tell me something about Digi Talk
-   **Navigacija po stranici**
	> open `naziv stranice`  
	home | about | blog | contact | careers | registration page

### Korištene tehnologije i alati:
<p>
<img src="https://img.shields.io/badge/Django%20-%23092e20.svg?&style=for-the-badge&logo=django&logoColor=white"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/python%20-%234b8bbe.svg?&style=for-the-badge&logo=python&logoColor=ffd43b"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/javascript%20-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/html5%20-%23e34f26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/CSS3-1572B6?&style=for-the-badge&logo=css3&logoColor=white"/>
</p>

**Alat korišten pri izradi grafičkih elemenata - [Canva](https://www.canva.com/)**   
**Više o glasovnom asistentu ***Alan AI*** možete pronaći na [alan.app](https://alan.app/)**  
**Hosting: [Heroku](https://www.heroku.com/home)**  

---

## Screenshots: 
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="1604" alt="screenshot of desktop view 1 - home page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/desktop01.png"> | <img width="1604" alt="screenshot of desktop view 2 - blog page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/desktop02.png"> | <img width="1604" alt="screenshot of desktop view 3 - login page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/desktop03.png">|
|<img width="1604" alt="screenshot of mobile view 1 - about us page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/mobile01.jpg"> | <img width="1604" alt="screenshot of mobile view 2 - careers page" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/mobile02.jpg"> | <img width="1604" alt="screenshot of mobile view 3 - nav menu" src="https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/static/images/mobile03.jpg">|

---

## Pokretanje projekta lokalno

Prvo, klonirajte ovaj repozitorijum na vasu lokalnu masinu pomoću komande:

```bash
git clone https://github.com/vladocodes/PMF_ITAS_CMS
```

Ukoliko nemate instaliran Python preuzmite posljednju verziju sa [Python sajta](https://www.python.org/downloads/windows/) i instalirajte je

Uvjerite se da imate instaliranu noviju verziju (Python 3.x.x) pomoću komande:

```bash
py --version
```

Uvjerite se da imate i najnoviju verziju pip-a pomoću komande:

```bash
py -m pip --version
```

Kreirajte virtuelno okruzenje:

```bash
py -m venv env
```

Da aktivirate virtuelno okruzenje pozicionirajte se u direktorijum Scripts i unesite:
```bash
activate
```

Instalirajte Django:

```bash
pip install -r local_requirements.txt
```

Primjenite potrebne migracije:

```bash
py manage.py migrate
```

Pokrenite lokalni web server:

```bash
py manage.py runserver
```

Projekat je dostupan na http://localhost:8000/

Da obustavite rad servera unesite `CTRL + BREAK`

Za deaktiviranje virtuelnog okruzenja unesite:

```bash
deactivate
```
---
## Licenca
Ovaj projekat se nalazi pod [MIT licencom](https://github.com/vladocodes/PMF-ITAS-project/blob/master/LICENSE).  
