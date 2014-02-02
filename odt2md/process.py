import re
with open("exos.md", "r") as myfile:
    #data = myfile.read().replace('\n', '')
    data = myfile.read()
data = re.sub(r'<span>(.*)<\/span>', r'', data)
 # semble foctionner sur http://rubular.com/r/t2Ahjs9UzF
 # mais non :(  )<span>(.*\s*)*<\/span>

regex = re.compile("(\d\.(.*\s)*)\d")
