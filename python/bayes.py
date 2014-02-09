# les filtres Baysesiens permettent de classifier des données.
# Exemple d'application : reconnaissance automatique de la langue, anti-Spam,
# cryptographie...

from reverend.thomas import Bayes

unReseauBayesiens = Bayes()
uneListeDePropositions = [('math', 'on fait des calculs , \
                           des additions, des multiplications'),
                          ('math',        '3 + 4 = 7 ; 10 + 7 = 17 ; \
                           99/11 = 9'),
                          ('math', '12 + 10 -5 = 17 ; 70-10 = 60'),
                          ('math', 'le carré des 2 cotés du triangle \
                           sont liés par une relation'),
                          ('math', 'la fonction sinus ( sin ) sert à \
                           représenter les phénomènes cycliques'),
                          ('math', 'sin (PI) = 3.14159 et \
                           cosinus (0) = 1'),
                          ('philosophie', 'je disserte sur le sens de la vie'),
                          ('philosophie', 'être ou ne pas être, telle est \
                           la question'),
                          ('philosophie', 'je sais que je ne sais rien'),
                          ('philosophie', 'les phénomènes sont réels à \
                           condition que nous le souhaitions'),
                          ('philosophie', 'la raison est-elle toujours \
                           raisonnable ?'),
                          ('philosophie', 'le cerveau peut-il être compris ?'),
                          ('philosophie',  "l'univers peut-il être l'objet de \
                           connaissance ?"),
                          ('philosophie', 'le calcul a-t-il des limites \
                           intrinsèques ?'),
                          ('philosophie', "une relation peut être durable si \
                           l'homme la souhaite")]

for uneCategorie, uneProposition in uneListeDePropositions:
    # entrainement du réseau
    unReseauBayesiens.train(uneCategorie, uneProposition)


phraseAnalyz1 = 'voici un résultat  : 66/6 = 11 '
phraseAnalyz2 = "je ne saurais dire s'il  pourra tout comprendre ... "
phraseAnalyz3 = "le phénomène de la pluie pourrait être d'origine divine"
phraseAnalyz4 = 'la représentation bourbakiste des chiffres assure leur \
                    détermination'

for unePhrase in (phraseAnalyz1, phraseAnalyz2, phraseAnalyz3, phraseAnalyz4):
    # calculs de la catégorie
    solutions = unReseauBayesiens.guess(unePhrase)
    categorie = solutions[0][0]
    probabilite = solutions[0][1]
    print "la phrase '%s' est de catégorie '%s' avec une \
          proba de '%d /100' " % (unePhrase, categorie, probabilite * 100)


# Résultats :
# la phrase 'voici un résultat  : 66/6 = 11 ' est de catégorie 'math'
# avec une probabilité de '99 /100'
# la phrase 'je ne saurais dire s'il  pourra tout comprendre ... ' est
# de catégorie 'philosophie' avec une probabilité de '99 /100'
# la phrase 'le phénomène de la pluie pourrait être d'origine divine' est
# de catégorie 'philosophie' avec une probabilité de '92 /100'
# la phrase 'la représentation bourbakiste des chiffres assure leur déter-
# -mination' est de catégorie 'philosophie' avec une probabilité de '55 /100'
