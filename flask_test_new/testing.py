from flask import Flask, render_template, request , url_for


app = Flask(__name__) 

@app.route('/') #page d'acceuil
def index():
    return render_template("pages.html")
            
            
@app.route('/ajouter', methods = ['POST','GET'])
def ajouter():
    return render_template('ajouter.html')
        
@app.route('/resultat_ajouter', methods = ['POST','GET'])
def resultat_ajouter():
    if request.method == "POST": #action lorsqu'une requete est faite
        name = request.form #name est un dictionaire qui prend pour valeurs les reponses aux questions de la page html
        nom = name['nom']
        num = name['num']
        with open('rep2.txt','a') as f:
            f.write('\n')
            f.write(nom)
            f.write('\n')
            f.write(num)

        resultat = 'le nom a bien été ajouté'
        return render_template('resultat_ajouter.html', resultat = resultat, nom = nom, num = num) #charge une nouvelle page html et retourne si le repertoire a ecrit le nouveau nom
    return render_template('resultat_ajouter.html')
        
@app.route('/supprimer', methods = ['POST','GET'])
def supprimer():
    return render_template('supprimer.html')


@app.route('/resultat_supprimer', methods = ['POST','GET'])
def resultat_supprimer():
    resultat = "le nom n'a pas été trouvé"
    trouve = False
    if request.method == "POST":
        name = request.form
        supprime = name['nom'] #le nom a supprimer
        with open('rep2.txt','r') as f:
            for line in f:
                if supprime == line
        if trouve == True:
            resultat = 'le nom a ete supprimé'
        return render_template('resultat_supprimer.html', resultat = resultat, nom = supprime)
    return render_template('resultat_supprimer.html')  
          
  
@app.route('/recherche', methods = ['POST','GET'])
def recherche():
    return render_template('recherche.html') 
            
@app.route('/resultat_recherche', methods = ['POST','GET'])
def resultat_recherche():
    liste = []
    resultat = "le nom n'a pas été trouvé"
    trouve = False
    if request.method == "POST":
        nom = request.form
        nom_recherche = nom['nom']
        with open('rep2.txt','r') as f:
            lignes = f.readlines()
            print(lignes)
            for i in range (len(lignes)):
                if nom_recherche == lignes[i].replace('\n', ''):
                    liste.append(lignes[i].replace('\n', ''))
                    liste.append(lignes[i+1].replace('\n', ''))
                    trouve = True
        if trouve == True:
            resultat = liste
        return render_template('resultat_recherche.html', nom = resultat)
    return render_template('resultat_recherche.html')
        
            
app.run(debug=True)