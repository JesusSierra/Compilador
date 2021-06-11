import sys
from analizadorLexico import *

tablaTokens=[]
index = 0
lista =[]
currentToken = ""
variablesDeclaradas = []
variable = []
variableGuardada=[]

class sintax:  
    #El main nos sirve para hacer la primer llamada y empezar a recorrer toda la sintáxis así como agregar el símbolo de pesos al final de la lista de tokens
    def main(self):
        global tablaTokens
        tablaTokens = tokens
        currentToken = a.obtenerToken()
        lista.pop()
        lista.append('$')
        a.program(currentToken)
    #Aquí se encuentra toda la lógica para obtener el siguiente token, tenemos un index igual a 0 que usamos para obtener todos los tokens de la lista del analizador léxico solo una vez 
    #También se implementó un condicional de si hay una nueva línea que vuelva a buscar el siguiente token hasta tener algo diferente a una nueva línea
    #Se hace uso de un index y a este se le suma unocada vez que se manda a llamar la función para obtener el siguiente token
    def obtenerToken(self):
        global lista
        global index
        while(index == 0):
            currentToken=[]
            for token in tablaTokens:
                lista.append(token[2])
            break
        currentToken = lista[index]
        index = index +1
        if(currentToken == 'NUEVA_LINEA'):
            currentToken = self.Match(currentToken)
        return currentToken
    #Inicio del recorrido del programa
    def program(self, currentToken):
        currentToken = self.declaration_list(currentToken)
    def declaration_list(self, currentToken):
        currentToken = self.declaration(currentToken)
        currentToken = self.declaration_listPrime(currentToken)
        return currentToken
    #Esta función es la encargada de decidir si el análsis fué exitoso o si falló
    def declaration_listPrime(self, currentToken):
        currentToken = self.declaration(currentToken)
        if(currentToken == '$'):
            currentToken = self.checkFuncMain(currentToken)
            sys.exit("Parser completado correctamente")
        else: 
            sys.exit("Error sintáctico forma incorrecta de iniciar el stmt")
    def declaration(self, currentToken):
        currentToken = self.fun_declaration(currentToken)
        currentToken = self.var_declaration(currentToken)
        return currentToken
    #Esta función es la encargada de permitir las declaraciones, se asegura que se siga el orden implementado en las reglas gramáticales
    #Manda a llamar a una función para revisar primero si empieza con INT de lo contrario no entra como declaración
    def var_declaration(self, currentToken):
        currentToken = self.type_specifier(currentToken)
        if (currentToken == 'ID'):
            currentToken = self.saveVars(currentToken)
            currentToken = self.Match(currentToken)
            if (currentToken == 'SEMICOLON'):
                currentToken = self.Match(currentToken)
                print ("var_declaration")
                return currentToken
            else:
                sys.exit("Error sintácctico en var_declaration se esperaba ';' ")
        else:
            return currentToken
    def type_specifier(self, currentToken):
        if (currentToken == 'INT'):
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
    #Esta función es la encargada de iniciar el recorrido que debe seguir una función, así como empezar a llamar parametros o compunds_stmt que contenga
    #Solo puede inciiar con void o int de lo contrario truena
    def fun_declaration(self, currentToken):
        if (currentToken == 'VOID' or currentToken == 'INT'):
            print("fun_declaration")
            currentToken = self.Match(currentToken)
            if (currentToken == 'ID'):
                currentToken = self.saveVars(currentToken)
                currentToken = self.Match(currentToken)
                if (currentToken == 'PARENTESIS_ABIERTO'):
                    currentToken = self.Match(currentToken)
                    currentToken = self.params(currentToken)
                    if (currentToken == 'PARENTESIS_CERRADO'):
                        currentToken = self.Match(currentToken)
                        currentToken = self.compound_stmt(currentToken)
                        return currentToken
                    else:
                        sys.exit("Error sintáctico se esperaba ')' ")
                else:
                    sys.exit("Error sintáctico en fun_declaration se esperaba '{' ")
        else: 
            return currentToken
    def params(self, currentToken):
        currentToken = self.param_list(currentToken)
        return currentToken
    def param_list(self, currentToken):
        currentToken = self.param(currentToken)
        currentToken = self.param_listPrime(currentToken)
        return currentToken
    #Al detectar que estamos declarando parámetros y dentro se encuentra una coma esta función permite que se sigan agregando parámetros seguidos de coma hasta que llegue un paréntesis cerrado
    def param_listPrime(self, currentToken):
        if(currentToken == 'COMA'):
            currentToken = self.Match(currentToken)
            currentToken = self.param(currentToken)
            currentToken = self.param_listPrime(currentToken)
        if(currentToken == 'PARENTESIS_CERRADO'):
            return currentToken
        else:
            return currentToken
    #Función encargada de obtener todos los parámetros
    #También manda a llamar una regla semántica que le permita inicializar sus variables para poder ser usados después
    def param(self, currentToken):
        currentToken = self.type_specifier(currentToken)
        if(currentToken=='ID'):
            currentToken = self.saveVars(currentToken)
            currentToken = self.Match(currentToken)
            print("param")
            if(currentToken=='BRACKETS_ABIERTAS'):
                currentToken = self.Match(currentToken)
                if(currentToken=='BRACKETS_CERRADAS'):
                    currentToken = self.Match(currentToken)
                    return currentToken
                else:
                    sys.exit("Error sintáctico en params se esperaba ']' ")
            else:
                return currentToken
        else: 
            return currentToken
    #Al detectar una curly abierta esta función se encargará de hacer un recorrido de todo lo que se enceuntre dentro de sus curlys llamado a local declarations y statement list
    def compound_stmt(self, currentToken):
        if (currentToken == 'CURLY_ABIERTAS'):
            print("compound_stmt")
            currentToken = self.Match(currentToken)
            currentToken = self.local_declarations(currentToken)
            currentToken = self.statement_list(currentToken)
            if(currentToken=='CURLY_CERRADAS'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en compound _statement se esperaba '}' ")
        elif(currentToken != 'CURLY_ABIERTAS'):
            return currentToken
        else:
                sys.exit("Error sintáctico en compound _statement se esperaba '{' ")
    def local_declarations(self, currentToken):
        currentToken = self.local_declarationsPrime(currentToken)
        return currentToken
    #Esta función nos permite saber si se está declarando una variable dentro del compound_stmt
    def local_declarationsPrime(self, currentToken):
        if(currentToken=='INT'):
            currentToken = self.var_declaration(currentToken)
            currentToken = self.local_declarationsPrime(currentToken)
            return currentToken
        return currentToken    
    def statement_list(self, currentToken):
        currentToken = self.statement_listPrime(currentToken)
        return currentToken
    #Función que empezará a definir los statements que existen en el programa, hace llamada a la función statement en la cual existen diferentes statement que pueden existir
    def statement_listPrime(self, currentToken):
        currentToken = self.statement(currentToken)
        if(currentToken=='ID' or currentToken=='CURLY_ABIERTAS' or currentToken=='IF' or currentToken=='WHILE' or currentToken=='RETURN' or currentToken=='INPUT' or currentToken=='OUTPUT'):
            currentToken = self.statement_listPrime(currentToken)
            return currentToken
        if(currentToken=='CURLY_CERRADAS'):
            return currentToken
        else:
            return currentToken
    #Función que su objetivo es comparar los tokens que le llegan para crear el statement indicado
    def statement(self, currentToken):
        currentToken = self.call_stmt(currentToken)
        currentToken = self.assignment_stmt(currentToken)
        currentToken = self.compound_stmt(currentToken)
        currentToken = self.selection_stmt(currentToken)
        currentToken = self.iteration_stmt(currentToken)
        currentToken = self.return_stmt(currentToken)
        currentToken = self.input_stmt(currentToken)
        currentToken = self.output_stmt(currentToken)
        return currentToken
    #Función que ayuda a detectar si es una asignación
    def assignment_stmt(self, currentToken):
        currentToken = self.var(currentToken)
        if(currentToken=='ASIGNACION'):
            print("assignment_stmt")
            currentToken = self.Match(currentToken)
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en assignment se esperaba ';' ")
        else:
            return currentToken
    #Función que detecta si están haciendo una llamada a una función externa
    def call_stmt(self, currentToken):
        currentToken = self.call(currentToken)
        if(currentToken=='SEMICOLON'):
            print("call_stmt")
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
    #Función que empieza el selection_stmt
    def selection_stmt(self, currentToken):
        if(currentToken=='IF'):
            print("selection_stmt")
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                currentToken = self.Match(currentToken)
                currentToken = self.expression(currentToken)
                if(currentToken=='PARENTESIS_CERRADO'):
                    currentToken = self.Match(currentToken)
                    currentToken = self.statement(currentToken)
                    return currentToken
                    if(currentToken=='ELSE'):
                        self.Match(currentToken)
                        self.statement(currentToken)
                else:
                    sys.exit("Error sintáctico en selection_ stmt se esperaba ')")
            else: sys.exit("Error sintáctico en intento de selection se esperaba '('")
        else:
            return currentToken
    #Función que devuelve el iteration statement
    def iteration_stmt(self, currentToken):
        if(currentToken=='WHILE'):
            print("iteration_stmt")
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                currentToken = self.Match(currentToken)
                currentToken = self.expression(currentToken)
                if(currentToken=='PARENTESIS_CERRADO'):
                    currentToken = self.Match(currentToken)
                    currentToken = self.statement(currentToken)
                    return currentToken
                else:
                    sys.exit("Error sintáctico en iteration_stmt se esperaba: ')' ")
            else: 
                sys.exit("Error sintáctico en intento de iteration se esperaba '('")
        else:
            return currentToken
    #Función que devuelve el return stmt
    def return_stmt(self, currentToken):
        if(currentToken=='RETURN'):
            print("return_stmt")
            currentToken = self.Match(currentToken)
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
                return currentToken
            else: 
                sys.exit("Error sintáctico en return_stmt se esperaba: ';'")
        else:
            return currentToken
    #Función que devuelve el input statement
    def input_stmt(self, currentToken):
        if(currentToken=='INPUT'):
            print("input_stmt")
            currentToken= self.Match(currentToken)
            if(currentToken != 'ID'):
                sys.exit("Error sintáctico no se encontraron las variables requeridas para el input")
            currentToken= self.var(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken= self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en input_stmt se esperaba ';'")
        else:
            return currentToken
    #Función que devuelve el output statement
    def output_stmt(self, currentToken):
        if(currentToken=='OUTPUT'):
            print("output_stmt")
            currentToken = self.Match(currentToken)
            if(currentToken != 'ID'):
                sys.exit("Error sintáctico no se encontraron las variables requeridas para el output")
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en output_stmt se esperaba ';' ")
        else: 
            return currentToken
    #Esta función es la encargada de revisar y definir variables si encuentra un ID solo o con Brackets definir
    #Hace llamada a una regla semántica encargada de definir si la variable quese planea usar ya fue declarada anteriormente
    def var(self, currentToken):
        if(currentToken=='ID'):
            print("var")
            currentToken = self.checkVars(currentToken)
            currentToken = self.Match(currentToken)
            if(currentToken=='BRACKETS_ABIERTAS'):
                currentToken = self.Match(currentToken)
                currentToken = self.arithmetic_expression(currentToken)
                if(currentToken=='BRACKETS_CERRADAS'):
                    currentToken = self.Match(currentToken)
                    return currentToken
                else:
                    sys.exit("Error sintáctico en var se esperaba ']' ")
            else: 
                return currentToken
        else: 
            return currentToken
    #La expression se encarga que las operaciones tnegan sentido, si se está haciendo una suma este debe tener un valor después de la suma o resta
    def expression(self, currentToken):
        if(currentToken == 'SEMICOLON'):
            sys.exit("Error sintáctico no se encontraron valores después del '=' ")
        if(currentToken == 'MENOR_IGUAL_QUE' or currentToken == 'MENOR_QUE' or currentToken == 'MAYOR_QUE' or currentToken == 'MAYOR' or currentToken == 'MAYOR_IGUAL_QUE' or currentToken == 'MENOR'):
            sys.exit("Error sintáctico no se encontraron valores para crear la expresión")
        currentToken = self.arithmetic_expression(currentToken)
        currentToken = self.relop(currentToken)
        currentToken = self.arithmetic_expression(currentToken)
        currentToken = self.arithmetic_expression(currentToken)
        return currentToken
    #Función encargada de revisar si se está siguiendo la expresión que debe existir cuando existe algún relop
    def relop(self, currentToken):
        if(currentToken=='MENOR_IGUAL_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            if(currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
                return currentToken
            else:
                sys.exit("No se encontraron valores después de la condicionante")
        elif(currentToken=='MENOR_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            if(currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
                return currentToken
            else:
                sys.exit("No se encontraron valores después de la condicionante")      
        elif(currentToken=='MAYOR_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            if(currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
                return currentToken
            else:
                sys.exit("No se encontraron valores después de la condicionante")
        elif(currentToken=='MAYOR_IGUAL_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            if(currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
                return currentToken
            else:
                sys.exit("No se encontraron valores después de la condicionante")
        elif(currentToken=='IGUAL_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            if(currentToken != 'PARENTESIS_ABIERTO' or currentToken != 'INT' or currentToken != 'ID' or currentToken != 'NUM'):
                return currentToken
            else:
                sys.exit("No se encontraron valores después de la condicionante")
        elif(currentToken=='ES_DIFERENTE'):
            print("relop")
            currentToken = self.Match(currentToken)
            if(currentToken != 'PARENTESIS_ABIERTO' or currentToken != 'INT' or currentToken != 'ID' or currentToken != 'NUM'):
                return currentToken
            else:
                sys.exit("No se encontraron valores después de la condicionante")
        else:
            return currentToken
    #Las arithmetic expression son llamadas cuando existe una expresión que puede tener un asignment o sumas, restas, multiplicaciones, etc
    def arithmetic_expression(self, currentToken):
        currentToken = self.term(currentToken)
        currentToken = self.arithmetic_expressionPrime(currentToken)
        return currentToken
    def arithmetic_expressionPrime(self, currentToken):
        currentToken = self.addop(currentToken)
        if (currentToken == 'SUMA' or currentToken == 'RESTA'):
            print("arithmetic_expression")
            currentToken = self.arithmetic_expressionPrime(currentToken)
            return currentToken
        currentToken = self.term(currentToken)
        if (currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
            print("arithmetic_expression")
            currentToken = self.arithmetic_expressionPrime(currentToken)
            return currentToken
        if (currentToken == 'CURLY_CERRADAS'):
            return currentToken
        else:
            return currentToken
    #Función encargada de revisar el formato que debe tener la operación 
    def addop(self, currentToken):
        if(currentToken=='SUMA'):
            print("addop")
            currentToken = self.Match(currentToken)
            if(currentToken == 'SEMICOLON'):
                sys.exit("Error de sintaxis se esperaba un valor después de '+' ")
            return currentToken
        elif(currentToken=='RESTA'):
            print("addop")
            currentToken = self.Match(currentToken)
            if(currentToken == 'SEMICOLON'):
                sys.exit("Error de sintaxis se esperaba un valor después de '-' ")
            return currentToken
        else: 
            return currentToken
    #Función que nos ayuda a saber si lo que viene es una expresión airtmética, variable, llamada o número
    def term(self, currentToken):
        currentToken = self.factor(currentToken)
        if (currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
            currentToken = self.termPrime(currentToken)
            return currentToken
        return currentToken
    #En dado caso que encuentre una expresión aritmética entran estas condicionales para implementar sus respectivas operaciones
    def termPrime(self, currentToken):
        currentToken = self.mulop(currentToken)
        if(currentToken=='MULTIPLICACION' or currentToken=='DIVISION'):
            currentToken = self.termPrime(currentToken)
            return currentToken
        currentToken =self.factor(currentToken)
        if(currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
            currentToken = self.termPrime(currentToken)
            return currentToken
        if(currentToken == 'SUMA' or currentToken == 'RESTA' or currentToken == 'SEMICOLON'):
            return currentToken
        return currentToken
    #Función encargada de implementar las reglas de mulop
    def mulop(self, currentToken):
        if(currentToken=='MULTIPLICACION'):
            print("mulop")
            currentToken = self.Match(currentToken)
        elif(currentToken=='DIVISION'):
            print("mulop")
            currentToken = self.Match(currentToken)
        else: 
            return currentToken
    #Tiene una regla implementada que no permite el uso de números negativos
    #Encargado de definir el tipo de regla que se deverá seguir
    def factor(self, currentToken):
        if (currentToken == 'RESTA'):
            sys.exit("Error no se permiten números negativos")
        if (currentToken == 'PARENTESIS_ABIERTO'):
            print("factor")
            currentToken = self.Match(currentToken)
            currentToken = self.arithmetic_expression(currentToken)
            return currentToken
            if(currentToken == 'PARENTESIS_CERRADO'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en factor se esperaba ')' ")
        currentToken = self.var(currentToken)
        currentToken = self.call(currentToken)
        if(currentToken=='NUM'):
            print("numero")
            currentToken = self.Match(currentToken)
            return currentToken
        else: 
            return currentToken
    #Función encargada de definir la regla de una llamada
    def call(self, currentToken):
        if(currentToken=='ID'):
            currentToken = self.checkVars(currentToken)
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                print("call")
                currentToken = self.Match(currentToken)
                currentToken = self.args(currentToken)
                return currentToken
                if(currentToken=='PARENTESIS_CERRADO'):
                    self.Match(currentToken)
                else:
                    sys.exit("Error Sintáctico en call se esperaba ')' ")
            else:
                return currentToken
        else:
            return currentToken
    #Funciones args nos permite revisar si en nuestro código tenemos variables con múltiples parámetros
    def args(self, currentToken):
        currentToken = self.args_list(currentToken)
        if(currentToken=='PARENTESIS_CERRADO'):
            currentToken = self.Match(currentToken)
            return currentToken
    def args_list(self, currentToken):
        currentToken = self.arithmetic_expression(currentToken)
        currentToken = self.args_listPrime(currentToken)
        return currentToken
    def args_listPrime(self, currentToken):
        if(currentToken=='COMA'):
            currentToken = self.Match(currentToken)
            currentToken = self.arithmetic_expression(currentToken)
            currentToken = self.args_listPrime(currentToken)
            return currentToken
        if(currentToken=='PARENTESIS_CERRADO'):
            return currentToken
    #Función encargada de hacer Match cuando se encuentra algún token terminar en las funciones anteriores
    #Esta función es la encargada de mandar a llamar la regla para obtener el siguiente token y devolver el token obtenido 
    def Match(self, currentToken):
        if(currentToken == 'NUEVA_LINEA' or currentToken=='VOID' or currentToken=='SUMA' or currentToken=='RESTA' or currentToken=='MULTIPLICACION' or currentToken=='DIVISION' or currentToken=='MAYOR_QUE' or currentToken=='MAYOR_IGUAL_QUE' or currentToken=='MENOR_QUE' or 
        currentToken=='MENOR_IGUAL_QUE' or currentToken=='IGUAL_QUE' or currentToken=='ES_DIFERENTE' or currentToken=='ASIGNACION' or currentToken=='SEMICOLON' or currentToken=='COMA' or 
        currentToken=='PARENTESIS_ABIERTO' or currentToken=='PARENTESIS_CERRADO' or currentToken=='BRACKETS_ABIERTAS' or currentToken=='BRACKETS_CERRADAS' or currentToken=='CURLY_ABIERTAS' or
        currentToken=='CURLY_CERRADAS' or currentToken=='NUM' or currentToken=='ID' or currentToken=='ELSE' or currentToken=='IF' or currentToken=='INT' or currentToken=='RETURN' or
        currentToken=='WHILE' or currentToken=='INPUT' or currentToken=='OUTPUT'):
            currentToken = a.obtenerToken()
            return currentToken
    # Lógica Semántica
    #Esta función se encarga de estar guardando las variables que se declararon en el programa para después poder usarse
    #Se le implementó una operación que revisa si la variable encontrada se está volviendo a implementar mediante un bool
    def saveVars(self, currentToken):
        global variablesDeclaradas
        variablesDeclaradas.append(tablaTokens[index-1][1])
        duplicados = set(variablesDeclaradas)
        contains_duplicates = len(variablesDeclaradas) != len(duplicados)
        if (contains_duplicates == True):
            sys.exit("Error se está declarando una variable anteriormente declarada")
        return currentToken
    #Función encargada de revisar si la variable que se desea usar ya fue declarada anteriormente
    #Tiene una condicional immplementada la cual se encarga de revisar si la variable que se obtuvo se encuentra en la lista de variables ya declaradas anteriormente
    def checkVars(self, currentToken):
        global variable
        count = 0
        variable.append(tablaTokens[index-1][1])
        if ("".join(variable) in variablesDeclaradas):
            variable.pop()
            return currentToken
        else:
            sys.exit("Error variable no declarada " + str(variable))
    #función encargada de revisar sila función void main existe, de no ser así truena debido a que es necesario que exista una
    def checkFuncMain(self, currentToken):
        global variableGuardada
        for i in tablaTokens:
            variableGuardada.append(i[1])
        requeridos=['main', 'void']
        if('void' in variableGuardada):
            if('main' in variableGuardada):
                if('(' in variableGuardada):
                    if(')' in variableGuardada):
                        return currentToken
                    else:
                        sys.exit("Error")
                else:
                    sys.exit("Error")
            else:
                sys.exit("Error no existe función main")
        return currentToken

a = sintax()
a.main()