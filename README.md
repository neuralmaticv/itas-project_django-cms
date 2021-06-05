# Projekat za predmet Informacione tehnologije i drustvo

Read this guide in [English](https://github.com/vladocodes/PMF_ITAS_CMS/blob/master/README.en.md).


# Pokretanje projekta lokalno

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
pip install -r requirements.txt
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

# Licenca
Ovaj projekat se nalazi pod [MIT licencom](https://github.com/vladocodes/PMF-ITAS-project/blob/master/LICENSE).  
