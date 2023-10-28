									Projet Repertoire telephonique site web 1ere NSI

Je m'excuse pour le manque d'accents ou les eventuelles erreurs d'orthographe dans ce document.

Le projet consiste de creer un repertoire telephonique integre dans un site web. Le repertoire et le "back end" du site web sont codees en python avec l'aide de l'application flask
et le "front end" du site web est code avec du html djangom du css et du javaScript.

les fonctions principales de ce site web sont l'ajout d'un nom associe a un numero, la recherche d'un nom dans le repertoire, la modification d'un nom ou numero dans le repertoire,
et la supprimation d'un nom du repertoire.

Le programme ne permet pas l'ajout de noms ou numeros identiques, les noms et numeros sont stockees dans un fichier txt (ont pourait utiliser une base de donnees SQL mais cela est
 hors programme)

Les parties codees en java/html/css sont tres simple car on n'a pas besoin de faire un site qui est tres esthetique et on s'interesse principalement a l'utilisation du framework
 Flask. Cependant j'ai fait des animations pour les boutons lorsque la souris est au dessus de celui-ci, cela n'est pas dutout necessaire mais c'est beau et rajoute 
 du dynamisme au site web.

Pour les pages HTML j'ai decide de faire une page pour chaque action meme si les pages se ressemblent beaucoup. Il y a un moyen de faire une page d'HTML "Squelette" ce qui serait
plus efficace que la solution effectue mais cela sors un peu du cadre du projet. Ceoendantm cela pourait vous donner des points bonus au pres de votre professeur d'NSI.

Le programme ne verifie pas la longeur du numero qui est donne donc on peut avoir des numeros de telephone qui ont moins de chiffres. Aucun systeme a ete mis en place pour
 gerer les caracteres speciaux, ce programme ne gere donc que les caracteres de la table ASCII (pas d'accents ou lettres de languages non latins)