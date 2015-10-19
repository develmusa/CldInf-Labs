
## Cloud_Infrastructure Labs

### Gio, you're [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Bei Collaboration möglichst auf/mit Branches arbeiten ;)  
Vorschlag für Branchnames dieses Projekts: 
- {aktuelle Abschnitt}{init}
- {aktuelle Abschnitt}{korrektur}

## Index
- [Tutorials](#tutorials)
- [Einrichtung](#einrichtung)
- [Befehle](befehle)
	- [Branch](#branch)
	- [Merge](#merge)
	- [Add (Dateien hinzufügen)](#add-(dateien-hinzufügen))
	- [Commit](#commit)
	- [Push](#push)
	- [Pull](#pull)
	- [Reset (Zurücksetzten)](#reset-(zurücksetzten))
	- [Nützliches](#nützliches)



## Tutorials
Chlini Hilf und Gedankestützi für die ahnigslose Motherfuckers:
- Interaktives Gittutorial (SE Übungen): http://pcottle.github.io/learnGitBranching/
- Tutorial Git in Kombination mit Latex: https://de.sharelatex.com/blog/2012/10/16/collaborating-with-latex-and-git.html
- Eifach und übersichtlich: https://www.atlassian.com/git/tutorials/
- GitHub Cheat Sheet: https://github.com/tiimgreen/github-cheat-sheet

##Einrichtung
Git initialisiern:
```bash
$ git init
```

Remote hinzufügen:
```bash
$ git remote add origin https://github.com/xxxx.git
```

Save Login
Speicher Login im Klartext auf Lokalem Datenträger:
```bash
$ git config credential.helper store
```

## Befehle
###Branch
Erstellen:  
Naming wenn möglich Feature spezifisch
```bash
$ git branch dildo-vibration-hardcore
```

Wechseln
```bash
$ git checkout newBranch
```

###Merge 
Beispiel um Branch in Master zu mergen:
```bash
$ git checkout master
$ git merge branch
```

###Add (Dateien hinzufügen)
Jede Datei einzeln mit:
```bash
$ git add filename
```

Alle Dateien:
```bash
$ git add .
```

Nicht zu empfehlen ausser es besteht ein .gitignore file im root directory
- Bsp. .gitignore file for LaTeX projects https://gist.github.com/kogakure/149016

###Commit
```bash
$ git commit -a -m "text"
```

###Push
```bash
$ git push -u origin "source/branch"
```

###Pull
```bash
$ git pull origin "source/branch"
```

###Reset (Zurücksetzen)

relativ mittels HEAD~x:
```bash
$ git reset HEAD~1
```
oder über Hash:
```bash
$ git reset xxxxxxx
```

###Nützliches
####Repository neu ziehen
"Fuck was funkt nüm" Plan:
```bash
$ git fetch --all 
$ git reset --hard HEAD
```

####Tracked Files
```bash
$ git ls-files
```

####Git Log
Mit dem x kann man die Anzahl Commits definieren.
```bash
$ git log -x
```
     
