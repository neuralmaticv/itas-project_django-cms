# Tema: Algoritmi za prepoznavanje govora | Topic: Algorithms for Speech Recognition
Projekat za predmet Informacione tehnologije i drustvo, College project for Information Technology and Society course 

Prvo, klonirajte ovaj repozitorijum na vasu lokalnu masinu

```bash
git clone https://github.com/vladocodes/PMF_ITAS_CMS
```

Ukoliko nemate instaliran Python preuzmite posljednju verziju sa [Python sajta](https://www.python.org/downloads/windows/) i instalirajte je

Uvjerite se da imate instaliranu noviju verziju (Python 3.x.x)

```bash
py --version
```

Uvjerite se da imate i najnoviju verziju pip-a

```bash
py -m pip --version
```

Instalirajte Django

```bash
pip install -r requirements.txt
```

Kreirajte virtuelno okruzenje

```bash
py -m venv env
```

Da aktivirate virtuelno okruzenje pozicionirajte se u direktorijum Scripts i unesite 
```bash
activate
```

Primjenite potrebne migracije

```bash
py manage.py migrate
```

Pokrenite server

```bash
py manage.py runserver
```

Projekat je dostupan na http://localhost:8000/

Da obustavite rad servera unesite CTRL + BREAK

Za deaktiviranje virtuelnog okruzenja unesite

```bash
deactivate
```

# Licenca | License
Ovaj kod se nalazi pod [MIT licencom].(https://github.com/vladocodes/PMF-ITAS-project/blob/master/LICENSE).  
The source code is released under the [MIT License].(https://github.com/vladocodes/PMF-ITAS-project/blob/master/LICENSE).
