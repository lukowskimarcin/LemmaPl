import xml.etree.ElementTree
import codecs

e = xml.etree.ElementTree.parse('out.xml').getroot()

# https://docs.python.org/3/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/43589769/python3-parse-xml
# https://www.w3schools.com/xml/xpath_syntax.asp

outF = codecs.open("result.txt", "w", "utf-8")
for chunk in e.findall(".//chunk[@type='s']"):
    line = ''
    for lex in chunk.findall(".//lex"):
        ctag = lex.find('ctag').text
        base = lex.find('base').text

        if ctag == 'interp':
            line = line + base
        else:
            line = line +  ' ' + base 
        
    outF.write(line.strip())
    outF.write("\n")
outF.close()
 