#!/usr/bin/python
# -*- coding: utf8 -*-


class Quadrilateral(object):
    """
    Pour une classe fondamentale (ie. ne ne dérivant d’aucune autre)
    la référence est, par convention, le nom spécial «object»
    qui désigne l’ancêtre de toutes les classes

    Convention de nommage :
        Les classes sont en PascalCase
    """

    objectCounter = 0

    def __init__(self):
        """ Une méthode d'instance pour compter les objets instanciés"""
        Quadrilateral.objectCounter += 1

    def get_infos(cls):
        """
        Une méthode de classe afficher le nombre d'objets

        Convention de nommage :
            les méthodes sont en lower_case_underscored ou camelCase
        """
        print
        print "Object #%s" % str(cls.objectCounter)

    get_infos = classmethod(get_infos)


class Parallelogram(Quadrilateral):
    """
    Un Parallelograme est un Quadrilatère particulier
    La classe Parallelogram  est donc dérivée de Quadrilateral
    """

    def __init__(self, side1, side2, angle):
        """
        Le constructur __init__ définit un Parallelogramme
        par ses deux longueurs et un angle.
        """
        self.side1 = side1
        self.side2 = side2
        self.angle = angle
        """ Un appel pour bien incrémenter le nb de quadrilatères """
        Quadrilateral.__init__(self)

    def perimeter(self):
        """ Calcul du périmètre """
        return 2 * (self.side1 + self.side2)

    def get_infos(self):
        """
        L'accesseur get_infos de la classe Parallelogram surcharge
        celui de la classe Quadrilateral pour afficher
        - les infos de Quadrilateral (le nb d'objets)
        - le nom de la classe de l'instance
        - le périmètre
        """
        Quadrilateral.get_infos()
        print "We have a %s" % self.__class__.__name__
        print "Its perimeter is %s" % self.perimeter()


class Rectangle(Parallelogram):
    """
    Un Rectangle est un Parallelogramme particulier
    L'accesseur get_infos remplace la méthode de même nom
    héritée de la classe parent :
    la méthode get_infos a été «surchargée».
    Deux classes possèdent une méthode homonyme qui
    effectuent un travail différent : c'est le polymorphisme.
    """

    def __init__(self, side1, side2):
        """
        Le constructeur __init__ se base sur celui du parent pour définir
        un nouveau constructeur avec un paramètre de moins
        """
        Parallelogram.__init__(self, side1, side2, 90)

    def area(self):
        """ Calcul de l'aire """
        return self.side1 * self.side2

    def get_infos(self):
        """
        L'accesseur get_infos de la classe Rectangle surcharge
        celui de la classe Parallelogram pour afficher
        - les infos de Parallelogram
        - l'aire
        """
        Parallelogram.get_infos(self)
        print "Its area is %s" % self.area()


# -----------------------------
# Le programme principal
# -----------------------------


my_para = Parallelogram(1, 7, 45)
my_para.get_infos()
my_rectangle = Rectangle(2, 3)
my_rectangle.get_infos()
