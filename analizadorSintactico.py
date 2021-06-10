import sys
from analizadorLexico import *

tablaTokens=[]
index = 0
lista =[]
currentToken = ""


class sintax:   
    def main(self):
        global tablaTokens
        tablaTokens = tokens
        currentToken = a.obtenerToken()
        lista.pop()
        lista.append('$')
        a.program(currentToken)

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

    def program(self, currentToken):
        currentToken = self.declaration_list(currentToken)
    def declaration_list(self, currentToken):
        currentToken = self.declaration(currentToken)
        currentToken = self.declaration_listPrime(currentToken)
        return currentToken
    def declaration_listPrime(self, currentToken):
        currentToken = self.declaration(currentToken)
        if(currentToken == '$'):
            sys.exit("Parser completado correctamente")
        else: 
            sys.exit("Error sintáctico forma incorrecta de iniciar el stmt")
    def declaration(self, currentToken):
        currentToken = self.fun_declaration(currentToken)
        currentToken = self.var_declaration(currentToken)
        return currentToken
    def var_declaration(self, currentToken):
        currentToken = self.type_specifier(currentToken)
        if (currentToken == 'ID'):
            currentToken = self.Match(currentToken)
            if (currentToken == 'SEMICOLON'):
                currentToken = self.Match(currentToken)
                print ("var_declaration")
                return currentToken
            else:
                sys.exit("Error sintácctico se esperaba ';' ")
        else:
            return currentToken
    def type_specifier(self, currentToken):
        if (currentToken == 'INT'):
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
    def fun_declaration(self, currentToken):
        if (currentToken == 'VOID' or currentToken == 'INT'):
            print("fun_declaration")
            currentToken = self.Match(currentToken)
            if (currentToken == 'ID'):
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
    def param_listPrime(self, currentToken):
        if(currentToken == 'COMA'):
            currentToken = self.Match(currentToken)
            currentToken = self.param(currentToken)
            currentToken = self.param_listPrime(currentToken)
        if(currentToken == 'PARENTESIS_CERRADO'):
            return currentToken
        else:
            return currentToken
    def param(self, currentToken):
        currentToken = self.type_specifier(currentToken)
        if(currentToken=='ID'):
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
                sys.exit("Error sintáctico se esperaba '}' ")
        elif(currentToken != 'CURLY_ABIERTAS'):
            return currentToken
        else:
                sys.exit("Error sintáctico se esperaba '{' ")
    def local_declarations(self, currentToken):
        currentToken = self.local_declarationsPrime(currentToken)
        return currentToken
    def local_declarationsPrime(self, currentToken):
        if(currentToken=='INT'):
            currentToken = self.var_declaration(currentToken)
            currentToken = self.local_declarationsPrime(currentToken)
            return currentToken
        return currentToken    
    def statement_list(self, currentToken):
        currentToken = self.statement_listPrime(currentToken)
        return currentToken
    def statement_listPrime(self, currentToken):
        currentToken = self.statement(currentToken)
        if(currentToken=='ID' or currentToken=='CURLY_ABIERTAS' or currentToken=='IF' or currentToken=='WHILE' or currentToken=='RETURN' or currentToken=='INPUT' or currentToken=='OUTPUT'):
            currentToken = self.statement_listPrime(currentToken)
            return currentToken
        if(currentToken=='CURLY_CERRADAS'):
            return currentToken
        else:
            return currentToken
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
    def call_stmt(self, currentToken):
        currentToken = self.call(currentToken)
        if(currentToken=='SEMICOLON'):
            print("call_stmt")
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
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
        else:
            return currentToken
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
            return currentToken
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
    def input_stmt(self, currentToken):
        if(currentToken=='INPUT'):
            print("input_stmt")
            currentToken= self.Match(currentToken)
            currentToken= self.var(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken= self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en input_stmt se esperaba ';'")
        else:
            return currentToken
    def output_stmt(self, currentToken):
        if(currentToken=='OUTPUT'):
            print("output_stmt")
            currentToken = self.Match(currentToken)
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico en output_stmt se esperaba ';' ")
        else: 
            return currentToken
    def var(self, currentToken):
        if(currentToken=='ID'):
            print("var")
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
    def expression(self, currentToken):
        currentToken = self.arithmetic_expression(currentToken)
        currentToken = self.relop(currentToken)
        currentToken = self.arithmetic_expression(currentToken)
        currentToken = self.arithmetic_expression(currentToken)
        return currentToken
    def relop(self, currentToken):
        if(currentToken=='MENOR_IGUAL_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='MENOR_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='MAYOR_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='MAYOR_IGUAL_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='IGUAL_QUE'):
            print("relop")
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='ES_DIFERENTE'):
            print("relop")
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
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
    def addop(self, currentToken):
        if(currentToken=='SUMA'):
            print("addop")
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='RESTA'):
            print("addop")
            currentToken = self.Match(currentToken)
            return currentToken
        else: 
            return currentToken
    def term(self, currentToken):
        currentToken = self.factor(currentToken)
        if (currentToken == 'PARENTESIS_ABIERTO' or currentToken == 'INT' or currentToken == 'ID' or currentToken == 'NUM'):
            currentToken = self.termPrime(currentToken)
            return currentToken
        return currentToken
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
    def mulop(self, currentToken):
        if(currentToken=='MULTIPLICACION'):
            print("mulop")
            currentToken = self.Match(currentToken)
        elif(currentToken=='DIVISION'):
            print("mulop")
            currentToken = self.Match(currentToken)
        else: 
            return currentToken
    def factor(self, currentToken):
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
            print("factor")
            currentToken = self.Match(currentToken)
            return currentToken
        else: 
            return currentToken
    def call(self, currentToken):
        if(currentToken=='ID'):
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
    def Match(self, currentToken):
        if(currentToken == 'NUEVA_LINEA' or currentToken=='VOID' or currentToken=='SUMA' or currentToken=='RESTA' or currentToken=='MULTIPLICACION' or currentToken=='DIVISION' or currentToken=='MAYOR_QUE' or currentToken=='MAYOR_IGUAL_QUE' or currentToken=='MENOR_QUE' or 
        currentToken=='MENOR_IGUAL_QUE' or currentToken=='IGUAL_QUE' or currentToken=='ES_DIFERENTE' or currentToken=='ASIGNACION' or currentToken=='SEMICOLON' or currentToken=='COMA' or 
        currentToken=='PARENTESIS_ABIERTO' or currentToken=='PARENTESIS_CERRADO' or currentToken=='BRACKETS_ABIERTAS' or currentToken=='BRACKETS_CERRADAS' or currentToken=='CURLY_ABIERTAS' or
        currentToken=='CURLY_CERRADAS' or currentToken=='NUM' or currentToken=='ID' or currentToken=='ELSE' or currentToken=='IF' or currentToken=='INT' or currentToken=='RETURN' or
        currentToken=='WHILE' or currentToken=='INPUT' or currentToken=='OUTPUT'):
            # index = index + 1
            # index2 = index2 + 1
            currentToken = a.obtenerToken()
            return currentToken


a = sintax()
a.main()