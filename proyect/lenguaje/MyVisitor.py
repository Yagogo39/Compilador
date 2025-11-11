from .GrammarVisitor import GrammarVisitor

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory={}

#Definir la asignacion
def visitAssign(self, ctx):
    #Se obtiene el nombre de la variable y su valor
    name=ctx.ID().getText()
    #Se obtiene el valor, ya sea un numero o una expresion
    value=self.visit(ctx.expr())
    #Se almacena en la memoria a partir del nombre y el valor
    self.memory[name]=value

def visitPrint(self, ctx):
    #Definimos la expresion que se desea mostrar
    value=self.visit(ctx.expr())
    #Imprimimos el valor en pantalla
    print(value)

#Definimos las expresiones
def visitExpr(self, ctx):
    #Busca si existen ID'S
    if ctx.ID():
        #Si el nombre de la variable no esta en memoria, lanza un error
        name = ctx.ID().getText()
        if name not in self.memory:
            raise NameError(f"Variable '{name}' no definida")
        # Si existe el nombre regresa la variable
        return self.memory[name]
    #Busca el operador numerico
    elif ctx.op:
        #Visita y obtiene lado izquierdo y derecho
        left=self.visit(ctx.expr(0))
        right=self.visit(ctx.expr(1))
        #Evalua la operacion a realizar
        if ctx.op.text=='+':
            return left + right
        if ctx.op.text=='-':
            return left - right
        if ctx.op.text=='*':
            return left * right
        if ctx.op.text=='/':
            #Verifica que no se divida entre cero
            if right == 0:
                raise ValueError("Division por cero")
            return left / right


