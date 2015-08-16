def intToChar(_index):
	return chr(_index)

def intToHex(_index):
	return hex(_index).rstrip("L").lstrip("0") or "0"