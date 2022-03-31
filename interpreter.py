# Linguarcana

import sys

src = open( sys.argv[1], "r" )

whole = "".join( x for x in src )
sections = whole.split( "\nMense " )

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

sectionList = list(i for i in range(10))

n = 0
for section in sections:
	lines = section.split("\n")
	month = lines[0]
	if n != 0:
		months.update({ month: section })
	n += 1

print( months )

# VARIABLE est omnis divisa in partes NUMBER -> divide
# first line "De ..."
# ave ... -> print
# dum ... -> while