
## Cloud_Infrastructure Labs

Bei Collaboration möglichst auf/mit Branches arbeiten ;)
Vorschlag für Branchnames dieses Projekts: 
- {aktuelle Abschnitt}{init}
- {aktuelle Abschnitt}{korrektur}

Chlini Hilf und Gedankestützi für die Ahnigslose Motherfuckers:
## Tutorials
- Interaktives Gittutorial (SE Übungen): http://pcottle.github.io/learnGitBranching/
- Tutorial Git in Kombination mit Latex: https://de.sharelatex.com/blog/2012/10/16/collaborating-with-latex-and-git.html
- Eifach und übersichtlich: https://www.atlassian.com/git/tutorials/

##Einrichtung
Git initialisiern:
```bash
$ git init
```

Remote hinzufügen:
```bash
$ git remote add origin https://github.com/xxxx.git
```

###Save Login
Speicher Login im Klartext auf Lokalem Datenträger:
```bash
$ git config credential.helper store
```

## Befehle
###Branch
Naming wenn möglich Feature spezifisch
```bash
$ git branch dildo-vibration-hardcore
```

###Dateien hinzufügen
Jede Datei einzeln mit:
```bash
$ git filename
```

Alle Dateien:
```bash
$ git add .
```

Nicht zu empfehlen ausser es besteht ein .gitignore file
- Bsp. .gitignore file for LaTeX projects https://gist.github.com/kogakure/149016


###Commit
```bash
$ git commit -a -m "text"
```

###Zurücksetzen
relativ mittels HEAD~x:
```bash
$ git reset HEAD~1
```
oder über Hash:
```bash
$ git reset xxxxxxx
```

###Repository neu ziehen
```bash
$ git fetch --all 
$ git reset --hard HEAD
```




     
