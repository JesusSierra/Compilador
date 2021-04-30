import sys

#Se creó un diccionario con el cual podremos hacer consultas a la hora de asignar los tokens
dicc = {
    "suma":"SUMA",
    "resta":"RESTA",
    "multiplicacion":"MULTIPLICACION",
    "division":"DIVISION",
    "mayor_que":"MAYOR_QUE",
    "mayor_igual_que":"MAYOR_IGUAL_QUE",
    "menor_que":"MENOR_QUE",
    "menor_igual_que":"MENOR_IGUAL_QUE",
    "igual_que":"IGUAL_QUE",
    "es_diferente":"ES_DIFERENTE",
    "asignacion":"ASIGNACION",
    "semicolon":"SEMICOLON",
    "coma":"COMA",
    "parentesis_abierto":"PARENTESIS_ABIERTO",
    "parentesis_cerrado":"PARENTESIS_CERRADO",
    "brackets_abiertas":"BRACKETS_ABIERTAS",
    "brackets_cerradas":"BRACKETS_CERRADAS",
    "curly_abiertas":"CURLY_ABIERTAS",
    "curly_cerradas":"CURLY_CERRADAS",
    "nueva_linea":"NUEVA_LINEA",
    "num":"NUM",
    "id":"ID",
    "Else":"ELSE",
    "If":"IF",
    "Int":"INT",
    "Return":"RETURN",
    "Void":"VOID",
    "While":"WHILE",
    "Input":"INPUT",
    "Output":"OUTPUT",
}

#Estas variables se hacen globales para que todas la funciones las puedan usar
codigo = None
token = None
archivo = None

class analisis:
    #Leerá el archivo que se proporcione y lo guarda en variable
    def leerArchivo (self):
        global archivo
        archivo = open("codigo.txt", "r")
        global codigo

    #Comienza a leer caracter por caracter
    def conteo(self):
        global token
        while True:
            codigo=archivo.read(1)
            palabra = codigo
            while(codigo.isalpha()): #Comienza a revisar si los caracteres son letras
                for b in codigo:
                    #Aquí se asegurará de detener el almacenamiento de caracteres si se encuentra con alguna de estas condiciones
                    if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!", b == "," or b == ";"):
                        break;
                    palabra+=b
                if (palabra.startswith ('v')): #comenzará a coomparar las letras que almacenó, si concuerda con alguna condicional entra en el ciclo
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                        if(palabra == "void"):
                            token = dicc["Void"]
                        else:
                            token = dicc["id"] #En dado caso que la palabra no sea igual a algún keyword será catalogado como ID
                elif(palabra.startswith('i')):
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                        if(palabra == "if"):
                            token = dicc["If"]
                        elif(palabra == "int"):
                            token = dicc["Int"]
                        elif(palabra == "input"):
                            token = dicc["Input"]
                        else:
                            token = dicc["id"]

                elif (palabra.startswith ('w')):
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                        if(palabra == "while"):
                            token = dicc["While"]
                        else:
                            token = dicc["id"]
                elif (palabra.startswith ('e')):
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                        if(palabra == "else"):
                            token = dicc["Else"]
                        else:
                            token = dicc["id"]
                elif (palabra.startswith ('o')):
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                        if(palabra == "output"):
                            token = dicc["Output"]
                        else:
                            token = dicc["id"]
                elif (palabra.startswith ('r')):
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                        if(palabra == "return"):
                            token = dicc["Return"]
                        else:
                            token = dicc["id"]
                else:
                    token = dicc ["id"]
                    while(codigo.isalpha()):
                        codigo=archivo.read(1)
                        for b in codigo:
                            if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                                break;
                            palabra+=b
                print(token)
                #print(palabra)
            if (palabra.isdigit()): #Nos permititrá saber si el caracter es un número
                while(codigo.isdigit()):#Si los caracteres son números entrará en este ciclo
                    codigo=archivo.read(1)
                    for b in codigo:
                        if (b == " " or b == "(" or b == ")" or b == "{" or b == "}" or b == "[" or b == "]" or b == "+" or b == "-" or b == "/" or b == "*" or b == "=" or b == "!" or b == "," or b == ";"):
                            break;
                        palabra+=b
                    if (palabra.isdigit()): #Si cumple las condiciones se cataloga con su respectivo token
                        token = dicc ["num"]
                print(token)
                #print(palabra)
            if ( '@' in codigo or '&' in codigo or '%' in codigo or '#' in codigo or '"' in codigo or '^' in codigo or '¨' in codigo or '-' in codigo or '_' in codigo or '´' in codigo or '`' in codigo):
                sys.exit("Error caracter inválido: " +codigo)
            if (codigo == '+'):#En esta seccion compara símbolos 
                token = dicc["suma"]
                print(token)
            elif (codigo == '-'):
                token = dicc["resta"]
                print(token)
            elif (codigo == '*'):
                token = dicc["multiplicacion"]
                print(token)
            elif (codigo == '/'):
                tokenAnterior = codigo
                codigo=archivo.read(1)
                resultado = tokenAnterior+codigo
                if(resultado == '/*'):
                    codigo=archivo.read(1)
                    while (codigo != '*'):
                        codigo=archivo.read(1)
                        if(codigo == '*'):
                            tokenAnterior = codigo
                            codigo=archivo.read(1)
                            resultado = tokenAnterior+codigo
                            if(resultado =='*/'):
                                break;
                        if not codigo:
                            sys.exit("Error comentario no terminado")
                else:
                    token = dicc["division"]
                    print(token)     
            elif (codigo == ';'):
                token = dicc["semicolon"]
                print(token)
            elif (codigo == ','):
                token = dicc["coma"]
                print(token)
            elif (codigo == '('):
                token = dicc["parentesis_abierto"]
                print(token)
            elif (codigo == ')'):
                token = dicc["parentesis_cerrado"]
                print(token)
            elif (codigo == '['):
                token = dicc["brackets_abiertas"]
                print(token)
            elif (codigo == ']'):
                token = dicc["brackets_cerradas"]
                print(token)
            elif (codigo == '{'):
                token = dicc["curly_abiertas"]
                print(token)
            elif (codigo == '}'):
                token = dicc["curly_cerradas"]
                print(token)
            elif (codigo == '<'): #Si se encuentra con este símbolo hará otro analisis
                tokenAnterior = codigo
                codigo=archivo.read(1)
                resultado = tokenAnterior+codigo
                if (resultado == '<='):
                    token = dicc["menor_igual_que"]
                    codigo = resultado
                else:
                    token = dicc["menor_que"]
                    codigo = resultado
                print(token)
            elif (codigo == '>'):
                tokenAnterior = codigo
                codigo=archivo.read(1)
                resultado = tokenAnterior+codigo
                if (resultado == '>='):
                    token = dicc["mayor_igual_que"]
                    codigo = resultado
                else:
                    token = dicc["mayor_que"]
                    codigo = resultado
                print(token)
            elif (codigo == '='):
                tokenAnterior = codigo
                codigo=archivo.read(1)
                resultado = tokenAnterior+codigo
                if (resultado == '=='):
                    token = dicc["igual_que"]
                    codigo = resultado
                else:
                    token = dicc["asignacion"]
                    codigo = resultado
                print(token)
            elif (codigo == '!'):#Mismo caso que los anteriores solo que este únicamente puede existir si el símbolo de = está junto a él
                tokenAnterior = codigo
                codigo=archivo.read(1)
                resultado = tokenAnterior+codigo
                if (resultado == '!='):
                    token = dicc["es_diferente"]
                    codigo = resultado
                else:
                    sys.exit("Error de sintaxis, se esperaba '=', texto encontrado: " + codigo)
                    codigo = resultado
                print(token)
            #Analiza los saltos de línea    
            if (codigo == '\n'):
                token = dicc["nueva_linea"]
                print(token)
            #Analiza los espacios en blanco y los ignora
            if(codigo == ' ' or codigo == '\t'):
                None
            if not codigo: break
        # print (codigo) #Imprime el código 




analisis().leerArchivo()
analisis().conteo()

