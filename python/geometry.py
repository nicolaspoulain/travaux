# -*- coding: utf8 -*-


class Quadrilateral():
    """ Une classe générique """

    objectCounter = 0

    def __init__(self):
        Quadrilateral.objectCounter += 1

    def getInfos(cls):
        """ Une méthode de classe """
        print("Object #%s" % str(cls.objectCounter))

    getInfos = classmethod(getInfos)


class Parallelogram(Quadrilateral):
    """
    Un Parallelograme est un Quadrilatère particulier
    La classe Parallelogram  est donc dérivée de Quadrilateral
    Le constructur __init__ définit un Paralleologramme
    par ses deux longueurs et un angle.
    L'accesseur getInfos affiche
    - le nom de la classe de l'instance
    - et le périmètre
    """

    def __init__(self, side1, side2, angle):
        Quadrilateral.__init__(self)
        self.side1 = side1
        self.side2 = side2
        self.angle = angle

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def getInfos(self):
        print
        Quadrilateral.getInfos()
        print "We have a %s" % self.__class__.__name__
        print "Its perimeter is %s" % self.perimeter()


class Rectangle(Parallelogram):
    """
    Un Rectangle est un Parallelogramme particulier
    Le constructeur __init__ se base sur celui du parent
    L'accesseur getInfos remplace la méthode de même nom
    héritée de la classe parent :
    la méthode getInfos a été «surchargée».
    Deux classes possèdent une méthode homonyme qui
    effectuent un travail différent : c'est le polymorphisme.
    """

    def __init__(self, side1, side2):
        Parallelogram.__init__(self, side1, side2, 90)

    def area(self):
        return self.side1 * self.side2

    def getInfos(self):
        Parallelogram.getInfos(self)
        print "Its area is %s" % self.area()

my_para = Parallelogram(1, 7, 45)
my_para.getInfos()
my_rectangle = Rectangle(2, 3)
my_rectangle.getInfos()
