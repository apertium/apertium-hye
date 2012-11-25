#!/usr/local/bin/python3
#Takes a noun as a command line argument, then outputs the inflections of that noun to a file. NOTE: Only works for Armenian nouns, but I can't imagine it would be difficult to modify it to work with other wiktionaries...
import sys
import os
import re

noun = sys.argv[1]
os.system("python3 html2text.py html_files/"+noun+" > parsed_HTML.txt")
soup = ''.join(open("parsed_HTML.txt", 'r').read())


soup = re.sub(r'\((.*?)\)', '', soup, flags=re.DOTALL|re.MULTILINE)
output = re.findall('\[\[edit\]\][\s]Declension(.*?)###', soup, re.DOTALL|re.MULTILINE)


#We are only concerned with the first group of output, as second is always old armenian :)
output = output[0]

animacy = "aa"
if "inanimate" in output:
    animacy = "nn"

#Adjectives follow same layout each time: 
#
#nominative/accusative
#nominative/accusative definite
#genitive/dative
#dative definite
#ablative
#instrumental
#locative
#
# '-' means N/A, skip it
#nominative/accusative definite is the only inflection which can have two entries. These will be separated by a /
group_counter = 0

line = noun+"; "+noun+"; sg.nom.ind; n."+animacy
print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.nom.ind; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.nom.def; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.nom.def; n."+animacy
group_counter+=1
print (line)
if "]/[" in output:
    line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.nom.def; n."+animacy
    group_counter+=1
    print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.dat.ind; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.dat.ind; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.dat.def; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.dat.def; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.abl.ind; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.abl.ind; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.ins.ind; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.ins.ind; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.loc.ind; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.loc.ind; n."+animacy
group_counter+=1

print (line)

#######END OF NORMAL INFLECTIONS#######
#######POSSESSIVE FORMS BEGIN:  #######
line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.nom.ind.px1sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.nom.ind.px1sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.dat.ind.px1sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.dat.ind.px1sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.abl.ind.px1sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.abl.ind.px1sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.ins.ind.px1sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.ins.ind.px1sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.loc.ind.px1sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.loc.ind.px1sg; n."+animacy
group_counter+=1

print (line)


########2ND PERSON POSESSIVES###########
line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.nom.ind.px2sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.nom.ind.px2sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.dat.ind.px2sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.dat.ind.px2sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.abl.ind.px2sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.abl.ind.px2sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.ins.ind.px2sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.ins.ind.px2sg; n."+animacy
group_counter+=1

print (line)


line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; sg.loc.ind.px2sg; n."+animacy
group_counter+=1

print (line)

line = noun+"; "+re.findall('\[(.*?)\]', output, re.DOTALL|re.MULTILINE)[group_counter]+"; pl.loc.ind.px2sg; n."+animacy
group_counter+=1

print (line)


########################################
### SORTING, ETC, DONE IN OTHER FILE ###
########################################


#rm files created:
os.system("rm parsed_HTML.txt")
