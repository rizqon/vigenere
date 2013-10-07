#Implementation VIGENERE CIPHER
#
#Author 	: Rizqon Sadida
#NIM		: 11.11.5381
#
#
#License 	: Open Source
import getopt, sys, os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 'operasi'
def main(argv):
    try:
        opt, args = getopt.getopt(argv, "h:e:d:o:c:", ["help", "encrypt", "decrypt", "open", "chiper"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    
    for o, text in opt:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--encrypt"):
         	print encrypt(text, KEY)
        elif o in ("-d", "--decrypt"):
            print decrypt(text, KEY)
        elif o in ("-o", "--open"):
        	text = open(text, 'r').read()
        	print encrypt(text, KEY)
        elif o in ("-c", "--chiper"):	
        	text = open(text, 'r').read()
        	print decrypt(text, KEY)
        else:
            assert False, "unhandled option"

def usage():
    usage = """
    -h --help           	Prints this
    -e --encrypt        	encrypt plaintext
    -d --decrypt        	decrypt chipertext
    -o --open				open file
    -c --chiper 			decode chiper text file
    """
    print usage

def encrypt(plaintext, kunci):
	translated = []
	keyIndex = 0
	kunci = kunci.upper()

	for symbol in plaintext:
		p1 = LETTERS.find(symbol.upper())
		if p1 != -1:
			k1 = LETTERS.find(kunci[keyIndex])

			nganu = (p1 + k1) % len(LETTERS)
			if symbol.isupper():
				translated.append(LETTERS[nganu])
			elif symbol.islower():
				translated.append(LETTERS[nganu].lower())

			keyIndex += 1
			if keyIndex == len(kunci):
				keyIndex = 0
		else:
			translated.append(symbol)			
	return ''.join(translated)
	pyperclip.copy(''.join(translated))
def decrypt(chipertext, kunci):
	translated = []
	keyIndex = 0
	kunci = kunci.upper()

	for symbol in chipertext:
		p1 = LETTERS.find(symbol.upper())
		if p1 != -1:
			k1 = LETTERS.find(kunci[keyIndex])

			nganu = (p1 - k1) % len(LETTERS)
			if symbol.isupper():
				translated.append(LETTERS[nganu])
			elif symbol.islower():
				translated.append(LETTERS[nganu].lower())

			keyIndex += 1
			if keyIndex == len(kunci):
				keyIndex = 0
		else:
			translated.append(symbol)			
	return ''.join(translated)
	#print 
if __name__ == "__main__":
    main(sys.argv[1:])
