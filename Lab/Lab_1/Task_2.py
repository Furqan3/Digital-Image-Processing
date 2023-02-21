def conversion(number,system):
    """This function convert the decimal value to binary octal and hexa"""
    return_value=[]
    if system=="bin":
        print("To binary:")
        while number>0:
            return_value.append(number%2)
            number=int(number/2)
    elif system=="oct":
        print("To binary:")
        while number>0:
            return_value.append(number%8)
            number=int(number/8)
    elif system=="hex":
        print("To binary:")
        while number>0:
            if (number%16)==10:
                return_value.append('A')
            elif (number%16)==11:
                return_value.append('B')
            elif (number%16)==12:
                return_value.append('C')
            elif (number%16)==13:
                return_value.append('D')
            elif (number%16)==14:
                return_value.append('E')
            elif (number%16)==15:
                return_value.append('F')
            else:
                return_value.append(number%16)
            number=int(number/16)
    return return_value


number=int(input("Enter Number"))
system=input("Enter Number system(oct,bin,hex)")
myreturn=conversion(number,system)
for i in range(len(myreturn),0,-1):
    print(myreturn[i-1],end='')