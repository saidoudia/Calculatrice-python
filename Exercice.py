# Exercice 1 : Affichez les deux phrases suivantes à l'écran en utilisant différentes syntaxes de guillemets :
# "Bonjour tout le monde !"
# 'Python est génial !'
print("Bonjour tout le monde ")
print('Python est géniale')

# Exercice 2 : Citations à l’intérieur des guillemets
# Affichez les phrases suivantes, où les guillemets sont à l’intérieur de la chaîne :
# It’s time to learn Python!
# She said, 'Hello, world!'
print("It's time to learn python!")
print("She said,'hello',world!")
# Exercice 3 : Attribuer une chaîne à une variable
# Attribuez la phrase "Python est un langage de programmation" à une variable appelée langage et affichez-la à l’écran.
langage = "Python est un langage de programmation"
print(langage)

# Exercice 4 : Chaînes multilignes
# Attribuez un texte multiligne à une variable texte et affichez-le. Utilisez les triples guillemets simples ou doubles pour inclure des retours à la ligne.
# Exemple de texte multiligne :
# Python est un langage puissant.
# Il est facile à apprendre.
# Il est utilisé dans divers domaines.
x = ''' Python est un langage puissant.
 Il est facile à apprendre.
 Il est utilisé dans divers domaines.'''
print(x)
# Exercice 5 : Les chaînes sont des tableaux
# Créez une variable mot contenant le mot "Programmation" et affichez le caractère à la position 4 (rappel : les indices commencent à 0).
mot = "Programmation" 
print(mot[4])
# Exercice 6 : Boucle à travers une chaîne
# Créez une boucle qui parcourt chaque caractère de la chaîne "informatique" et l'affiche à l'écran.
informatique = "information"
for i in  informatique:
 print(i)
# Exercice 7 : Longueur de la chaîne
# Créez une variable phrase contenant "Apprendre Python" et affichez la longueur de cette chaîne (le nombre de caractères).
 x = "Apprendre Python"
 print(len(x))
# Exercice 8 : Vérifier la chaîne (mot-clé in)
# Créez une variable sentence contenant "Le Python est facile à apprendre" et vérifiez si le mot "facile" est présent dans cette phrase. Affichez le résultat.
x = "Le Python est facile à apprendre"
print("facile" in x)
# Exercice 9 : Utiliser if avec in
# Créez une variable txt contenant "Python est mon langage préféré" et affichez "Oui, Python est mon langage préféré" seulement si le mot "Python" est présent dans la chaîne.
txt = "Python est mon langage préféré"
if "Python" in txt:
 print("Oui, Python est mon langage préféré")

# Exercice 10 : Vérifier si un mot n'est pas présent (mot-clé not in)
# Créez une variable texte contenant "Le Python est un langage génial" et vérifiez si le mot "Java" n'est pas présent. Affichez "Non, Java n'est pas présent" si c'est le cas.
texte = "Le Python est un langage génial"
if "Java"  not in  texte:
 print("Non, Java n'est pas présent")