from flask import Flask, render_template, request , url_for


app = Flask(__name__) 

@app.route('/') #page d'acceuil
def index():
    return render_template("index.html")
            
            
@app.route('/ajouter', methods = ['POST','GET'])
def ajouter():
    return render_template('ajouter.html')
        
@app.route('/resultat_ajouter', methods = ['POST','GET'])
def resultat_ajouter():
    if request.method == "POST": #action lorsqu'une requete est faite
        name = request.form #name est un dictionaire qui prend pour valeurs les reponses aux questions de la page html
        nom = name['nom']
        num = name['num']
        repertoire = open('repertoire.txt', 'a')
        repertoire.write('\n')
        repertoire.write(nom)
        repertoire.write('  :  ')
        repertoire.write(num)
        repertoire.close()
        resultat = 'Le nom et le numéro correspondant ont bien été ajoutés au répertoire.'
        return render_template('resultat_ajouter.html', resultat = resultat, nom = nom, num = num) #charge une nouvelle page html et retourne si le repertoire a ecrit le nouveau nom
    return render_template('resultat_ajouter.html')
        
@app.route('/supprimer', methods = ['POST','GET'])
def supprimer():
    return render_template('supprimer.html')


@app.route('/resultat_supprimer', methods = ['POST','GET'])
def resultat_supprimer():
    info = ''
    if request.method == "POST":
        name = request.form #le formulaire dans la page web
        nom = name['nom'] #le nom a supprimer
        num = name['numero']
        with open('repertoire.txt','r') as repertoire:
            lignes = repertoire.readlines() #transforme le repertoire en une liste separré a chaque saut de ligne
        trouve = False
        for i, line in enumerate(lignes):#pour chaque element dans la liste lignes
            if nom in line:
                if num in line:
                    lignes.remove(line)#supprime la ligne
                    trouve = True
        if trouve ==True :
            with open('repertoire.txt','w') as repertoire: #ouvre le fichier pour écrire
                for line in lignes:
                    repertoire.write(line)#reécrit le fichier sans les noms a supprimer
            resultat = 'Le nom et le numéro correspondant ont été supprimés avec succès.'
        else:
            resultat = 'Le nom ou le numéro demandé ne sont pas dans le répertoire.'
        repertoire.close()
        return render_template('resultat_supprimer.html', resultat = resultat,)
    return render_template('resultat_supprimer.html')  
          
  
@app.route('/recherche', methods = ['POST','GET'])
def recherche():
    return render_template('recherche.html') 
            
@app.route('/resultat_recherche', methods = ['POST','GET'])
def resultat_recherche():
    liste = []
    resultat = ""
    if request.method == "POST":
        nom = request.form
        nom_recherche = nom['nom']
        with open('repertoire.txt','r') as repertoire:
            lignes = repertoire.readlines() #transforme le fichier texte en une liste separré a chque saut de ligne
        trouve = False
        for i, line in enumerate(lignes):
            if nom_recherche in line:
                liste.append(line.replace('\n', '')) #ajoute la ligne avec le nom dans la liste
                trouve = True
        if trouve ==True :
            for i in range(len(liste)):
                resultat = resultat + liste[i] +'          ' #resultat designe la variable avec tous les noms ou numéros qui correspondent a la recherche
        else:
            resultat = 'Le nom ou le numéro recherché est introuvable.'
        repertoire.close()
        print(resultat)
        return render_template('resultat_recherche.html', nom = resultat)
    return render_template('resultat_recherche.html')

@app.route('/modifier', methods = ['POST', 'GET'])
def modifier():
    return render_template('modifier.html')


@app.route('/resultat_modifier', methods = ['POST', 'GET'])
def resultat_modifier():
    if request.method == 'POST':
         name = request.form
         nom = name['nom']
         num = name['numero']
         nouv_nom = name['nouveau_nom']
         nouv_num = name['nouveau_numero']
         with open('repertoire.txt','r') as repertoire:
            lignes = repertoire.readlines() #transforme le fichier texte en une liste separré a chque saut de ligne
         trouve = False
         for i, line in enumerate(lignes):#pour chaque element dans la liste lignes
            if nom in line:
                if num in line:
                    lignes.remove(line)
                    info = line #info prend la valeur de la ligne supprimé
                    trouve = True
         if trouve ==True :
             with open('repertoire.txt','w') as repertoire: #ouvre le fichier pour écrire
                 for line in lignes:
                     repertoire.write(line)#re ecrit le fichier sans les noms a supprimer
             repertoire.close()
             repertoire = open('repertoire.txt', 'a')
             repertoire.write('\n')
             repertoire.write(nouv_nom)
             repertoire.write('  :  ')
             repertoire.write(nouv_num)
             repertoire.close()        
             resultat = 'Le nom et le numéro ont été modifiés avec succès.'
             
         else:
             resultat = 'La demande est impossible car le nom ou le numéro est introuvable.'
         return render_template('resultat_recherche.html', nom = resultat)
    return render_template('resultat_recherche.html')
         
@app.route('/repertoire', methods = ['GET'])        
def repertoire():
    with open('repertoire.txt','r') as f:
        repertoire = f.readlines()
    return render_template('repertoire.html', repertoire = repertoire)
            
app.run(debug=True)