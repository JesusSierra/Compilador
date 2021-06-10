import sys
from analizadorLexico import *

tablaTokens=[]
tipoToken=""
index = 0
index2 = -1
tokenAnterior=""
lista =[]
currentToken = ""
compound_stmtFlag = False


class sintax:   
    global compound_stmtFlag
    def main(self):
        global tablaTokens
        global tipoToken
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
            sys.exit("Error sintáctico")
    def declaration(self, currentToken):
        currentToken = self.var_declaration(currentToken)
        currentToken = self.fun_declaration(currentToken)
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
            return currentToken
    def type_specifier(self, currentToken):
        if (currentToken == 'INT'):
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
    def fun_declaration(self, currentToken):
        if (currentToken == 'VOID'):
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
                        sys.exit("Error sintáctico")
                else:
                    sys.exit("Error sintáctico")
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
            self.param(currentToken)
            self.param_listPrime(currentToken)
        if(currentToken == 'PARENTESIS_CERRADO'):
            return currentToken
        else:
            sys.exit("Error sintáctico")
    def param(self, currentToken):
        self.type_specifier(currentToken)
        if(currentToken=='ID'):
            currentToken = self.Match(currentToken)
            if(currentToken=='BRACKETS_ABIERTAS'):
                currentToken = self.Match(currentToken)
                if(currentToken=='BRACKETS_CERRADAS'):
                    currentToken = self.Match(currentToken)
                else:
                    sys.exit("Error sintáctico")
            else:
                return currentToken
        else: 
            return currentToken
    def compound_stmt(self, currentToken):
        if (currentToken == 'CURLY_ABIERTAS'):
            currentToken = self.Match(currentToken)
            currentToken = self.local_declarations(currentToken)
            currentToken = self.statement_list(currentToken)
            if(currentToken=='CURLY_CERRADAS'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico")
        else:
            return currentToken
    def local_declarations(self, currentToken):
        currentToken = self.local_declarationsPrime(currentToken)
        return currentToken
    def local_declarationsPrime(self, currentToken):
        currentToken = self.var_declaration(currentToken)
        if(currentToken=='INT' or currentToken=='ID' or currentToken=='CURLY_ABIERTAS' or currentToken=='IF' or currentToken=='WHILE' or currentToken=='RETURN' or currentToken=='INPUT' or currentToken=='OUTPUT'):
            
            return currentToken
        else:
            return currentToken
    def statement_list(self, currentToken):
        currentToken = self.statement_listPrime(currentToken)
        return currentToken
    def statement_listPrime(self, currentToken):
        currentToken = self.statement(currentToken)
        if(currentToken=='ID' or currentToken=='CURLY_ABIERTAS' or currentToken=='IF' or currentToken=='WHILE' or currentToken=='RETURN' or currentToken=='INPUT' or currentToken=='OUTPUT'):
            currentToken = self.statement(currentToken)
            return currentToken
        if(currentToken=='CURLY_CERRADAS'):
            currentToken = self.Match(currentToken)
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
            currentToken = self.Match(currentToken)
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico")
        else:
            return currentToken
    def call_stmt(self, currentToken):
        currentToken = self.call(currentToken)
        if(currentToken=='SEMICOLON'):
            currentToken = self.Match(currentToken)
            return currentToken
        else:
            return currentToken
    def selection_stmt(self, currentToken):
        if(currentToken=='IF'):
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                currentToken = self.Match(currentToken)
                currentToken = self.expression(currentToken)
                if(currentToken=='PARENTESIS_CERRADO'):
                    currentToken = self.Match(currentToken)
                    currentToken = self.statement(currentToken)
        elif(currentToken=='IF'):
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                currentToken = self.Match(currentToken)
                currentToken = self.expression(currentToken)
                if(currentToken=='PARENTESIS_CERRADO'):
                    self.Match(currentToken)
                    self.statement(currentToken)
                    if(currentToken=='ELSE'):
                        self.Match(currentToken)
                        self.statement(currentToken)
                    else:
                        sys.exit("Error sintáctico")
        else:
            return currentToken
    def iteration_stmt(self, currentToken):
        if(currentToken=='WHILE'):
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                currentToken = self.Match(currentToken)
                currentToken = self.expression(currentToken)
                if(currentToken=='PARENTESIS_CERRADO'):
                    currentToken = self.Match(currentToken)
                    currentToken = self.statement(currentToken)
                    return currentToken
                else:
                    sys.exit("Error sintáctico")
        else:
            return currentToken
    def return_stmt(self, currentToken):
        if(currentToken=='RETURN'):
            currentToken = self.Match(currentToken)
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
            else: 
                sys.exit("Error sintáctico se esperaba: ';'")
        else:
            return currentToken
    def input_stmt(self, currentToken):
        if(currentToken=='INPUT'):
            currentToken= self.Match(currentToken)
            currentToken= self.var(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken= self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico")
        else:
            return currentToken
    def output_stmt(self, currentToken):
        if(currentToken=='OUTPUT'):
            currentToken = self.Match(currentToken)
            currentToken = self.expression(currentToken)
            if(currentToken=='SEMICOLON'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico")
        else: 
            return currentToken
    def var(self, currentToken):
        if(currentToken=='ID'):
            currentToken = self.Match(currentToken)
            if(currentToken=='BRACKETS_ABIERTAS'):
                currentToken = self.Match(currentToken)
                currentToken = self.arithmetic_expression(currentToken)
                if(currentToken=='BRACKETS_CERRADAS'):
                    currentToken = self.Match(currentToken)
                    return currentToken
                else:
                    sys.exit("Error sintáctico")
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
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='MENOR_QUE'):
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='MAYOR_QUE'):
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='MAYOR_IGUAL_QUE'):
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='IGUAL_QUE'):
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='ES_DIFERENTE'):
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
        if (currentToken == 'CURLY_CERRADAS'):
            return currentToken
        currentToken = self.term(currentToken)
        if (currentToken == 'CURLY_CERRADAS'):
            return currentToken
        else:
            return currentToken
    def addop(self, currentToken):
        if(currentToken=='SUMA'):
            currentToken = self.Match(currentToken)
            return currentToken
        elif(currentToken=='RESTA'):
            currentToken = self.Match(currentToken)
            return currentToken
        else: 
            return currentToken
    def term(self, currentToken):
        currentToken = self.factor(currentToken)
        currentToken = self.termPrime(currentToken)
        return currentToken
    def termPrime(self, currentToken):
        currentToken = self.mulop(currentToken)
        if(currentToken=='SUMA' or currentToken=='RESTA' or currentToken=='PARENTESIS_ABIERTO' or currentToken=='INT' or currentToken=='ID' or currentToken=='NUM' or currentToken=='SEMICOLON'):
            return currentToken
        currentToken =self.factor(currentToken)
        if(currentToken=='SUMA' or currentToken=='RESTA' or currentToken=='PARENTESIS_ABIERTO' or currentToken=='INT' or currentToken=='ID' or currentToken=='NUM' or currentToken=='SEMICOLON'):
            return currentToken
        else:
            return currentToken
    def mulop(self, currentToken):
        if(currentToken=='MULTIPLICACION'):
            currentToken = self.Match(currentToken)
        elif(currentToken=='DIVISION'):
            currentToken = self.Match(currentToken)
        else: 
            return currentToken
    def factor(self, currentToken):
        if (currentToken == 'PARENTESIS_ABIERTO'):
            currentToken = self.Match(currentToken)
            currentToken = self.arithmetic_expression(currentToken)
            return currentToken
            if(currentToken == 'PARENTESIS_CERRADO'):
                currentToken = self.Match(currentToken)
                return currentToken
            else:
                sys.exit("Error sintáctico")
        currentToken = self.var(currentToken)
        currentToken = self.call(currentToken)
        if(currentToken=='NUM'):
            currentToken = self.Match(currentToken)
            return currentToken
        else: 
            return currentToken
    def call(self, currentToken):
        if(currentToken=='ID'):
            currentToken = self.Match(currentToken)
            if(currentToken=='PARENTESIS_ABIERTO'):
                currentToken = self.Match(currentToken)
                currentToken = self.args(currentToken)
                return currentToken
                if(currentToken=='PARENTESIS_CERRADO'):
                    self.Match(currentToken)
                else:
                    sys.exit("Error Sintáctico")
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