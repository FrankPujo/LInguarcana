# Linguarcana

import sys

# open file
src = open( sys.argv[1], "r" )

# identify sections
whole = "".join( x for x in src )
sections = whole.split( "\nMense " )

# month sections
months = {
	"Martio": "",
	"Aprile": "",
	"Maio": "",
	"Iunio": "",
	"Quintili": "",
	"Sextili": "",
	"Septembre": "",
	"Octobre": "",
	"Novembre": "",
	"Decembre": ""
}

#sectionList = list(i for i in range(10))

# fill the sections in dictionary with the right content
n = 0
for section in sections:
	lines = section.split("\n")
	month = lines[0]
	if n != 0:
		months.update({ month: section })
	n += 1

finContent = []
for section in months:
	# consider only non-empty sections
	content = months.get(section)
	if content != "":
		# modify content removing months
		lines = content.split("\n")
		lines.pop(0)
		for line in lines:
			finContent.append(line)

print(finContent)

for line in finContent:
	if line == "Memento Mori":
		break
	else:
		print( "read line" )

# VARIABLE est omnis divisa in partes NUMBER -> divide
# ipse dixit ... -> print
# dum ... -> while
# aut ... aut ... --> xor
# condicio sine qua non --> if