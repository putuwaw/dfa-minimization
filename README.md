# DFA-MINIMIZATION

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Forks](https://img.shields.io/github/forks/putuwaw/dfa-minimization?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/putuwaw/dfa-minimization?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/putuwaw/dfa-minimization?style=for-the-badge)

DFA-Minimization is a website to minimize DFA using Table Filling Method.

## Features💡
By using DFA-Minimization you can:
- [x] Minimize DFA using Table Filling Method.
- [x] Get description (transition diagram, transition table, and detailed description) of DFA before minimization.
- [x] Get description (transition diagram, transition table, and detailed description) of DFA after minimization.



## Technology 👨‍💻
DFA-Minimization is created using:
- [Python](https://www.python.org/) - 
Python as the main programming language.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Flask is a web framework for Python, based on the Werkzeug toolkit.
- [PyScript](https://pyscript.net/) - PyScript is a framework that allows to create rich Python applications in the browser.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework that allows for the creation of easy and responsive web layouts.
- [Heroku](https://www.heroku.com/) - Heroku is a platform as a service (PaaS) that we use to deploy our apps.
- [Docker](https://www.docker.com/) - Docker is a platform for developing, shipping, and running our applications.


## Structure 📂
```
DFA-Minimization
├── .github
├── handlers
├── docs
├── modules
├── static
│   ├── images
│   ├── scripts
│   └── styles
├── templates
├── tests
├── .gitignore
├── Dockerfile
├── LICENSE
├── Procfile
├── README.md
├── app.py
└── requirements.txt
```
- [.github](.github/) is a folder that used to place Github related stuff, like issue template and CI pipeline.
- [handlers](handlers/) contain handler to handling HTTP request methods, especially POST method.
- [docs](docs/) contain documentation of this app.
- [modules](modules/) contain the main modules for minimizing DFA using Table Filling Method.
- [static](static/) contain static files like images, CSS, and JavaScript files.
- [templates](templates/) contain the file that will be rendered for display in the browser.
- [tests](tests/) contain unit test to make sure the main module work properly.
- [.gitignore](.gitignore) is a file to exclude some folders like venv.
- [LICENSE](LICENSE) is a file that contains the license we use in this app.
- [Dockerfile](Dockerfile) is a file that contains all the commands to build an image.
- [Procfile](Procfile) is a file that specifies the commands that are executed by an Heroku app on startup.
- [README.md](README.md) is the file you are reading now.
- [app.py](app.py) is the main file of this app.
- [requirements.txt](requirements.txt) is a file that contains a list of dependencies used in this app.

## Requirements 📦
- Python 3.10 or later
- Docker 20.10.17 or later
- PyScript 2022.09.1 or later

## Installation 🛠️
- Install Docker.
- Pull the image from [Docker Hub](https://hub.docker.com/r/putuwaw/dfa-minimization):
```
docker pull putuwaw/dfa-minimization
```
- Run the downloaded image:
```
docker run -p 8000:8000 putuwaw/dfa-minimization
```
- Open web browser and visit:
```
localhost:8000
```

## Contributors ✨
<br>
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/putuwaw"><img src="https://avatars.githubusercontent.com/u/90038606?v=4" width="150px;" alt=""/><br><sub><b>Putu Widyantara</b></sub></td> 
    <td align="center"><a href="https://github.com/KEVINMOSESWALELENG"><img src="https://avatars.githubusercontent.com/u/103045275?v=4" width="150px;" alt=""/><br><sub><b>Kevin Moses</b></sub></td> 
    <td align="center"><a href="https://github.com/Antoniusata12"><img src="https://avatars.githubusercontent.com/u/113809833?v=4" width="150px;" alt=""/><br><sub><b>Antonius Ata</b></sub></td>
    <td align="center"><a href="https://github.com/YogaLaksana"><img src="https://avatars.githubusercontent.com/u/103047470?v=4" width="150px;" alt=""/><br><sub><b>Yoga Laksana</b></sub></td>
  </tr>
</table>