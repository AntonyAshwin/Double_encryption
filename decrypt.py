#############################################################################
#REVERSE CIPHER
#The text is reversed
#############################################################################

output2 = input(">").lower()
message = " "
for letter in range(len(output2)-1,-1,-1):
    message += output2[letter]


###########################################################################
#MONO-ALPHABETIC SUBSTITUTION CIPHER
#A letter is directly replaced with the letter from the dictionary
###########################################################################


code = {
    "m":"a",  "w":"b",  "g":"c",  "f":"d",  "c":"e",  "b":"f",  "p":"g",
    "k":"h",  "v":"i",  "j":"j",  "x":"k",  "z":"l",  "q":"m",  "y":"n",
    "d":"o",  "u":"p",  "l":"q",  "r":"r",  "h":"s",  "s":"t",  "n":"u",
    "i":"v",  "a":"w",  "0":"x",  "t":"y",  "e":"z",
}
output1 = " "
for letter in range(0,len(message)):
    output1 += code.get(message[letter],message[letter])
print(output1)
