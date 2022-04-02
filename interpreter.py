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
I = 0

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

# ----------------------------------------------------------------------------- 5 ---
def Read( line ):
	# divide in tokens (words)
	tokens = line.split(" ")
	# useful variables
	lenght = len(tokens)
	firstToken = tokens[0]
	lastToken = tokens[-1]
	if " ".join(tokens[-7:-1]) == "Gallia est omnis divisa in partes":
		divisor = lastToken
		cellArr[I] /= roman.fromRoman( divisor )
		cellArr[I] = math.floor( cellArr[I] )
	elif line == "Carthago delenda est":
		cellArr[I] = 255
	elif line == "Ipse dixit":
		print(cellArr[I])
	elif firstToken == "Incedo":
		if lastToken == "legionibus":
			adder = tokens[-2]
			cellArr[I] += roman.fromRoman( adder )
			cellArr[I] = cellArr[I] % 255
		#elif lastToken == SOMETHING ELSE:
			# move pointer forward
	#elif firstToken == RETREAT:
		#legionibus or SOME ELSE?

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
		Parse( content )

# ----------------------------------------------------------------------------- 4 ---
for line in finContent:
	if line == "Memento Mori":
		break
	else:
		Read( line )

"""
elif lastToken == "est":
	print( "cell definition" )
"""
# dum ... -> while
# aut ... aut ... --> xor
# condicio sine qua non --> if
# advanse NUMBER legions --> cell += NUMBER
# retreat NUMBER legions --> cell -= NUMBER
# Supertempore Martio -> go to §Martio "coords" until finish coords