def longest_word(text):
    L = text.split()
    mot = ""
    for x in L:
        if(len(x)>len(mot)):
            mot = x
    return mot

# On teste la fonction :

# Les chaînes de caractères à tester

tests = ["Il fait beau aujourdhui ", "Le python est un langage de programmation", "il faut faire du sport souvent"]

# Tester la fonction pour chaque chaîne de caractères

for test in tests:
    resultat = longest_word(test)
    print("Pour la chaîne de caractères '{}', le mot le plus long est : '{}'".format(test, resultat))
