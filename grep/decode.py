import base64

with open("grep_chal.txt") as infile:

	dico = {}

	for line in infile:
		decoded = base64.b64decode(line.strip())
		
		if decoded not in dico:
			dico[decoded] = 1
		else:
			dico[decoded] += 1

	for entry in dico:
		if dico[entry] == 4:
			print(entry)