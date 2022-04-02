# Linguarcana

import sys
import math
# roman module to read nmerals
import roman

# open file
src = open( sys.argv[1], "r" )
# identify sections
whole = "".join( x for x in src )
sections = whole.split( "\nMense " )

# initialize cell array
cellArr = [0] * 64
# cell pointer
ptr = 0
# temporary variable
temp = 0

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
# list for character conversion when printing (and inputting in future)
#conversion = [ 
# initialize list
finContent = []

# ----------------------------------------------------------------------------- 3 ---
# section parsing function
def parse( thing ):
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

# ----------------------------------------------------------------------------- 5 ---
def read( line ):
	global ptr
	global temp
	# divide in tokens (words)
	tokens = line.split(" ")
	# useful variables
	lenght = len(tokens)
	firstToken = tokens[0]
	lastToken = tokens[-1]
	if " ".join(tokens[0:6]) == "Gallia est omnis divisa in partes":
		if " ".join( tokens[lenght-2:lenght] ) == "illo numero":
			divisor = temp
		else:
			divisor = roman.fromRoman( lastToken )
		cellArr[ptr] /= divisor
		cellArr[ptr] = math.floor( cellArr[ptr] )
	elif line == "Carthago delenda est":
		cellArr[ptr] = 256
	elif line == "Ipse dixit":
		print(cellArr[ptr])
	elif firstToken == "Incedo":
		if lastToken == "legionibus" or lastToken == "legione":
			if " ".join( tokens[-3:-1] ) == "illo numero":
				adder = temp
			else:
				adder = roman.fromRoman( tokens[-2] )
			cellArr[ptr] += adder
			cellArr[ptr] = cellArr[ptr] % 255
		elif lastToken == "miliariis" or lastToken == "miliario":
			ptr += 1
			ptr = ptr % 64
	elif firstToken == "Retrocedo":
		if lastToken == "legionibus" or lastToken == "legione":
			if " ".join( tokens[-3:-1] ) == "illo numero":
				subtracter = temp
			else:
				subtracter = roman.fromRoman( tokens[-2] )
			cellArr[ptr] -= subtracter
			cellArr[ptr] = abs( cellArr[ptr] )
		elif lastToken == "miliariis" or lastToken == "miliario":
			ptr -= 1
			if ptr < 0:
				ptr += 64
	elif line == "Hic est":
		temp = cellArr[ptr]

# ----------------------------------------------------------------------------- 1 ---
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

# ----------------------------------------------------------------------------- 2 ---
for section in months:
	# consider only non-empty sections
	# and parse them momentarily
	content = months.get(section)
	if content != "":
		parse( content )

# ----------------------------------------------------------------------------- 4 ---
for line in finContent:
	if line == "Memento Mori":
		break
	else:
		read( line )

# dum ... -> while
# aut ... aut ... --> xor
# condicio sine qua non --> if
# Supertempore Martio -> go to §Martio "coords" until finish coords