from xml.etree.ElementTree import parse

tree = parse("note.xml")
note = tree.getroot()

childs=note.getiterator()
childs=note.getchildren()

for child in note.getiterator:


childs=note.getiterator("from")
childs=note.getchildren()
print("end")
