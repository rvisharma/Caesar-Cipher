# this program is a Caesar cipher encrypter and decrypter

def translate_text(plain_text, key, mode = 'e'):
    """ (string, int) -> String

    takes the plain text and shift key and shifts the plain text characters to right side according to the key

    >>> translate_text("abcd", 3)
    'defg'
    >>> translate_text('AbC!d', 3)
    'DeF!g'
    """
    key = key%26
    if mode == 'd':
        key = -key
        
    shifted_text = ''
    
    for s in plain_text:
        
        if s.isalpha():
            char_num = ord(s)
            char_num += key
            if s.isupper():
                if char_num > ord('Z'):
                    char_num -= 26
                elif char_num < ord('A'):
                    char_num += 26
            else:
                if char_num > ord('z'):
                    char_num -= 26
                elif char_num < ord('a'):
                    char_num += 26
            shifted_text += chr(char_num)
        else:
            shifted_text += s
                
    return shifted_text


def brute_force(cipher_text):
    for key in range(1,27):
        print ("Key: " + str(key) + " : " + translate_text(cipher_text, key, 'd'))

    
## Program starts here ##

command = input("""To convert the Plain text to Cipher, press E
To convert the Cipher to Plain text, Press D: \n""")
  
if command.lower() == 'e':
    plain_text = input("Enter the plain text you want to encrypt: ")    #input
    key = input("Enter the Shift key, this key is important to remember!: ")  #input
    cipher = translate_text(plain_text, int(key))
    print ("Your Encrypted text is :\n" + cipher) #output

elif command.lower() == 'd':
    cipher_text = input('Input the Cipher\n') #input
    key_answer = (input('Enter the key or type ALL\n')) #input
    
    if key_answer.lower().isalpha():
        if key_answer.lower() == 'all':
            brute_force(cipher_text) #output
        else:
            print('Invalid Input')
    else:
        key_answer = int(key_answer)
        plain_text = translate_text(cipher_text, key_answer, 'd')
        print (plain_text) #output
      
else:
    print("Wrong Input")
