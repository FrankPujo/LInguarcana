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
convList = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","x","y","z","A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","V","X","Y","Z"]
backList = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7,"i": 8,"k": 9,"l": 10,"m": 11,"n": 12,"o": 13,"p": 14,"q": 15,"r": 16,"s": 17,"t": 18,"u": 19,"x": 20,"y": 21,"z": 22,
			"A": 23,"B": 24,"C": 25,"D": 26,"E": 27,"F": 28,"G": 29,"H": 30,"I": 31,"K": 32,"L": 33,"M": 34,"N": 35,"O": 36,"P": 37,"Q": 38,"R": 39,"S": 40,"T": 41,"V": 42,"X": 43,"Y": 44,"Z": 45}
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
	elif line == "Non ducor, duco":
		# shift value to the next cell
		newPtr = (ptr + 1) %64
		cellArr[newPtr] = cellArr[ptr]
		cellArr[ptr] = 0
	elif line == "Verba volant, scripta manent":
		num = cellArr[ptr] % 46
		letter = convList[num]
		cellArr[ptr] = letter
	elif line == "Non loqui sed facere":
		letter = cellArr[ptr]
		num = backList.get( letter )
		cellArr[ptr] = num
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
	elif line[0:10] != "Commentari":
		read( line )

# dum ... -> while
# aut ... aut ... --> xor
# condicio sine qua non --> if
# Supertempore Martio -> go to Martio "coords" until finish coords