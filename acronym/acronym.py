def abbreviate(words):
	words = words.upper()
	string = ""
	for letter in words:
		if letter.isalnum() or letter == "'":
			string += letter
		else:
			string += " "
	list = string.split()
	output = ""
	for word in list:
		output += word[0]
	return output