# P2 - DA Python - Utilisez les bases de Python pour l'analyse de marché

## Description
This is a script to scrape the website: 
 "https://books.toscrape.com/index.html"

 This program ,from the website link and will go through all the book categories on the site.For every category it will go and scrape all the info of all the books  "upc code, price , reviews etc ".For each book category (eg Poetry) a csv file with the coresponding name "Poetry.csv" will be created and the information for all the books in this category will be stored in this csv file.
All the book images will also be downloaded to a file path specified ,in my case " "


# Récupérer le projet :
`git clone https://github.com/tanakagombs/Books_to_scrape_project.git`

## Création de l'environnement virtuel
Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.
do this by typing `python` in the terminal for windows  and `python3` on mac,
if it is installed , the python version will be displayed 

Si ce n'est pas le cas go to : https://www.python.org/downloads/
and download and install python corresponding to your operating system (Windows,Linux/Unix or macOS).

### To create a virtual environment 

`python -m venv NOM_ENVIRONNEMENT`

## Activation de l'environnement virtuel du projet

`pip install -r requirements.txt`

## Exécuter le scraper

`python main.py`









