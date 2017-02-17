#################################################
#################################################
## Jérôme ROUGET & Yoann BAUMERT               ##
## 17/02/2017                                  ##
## Projet Python                               ##
#################################################
#################################################

# Import

import sqlite3
import re
import csv

# Initialisations


# Utilisation des fichiers

BDD=sqlite3.connect('pas_ma_base.db')

# Création de la table

connexion=BDD.cursor()

connexion.execute("""
CREATE TABLE IF NOT EXISTS Personnels(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    NOM TEXT,
    FIFILLE TEXT,
    PRENOM TEXT,
    NAISSANCE TEXT,
    FONCTION TEXT,
    DEPARTEMENT TEXT,
    COURRIEL TEXT,
    TEL INT,
    MOBILE INT
)
""")


# Lecture et parsing

with open ("personnels.csv",newline="\n") as csvfile:
    reader=csv.reader(csvfile,delimiter=',',quotechar='"')
    lecteur=csv.DictReader(csvfile)

    for row in lecteur:
        connexion.execute('INSERT INTO Personnels(NOM,FIFILLE,PRENOM,NAISSANCE,FONCTION,DEPARTEMENT,COURRIEL,TEL,MOBILE) VALUES("'+row['NOM']+'","'+row['NOM de jeune fille']+'","'+row['Prénom']+'","'+row['Date de naissance']+'","'+row['Fonction']+'","'+row['Département']+'","'+row['Courriel']+'","'+row['Téléphone']+'","'+row['Mobile']+'")')

# Select

connexion.execute("SELECT * FROM Personnels")

osef=connexion.fetchall()
print(osef)

BDD.commit()
░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
█░▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█░▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█░░░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░█░░░▀▀▄░█░░░█░███████░█
░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░█▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░█░░░░▀▄▄▄▄▄▄▄▄▄▄█
░░░░░░░░█░░░░░░░░█░░░░░░
░░░░░░░▄██▄░░▀▀░▄█▀▄░░░░
░░░░░▄▀░▀▄▀▀███▀▀▄▀░▀▄░░
░░░░░█░░░░▀▄▀░▀▄▀░▄░░█░░
░░░░░█░█░░░█░░░█░░█░░█░░
░░░░░█░█░░░░▀▄▀▀▀▀█░░█░░
░░░░░█░█░░░░░▄░░▄██▄▄▀░░
░░░░░█░█░░░░░▄░░████░░░░
░░░░░███▄░░░▄▄▄░░░▄▀░░░░
░░░░░░▀▀█▀▀▀░▄░▀▀▀█░░░░░
░░░░░░░░█░░░░█░░░░█░░░░░
