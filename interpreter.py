# Linguarcana

import sys

# open file
src = open( sys.argv[1], "r" )

# identify sections
whole = "".join( x for x in src )
sections = whole.split( "\nMense " )
run = True

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
monthLinks = {
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

# initialize list
finContent = []

# ----------------------------------------------- 3 ---
# section parsing function
def Parse( thing ):
	# modify content removing months
	lines = thing.split("\n")
	month = lines[0]
	lines.pop(0)
	monthStart = len( finContent )
	for line in lines:
		# store all the lines in the final content list
		finContent.append( line )
	monthEnd = len( finContent ) - 1
	coords = [ monthStart, monthEnd ]
	# save the start and end lines for recursion
	monthLinks.update({ month: coords })

# ----------------------------------------------- 5 ---
def Read( line ):
	print( line )

# ----------------------------------------------- 1 ---
# fill the sections in dictionary with the right content
n = 0
for section in sections:
	# START
	lines = section.split("\n")
	# each moth section is stored in the correct location
	month = lines[0]
	if n != 0:
		months.update({ month: section })
	n += 1

# ----------------------------------------------- 2 ---
for section in months:
	# consider only non-empty sections
	# and parse them momentarily
	content = months.get(section)
	if content != "":
		Parse( content )

# ----------------------------------------------- 4 ---
for line in finContent:
	if line != "Memento Mori":
		Read( line )

"""
tokens = line.split(" ")
lastToken = tokens[-1]
if lastToken == "dixit":
	print( "print statement" )
elif lastToken == "est":
	print( "cell definition" )
"""
# VARIABLE est omnis divisa in partes NUMBER -> divide
# ipse dixit ... -> print
# dum ... -> while
# aut ... aut ... --> xor
# condicio sine qua non --> if
# advanse NUMBER legions --> cell += NUMBER
# retreat NUMBER legions --> cell -= NUMBER
#FUTURE Supertempore Martio -> go to §Martio "coords" until finish coords