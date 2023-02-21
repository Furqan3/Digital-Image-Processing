def tomorse_code(message):
    message=message.upper()
   

    mydictionary={'A':'.-','B':'-...','C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':'--.','H':"....",'I':"..",'J':".---"
                  ,'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T':"-",'U':"..-"
                  ,'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--..",'0':"-----",'1':".----",'2':"..---",'3':"...--",'4':"....-"
                  ,'5':".....",'6':"-....",'7':"--...",'8':"---..",'9':"---..",' ':' ' }
    returnstring=''
    for i in message:
        returnstring+=mydictionary[i]
    return returnstring
user_message=str(input("Enter your message: "))
print("Morse Code= "+tomorse_code(user_message))