###########################################################################
#MONO-ALPHABETIC SUBSTITUTION CIPHER
#A letter is directly replaced with the letter from the dictionary 
###########################################################################


code = {
    "a":"m",  "b":"w",  "c":"g",  "d":"f",  "e":"c",  "f":"b",  "g":"p",
    "h":"k",  "i":"v",  "j":"j",  "k":"x",  "l":"z",  "m":"q",  "n":"y",
    "o":"d",  "p":"u",  "q":"l",  "r":"r",  "s":"h",  "t":"s",  "u":"n",
    "v":"i",  "w":"a",  "x":"0",  "y":"t",  "z":"e",
}
message = input("> ").lower()
output1 = " "
for letter in range(0,len(message)):
    output1 += code.get(message[letter],message[letter])
print(output1)



#############################################################################
#REVERSE CIPHER 
#The text is reversed
#############################################################################

output2 = " "
for letter in range(len(output1)-1,0,-1):
    output2 += output1[letter]
print(output2)

##############################################################################
