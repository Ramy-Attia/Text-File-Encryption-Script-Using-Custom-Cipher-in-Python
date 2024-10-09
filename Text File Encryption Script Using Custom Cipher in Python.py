
#In this code, we define a function that opens a dictionary with the encryption code given in the question.
#Then we take the text from the input file and use it as a string. Then encrypt it with the provided dictionary before creating a new file and writing the new encrypted code into it.

import os

def encrypt(line):
    decryptcode = ""
    Encrypt_code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
                    'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
                    'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
                    'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
                    'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
                    'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
                    'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
                    'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
                    'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
                    '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
                    '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
                    '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
                    ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
                    "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
                    '{':'[','[':'{','}':']',']':'}'\
                    }

    for text in line:
        if text == '\n':
            decryptcode = decryptcode + '\n'
        elif text.isspace():
            decryptcode = decryptcode + text
        else:
            decryptcode = decryptcode + Encrypt_code[text]

    return decryptcode

while True:
    print(os.path.dirname(os.path.abspath(__file__))) 
    input_file_name = input("Enter the name of an input text file with extention:")
    if os.path.isfile(input_file_name) == False:
        print("File Not found please try again")
    else:
        input_file = open(input_file_name, "r")
        print("\ninput file " + input_file_name+" open Successfully ....")
        break

output_file_name = input("Enter the Name of an output file with extension(to store the encrypted code):")
output_file = open(output_file_name, "w")
print("\noutput file" + output_file_name +" open Successfully for writing encrypted data....")

for line in input_file:
    decryptcode = encrypt(line)
    output_file.write(decryptcode)

print("\nData encryption completed .")
input_file.close()
output_file.close()
