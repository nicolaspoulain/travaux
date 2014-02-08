class Crayon:
    """
    Documentation
    """

    def __init__(self, couleur, epaisseur):
        """
        Constructeur
        """
        self.couleur = couleur
        self.epaisseur = epaisseur

    def getCouleur(self):
        """
        Rerourne la couleur du crayon
        """
        return self.couleur

unCrayonBleu = Crayon("bleu", 10)
print "Couleur : %s" % unCrayonBleu.getCouleur()
unCrayonRouge = Crayon("rouge", 12)
print "Couleur : %s" % unCrayonRouge.getCouleur()
