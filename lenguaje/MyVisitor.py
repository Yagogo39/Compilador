from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory={}

#Definir la asignacion
def visitAssign(self, context):
    name=context.ID().getText()
    value=self.visit(context.expr())
    self.memory[name]=value

def visitPrint(self, contexto):
    value=self.visit(contexto.expr())
    print(value)
