import pyperclip
message="0.1,0.2"
key=6
mode = 'encrypt'
SYMBOLS = "1 2 3 4 5 6 7 8 9,"
translated = ''
for symbols in message:
	if symbols in SYMBOLS:
           symbolIndex=SYMBOLS.find(symbols)
           if mode =='encrypt':    
             translatedIndex = symbolIndex + key
           elif mode == 'decrypt':
             translatedIndex = symbolIndex - key 
           if translatedIndex >= len(SYMBOLS):
             translatedIndex = translatedIndex-len(SYMBOLS)   
           elif translatedIndex < 0:
             translatedIndex = translatedIndex + len(SYMBOLS) 
           translated = translated + SYMBOLS[translatedIndex]
	else:
		translated = translated + symbols	               			    
print(translated)
pyperclip.copy(translated)        
