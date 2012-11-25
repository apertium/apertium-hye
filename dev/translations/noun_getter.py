#!/usr/local/bin/python3
#Takes a noun as a command line argument, then outputs the translations of that noun to a file. NOTE: Only works for Armenian nouns, but I can't imagine it would be difficult to modify it to work with other wiktionaries...
import sys
import os
import re

noun = sys.argv[1]
os.system("python3 html2text.py html_files/"+noun+" > parsed_HTML.txt")
soup = ''.join(open("parsed_HTML.txt", 'r').read())

#We have the HTML file stored in soup. first find if it is animate/inanimate.
animate_attrib = "aa"
if soup.find("inanimate") != -1:
    animate_attrib = "nn"
#Then if it needs to be parsed at all(Old Armenian/Alt. Spelling/Abbreviation)
if soup.find("Initialism") != -1:
    sys.exit(0)
if soup.find("Alternative") != -1:
    sys.exit(0)
if soup.find("Synonym of") != -1:
    sys.exit(0)
if soup.find("Traditional orthography spelling") != -1:
    sys.exit(0)
soup = soup.replace("ization", "isation")


#Now the real business, find the translations...
#Translations are done on all the lines from "[edit] Noun" "[edit] Synonyms" so grab those lines...
lines_to_parse = re.search('### \[\[edit\][^)]*\)\] Noun\n\n(.*?)\n\n####', soup, re.MULTILINE|re.DOTALL).group(0)

lines_to_parse = re.search('\)\n\n(.*)\)', lines_to_parse, re.MULTILINE|re.DOTALL).group(0)[3:]


#create each line individually:
lines = ("".join(lines_to_parse)).split("\n")
#If commas on line, split them at the comma.
for i in range(len(lines)):
    if "," in lines[i]:
        first, second, second = lines[i].partition(",")
        lines[i] = first
        second = "fill"+second
        lines.append(second)

for i in range(len(lines)):
    #line_to_input will store the semi-constructed line:
    line_to_input = "<e c=\""

    #remove the number section
    current_line = lines[i][5:]

    #Now remove the links in it:
    current_line = re.sub(r'\(/wiki/.*?\)', '', current_line)

    #If it has a comment attribute or not:
    if(current_line[0] == '('): #It has a comment...
        current_line = current_line[1:] #Take away the '('
        if(current_line[0] == '['):
            current_line = current_line[1:]
        #Finally have our comment:
        comment = re.search('([\w ]+)?', current_line).group(0)
        line_to_input += comment

        #Just take data after the next ')' (which matches the start of the comment
        current_line = current_line.partition("[")[2]
        #Last step, add the actual word:
        word = re.search('([\w ]+)?', current_line).group(0)
        line_to_input += "\"><p><l>" + noun + "<s n=\"n\"/><s n=\""+animate_attrib+"\"/></l><r>"+word+"<s n=\"n\"/></r></p></e>"

        #If the translation contains more than 3 spaces, comment it out:
        if word.count(' ') > 3:
            line_to_input += " -->"
            line_to_input = "<!-- "+line_to_input


    else:
        if(current_line[0] == '['):
            current_line = current_line[1:]
        #have our word:
        word = re.search('([\w ]+)?', current_line).group(0)

        #Last step, add the actual word:
        line_to_input += "\"><p><l>" + noun + "<s n=\"n\"/><s n=\""+animate_attrib+"\"/></l><r>"+word+"<s n=\"n\"/></r></p></e>"

        if word.count(' ') > 3:
           line_to_input = "<!-- "+line_to_input+" -->"

    print (line_to_input)


#RM files created:
os.system("rm parsed_HTML.txt")
