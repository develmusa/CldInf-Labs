
## Cloud_Infrastructure Labs

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


     
