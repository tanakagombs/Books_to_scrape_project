# P2 - DA Python - Utilisez les bases de Python pour l'analyse de marché

## Description
This is a script to scrape the website: 
 "https://books.toscrape.com/index.html"

 This program ,from the website link and will go through all the book categories on the site.For every category it will go and scrape all the info of all the books  "upc code, price , reviews etc ".For each book category (eg Poetry) a csv file with the coresponding name "Poetry.csv" will be created and the information for all the books in this category will be stored in this csv file.
All the book images will also be downloaded to a file path specified ,in my case " "


# Get the project :
`git clone https://github.com/tanakagombs/Books_to_scrape_project.git`

## Create a virtual environment

*Installation*

*Begin by installing VirtualEnv, command is :*

*```pip install virtualenv```*

Make sure you have python installed and access to your terminal,via the command line.
do this by typing `python` in the terminal for windows  and `python3` on Mac/Unix,
if it is installed , the python version will be displayed 

If that's not the case go to : https://www.python.org/downloads/
and download and install python corresponding to your operating system (Windows,Linux/Unix or macOS).

### To create a virtual environment 

Begin by creating a virtual environment with the command :

```virtualenv -p python3 env```

*On Windows the command is*

```virtualenv -p $env:python3 env```

To activate the environment,type the following command :

```source venv/bin/activate```

*In Powershel the commannd is :* 

```./env/scripts/activate.ps1```

to install dependencies:

```pip install -r requirements.txt```

## Exécuter le scraper

`python main.py`









