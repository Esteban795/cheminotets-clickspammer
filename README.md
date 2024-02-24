# cheminotets-clickspammer
Bot to spam click and be the first to get logged inside the enrollment platform.


# Requirements
- Python (3.10+, mais ça devrait marcher avec moins quand même..)
- pip

# Installation
- Clonez le repo, ou téléchargez le zip. Extraire les données du zip.
- Ouvrez vscode et mettez vous dans le bon dossier.
- Lancez le terminal et tapez : 

```txt
python -m venv .env
```
- Ensuite, tapez  : 
```txt
./.env/Scripts/activate
```
Si jamais windows fait chier en disant "il faut activer l'exécution des scripts, faire ceci : 
- Ouvrez powershell en mode admin
- Tapez : 
```txt
Set-ExecutionPolicy -ExecutionPolicy AllSigned
```
- Tapez "O" quand il vous demande de confirmer.

- Retour au projet en lui-même. Dans le terminal VSCode, tapez (une fois après avoir refait `./.env/Scripts/|activate`) : 
```txt
pip install -r requirements.txt
```

- Lancez la fenêtre de cheminot.
- Entrez vos identifiants.
- Lancez ce script en tapant : 
```py
python src/main.py
```
- Toutes les secondes, ça devrait cliquer sur le bouton (c'est dieu qui donne).