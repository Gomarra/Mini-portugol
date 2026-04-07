# Generated from miniportugol.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,
        1,1,1,1,1,1,3,1,44,8,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,52,8,2,1,2,1,
        2,1,3,1,3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,82,8,6,1,6,
        1,6,1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,6,1,6,3,6,95,8,6,1,7,1,
        7,3,7,99,8,7,1,7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,1,7,1,7,3,
        7,111,8,7,1,8,1,8,1,8,1,8,3,8,117,8,8,1,8,1,8,1,8,1,8,5,8,123,8,
        8,10,8,12,8,126,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,136,8,9,
        10,9,12,9,139,9,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,3,13,154,8,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,0,3,1,0,1,4,1,0,5,7,1,0,8,9,159,0,31,1,0,0,0,2,43,1,
        0,0,0,4,48,1,0,0,0,6,55,1,0,0,0,8,65,1,0,0,0,10,71,1,0,0,0,12,77,
        1,0,0,0,14,96,1,0,0,0,16,112,1,0,0,0,18,129,1,0,0,0,20,142,1,0,0,
        0,22,144,1,0,0,0,24,146,1,0,0,0,26,153,1,0,0,0,28,30,3,6,3,0,29,
        28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,37,1,0,0,
        0,33,31,1,0,0,0,34,36,3,26,13,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,
        1,0,0,0,37,38,1,0,0,0,38,1,1,0,0,0,39,37,1,0,0,0,40,41,3,22,11,0,
        41,42,5,24,0,0,42,44,1,0,0,0,43,40,1,0,0,0,43,44,1,0,0,0,44,45,1,
        0,0,0,45,46,3,20,10,0,46,47,5,24,0,0,47,3,1,0,0,0,48,49,5,17,0,0,
        49,51,5,24,0,0,50,52,3,2,1,0,51,50,1,0,0,0,51,52,1,0,0,0,52,53,1,
        0,0,0,53,54,5,18,0,0,54,5,1,0,0,0,55,56,3,24,12,0,56,60,5,24,0,0,
        57,59,5,24,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,
        0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,19,0,0,64,7,1,0,0,0,65,
        66,5,12,0,0,66,67,5,17,0,0,67,68,5,23,0,0,68,69,5,18,0,0,69,70,5,
        19,0,0,70,9,1,0,0,0,71,72,5,11,0,0,72,73,5,17,0,0,73,74,5,24,0,0,
        74,75,5,18,0,0,75,76,5,19,0,0,76,11,1,0,0,0,77,78,5,13,0,0,78,79,
        5,17,0,0,79,81,5,24,0,0,80,82,3,2,1,0,81,80,1,0,0,0,81,82,1,0,0,
        0,82,83,1,0,0,0,83,84,5,18,0,0,84,85,5,20,0,0,85,89,3,26,13,0,86,
        88,3,26,13,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,
        0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,94,5,21,0,0,93,95,3,14,7,0,94,
        93,1,0,0,0,94,95,1,0,0,0,95,13,1,0,0,0,96,98,5,14,0,0,97,99,3,4,
        2,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,20,0,0,
        101,105,3,26,13,0,102,104,3,26,13,0,103,102,1,0,0,0,104,107,1,0,
        0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,
        0,0,108,110,5,21,0,0,109,111,3,14,7,0,110,109,1,0,0,0,110,111,1,
        0,0,0,111,15,1,0,0,0,112,113,5,15,0,0,113,114,5,17,0,0,114,116,5,
        24,0,0,115,117,3,2,1,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,1,
        0,0,0,118,119,5,18,0,0,119,120,5,20,0,0,120,124,3,26,13,0,121,123,
        3,26,13,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,21,0,0,128,17,
        1,0,0,0,129,130,5,24,0,0,130,131,5,22,0,0,131,137,5,24,0,0,132,133,
        3,22,11,0,133,134,5,24,0,0,134,136,1,0,0,0,135,132,1,0,0,0,136,139,
        1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,137,
        1,0,0,0,140,141,5,19,0,0,141,19,1,0,0,0,142,143,7,0,0,0,143,21,1,
        0,0,0,144,145,7,1,0,0,145,23,1,0,0,0,146,147,7,2,0,0,147,25,1,0,
        0,0,148,154,3,8,4,0,149,154,3,10,5,0,150,154,3,12,6,0,151,154,3,
        16,8,0,152,154,3,18,9,0,153,148,1,0,0,0,153,149,1,0,0,0,153,150,
        1,0,0,0,153,151,1,0,0,0,153,152,1,0,0,0,154,27,1,0,0,0,15,31,37,
        43,51,60,81,89,94,98,105,110,116,124,137,153
    ]

class miniportugolParser ( Parser ):

    grammarFileName = "miniportugol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'&&'", "'||'", "'=!'", "'+'", 
                     "'-'", "'/'", "'INT'", "'String'", "<INVALID>", "'leia'", 
                     "'escreva'", "'se'", "'senao'", "'enquanto'", "'para'", 
                     "'('", "')'", "';'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WS", "LEIA", "ESCREVA", 
                      "SE", "SENAO", "ENQUANTO", "PARA", "AP", "FP", "PV", 
                      "AC", "FC", "IGUAL", "STRING", "ID" ]

    RULE_program = 0
    RULE_cond_op = 1
    RULE_condicao = 2
    RULE_declaracao_variavel = 3
    RULE_comando_escreva = 4
    RULE_comando_ler = 5
    RULE_comando_se = 6
    RULE_comando_senao = 7
    RULE_comando_enquanto = 8
    RULE_comando_definir = 9
    RULE_expr_condicionais = 10
    RULE_expr_aritmeticas = 11
    RULE_tipos_variaveis = 12
    RULE_lista_comandos = 13

    ruleNames =  [ "program", "cond_op", "condicao", "declaracao_variavel", 
                   "comando_escreva", "comando_ler", "comando_se", "comando_senao", 
                   "comando_enquanto", "comando_definir", "expr_condicionais", 
                   "expr_aritmeticas", "tipos_variaveis", "lista_comandos" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    WS=10
    LEIA=11
    ESCREVA=12
    SE=13
    SENAO=14
    ENQUANTO=15
    PARA=16
    AP=17
    FP=18
    PV=19
    AC=20
    FC=21
    IGUAL=22
    STRING=23
    ID=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_variavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniportugolParser.Declaracao_variavelContext)
            else:
                return self.getTypedRuleContext(miniportugolParser.Declaracao_variavelContext,i)


        def lista_comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniportugolParser.Lista_comandosContext)
            else:
                return self.getTypedRuleContext(miniportugolParser.Lista_comandosContext,i)


        def getRuleIndex(self):
            return miniportugolParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = miniportugolParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 28
                self.declaracao_variavel()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16824320) != 0):
                self.state = 34
                self.lista_comandos()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_condicionais(self):
            return self.getTypedRuleContext(miniportugolParser.Expr_condicionaisContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(miniportugolParser.ID)
            else:
                return self.getToken(miniportugolParser.ID, i)

        def expr_aritmeticas(self):
            return self.getTypedRuleContext(miniportugolParser.Expr_aritmeticasContext,0)


        def getRuleIndex(self):
            return miniportugolParser.RULE_cond_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_op" ):
                listener.enterCond_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_op" ):
                listener.exitCond_op(self)




    def cond_op(self):

        localctx = miniportugolParser.Cond_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cond_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                self.state = 40
                self.expr_aritmeticas()
                self.state = 41
                self.match(miniportugolParser.ID)


            self.state = 45
            self.expr_condicionais()
            self.state = 46
            self.match(miniportugolParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(miniportugolParser.AP, 0)

        def ID(self):
            return self.getToken(miniportugolParser.ID, 0)

        def FP(self):
            return self.getToken(miniportugolParser.FP, 0)

        def cond_op(self):
            return self.getTypedRuleContext(miniportugolParser.Cond_opContext,0)


        def getRuleIndex(self):
            return miniportugolParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)




    def condicao(self):

        localctx = miniportugolParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condicao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(miniportugolParser.AP)
            self.state = 49
            self.match(miniportugolParser.ID)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0):
                self.state = 50
                self.cond_op()


            self.state = 53
            self.match(miniportugolParser.FP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_variavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipos_variaveis(self):
            return self.getTypedRuleContext(miniportugolParser.Tipos_variaveisContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(miniportugolParser.ID)
            else:
                return self.getToken(miniportugolParser.ID, i)

        def PV(self):
            return self.getToken(miniportugolParser.PV, 0)

        def getRuleIndex(self):
            return miniportugolParser.RULE_declaracao_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_variavel" ):
                listener.enterDeclaracao_variavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_variavel" ):
                listener.exitDeclaracao_variavel(self)




    def declaracao_variavel(self):

        localctx = miniportugolParser.Declaracao_variavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao_variavel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.tipos_variaveis()
            self.state = 56
            self.match(miniportugolParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 57
                self.match(miniportugolParser.ID)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(miniportugolParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_escrevaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCREVA(self):
            return self.getToken(miniportugolParser.ESCREVA, 0)

        def AP(self):
            return self.getToken(miniportugolParser.AP, 0)

        def STRING(self):
            return self.getToken(miniportugolParser.STRING, 0)

        def FP(self):
            return self.getToken(miniportugolParser.FP, 0)

        def PV(self):
            return self.getToken(miniportugolParser.PV, 0)

        def getRuleIndex(self):
            return miniportugolParser.RULE_comando_escreva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_escreva" ):
                listener.enterComando_escreva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_escreva" ):
                listener.exitComando_escreva(self)




    def comando_escreva(self):

        localctx = miniportugolParser.Comando_escrevaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comando_escreva)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(miniportugolParser.ESCREVA)
            self.state = 66
            self.match(miniportugolParser.AP)
            self.state = 67
            self.match(miniportugolParser.STRING)
            self.state = 68
            self.match(miniportugolParser.FP)
            self.state = 69
            self.match(miniportugolParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_lerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEIA(self):
            return self.getToken(miniportugolParser.LEIA, 0)

        def AP(self):
            return self.getToken(miniportugolParser.AP, 0)

        def ID(self):
            return self.getToken(miniportugolParser.ID, 0)

        def FP(self):
            return self.getToken(miniportugolParser.FP, 0)

        def PV(self):
            return self.getToken(miniportugolParser.PV, 0)

        def getRuleIndex(self):
            return miniportugolParser.RULE_comando_ler

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_ler" ):
                listener.enterComando_ler(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_ler" ):
                listener.exitComando_ler(self)




    def comando_ler(self):

        localctx = miniportugolParser.Comando_lerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando_ler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(miniportugolParser.LEIA)
            self.state = 72
            self.match(miniportugolParser.AP)
            self.state = 73
            self.match(miniportugolParser.ID)
            self.state = 74
            self.match(miniportugolParser.FP)
            self.state = 75
            self.match(miniportugolParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_seContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(miniportugolParser.SE, 0)

        def AP(self):
            return self.getToken(miniportugolParser.AP, 0)

        def ID(self):
            return self.getToken(miniportugolParser.ID, 0)

        def FP(self):
            return self.getToken(miniportugolParser.FP, 0)

        def AC(self):
            return self.getToken(miniportugolParser.AC, 0)

        def lista_comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniportugolParser.Lista_comandosContext)
            else:
                return self.getTypedRuleContext(miniportugolParser.Lista_comandosContext,i)


        def FC(self):
            return self.getToken(miniportugolParser.FC, 0)

        def cond_op(self):
            return self.getTypedRuleContext(miniportugolParser.Cond_opContext,0)


        def comando_senao(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_senaoContext,0)


        def getRuleIndex(self):
            return miniportugolParser.RULE_comando_se

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_se" ):
                listener.enterComando_se(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_se" ):
                listener.exitComando_se(self)




    def comando_se(self):

        localctx = miniportugolParser.Comando_seContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comando_se)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(miniportugolParser.SE)
            self.state = 78
            self.match(miniportugolParser.AP)
            self.state = 79
            self.match(miniportugolParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0):
                self.state = 80
                self.cond_op()


            self.state = 83
            self.match(miniportugolParser.FP)
            self.state = 84
            self.match(miniportugolParser.AC)
            self.state = 85
            self.lista_comandos()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16824320) != 0):
                self.state = 86
                self.lista_comandos()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(miniportugolParser.FC)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 93
                self.comando_senao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_senaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SENAO(self):
            return self.getToken(miniportugolParser.SENAO, 0)

        def AC(self):
            return self.getToken(miniportugolParser.AC, 0)

        def lista_comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniportugolParser.Lista_comandosContext)
            else:
                return self.getTypedRuleContext(miniportugolParser.Lista_comandosContext,i)


        def FC(self):
            return self.getToken(miniportugolParser.FC, 0)

        def condicao(self):
            return self.getTypedRuleContext(miniportugolParser.CondicaoContext,0)


        def comando_senao(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_senaoContext,0)


        def getRuleIndex(self):
            return miniportugolParser.RULE_comando_senao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_senao" ):
                listener.enterComando_senao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_senao" ):
                listener.exitComando_senao(self)




    def comando_senao(self):

        localctx = miniportugolParser.Comando_senaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comando_senao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(miniportugolParser.SENAO)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 97
                self.condicao()


            self.state = 100
            self.match(miniportugolParser.AC)
            self.state = 101
            self.lista_comandos()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16824320) != 0):
                self.state = 102
                self.lista_comandos()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(miniportugolParser.FC)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 109
                self.comando_senao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_enquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENQUANTO(self):
            return self.getToken(miniportugolParser.ENQUANTO, 0)

        def AP(self):
            return self.getToken(miniportugolParser.AP, 0)

        def ID(self):
            return self.getToken(miniportugolParser.ID, 0)

        def FP(self):
            return self.getToken(miniportugolParser.FP, 0)

        def AC(self):
            return self.getToken(miniportugolParser.AC, 0)

        def lista_comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniportugolParser.Lista_comandosContext)
            else:
                return self.getTypedRuleContext(miniportugolParser.Lista_comandosContext,i)


        def FC(self):
            return self.getToken(miniportugolParser.FC, 0)

        def cond_op(self):
            return self.getTypedRuleContext(miniportugolParser.Cond_opContext,0)


        def getRuleIndex(self):
            return miniportugolParser.RULE_comando_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_enquanto" ):
                listener.enterComando_enquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_enquanto" ):
                listener.exitComando_enquanto(self)




    def comando_enquanto(self):

        localctx = miniportugolParser.Comando_enquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comando_enquanto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(miniportugolParser.ENQUANTO)
            self.state = 113
            self.match(miniportugolParser.AP)
            self.state = 114
            self.match(miniportugolParser.ID)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0):
                self.state = 115
                self.cond_op()


            self.state = 118
            self.match(miniportugolParser.FP)
            self.state = 119
            self.match(miniportugolParser.AC)
            self.state = 120
            self.lista_comandos()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16824320) != 0):
                self.state = 121
                self.lista_comandos()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(miniportugolParser.FC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_definirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(miniportugolParser.ID)
            else:
                return self.getToken(miniportugolParser.ID, i)

        def IGUAL(self):
            return self.getToken(miniportugolParser.IGUAL, 0)

        def PV(self):
            return self.getToken(miniportugolParser.PV, 0)

        def expr_aritmeticas(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miniportugolParser.Expr_aritmeticasContext)
            else:
                return self.getTypedRuleContext(miniportugolParser.Expr_aritmeticasContext,i)


        def getRuleIndex(self):
            return miniportugolParser.RULE_comando_definir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_definir" ):
                listener.enterComando_definir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_definir" ):
                listener.exitComando_definir(self)




    def comando_definir(self):

        localctx = miniportugolParser.Comando_definirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comando_definir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(miniportugolParser.ID)
            self.state = 130
            self.match(miniportugolParser.IGUAL)
            self.state = 131
            self.match(miniportugolParser.ID)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                self.state = 132
                self.expr_aritmeticas()
                self.state = 133
                self.match(miniportugolParser.ID)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(miniportugolParser.PV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_condicionaisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniportugolParser.RULE_expr_condicionais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_condicionais" ):
                listener.enterExpr_condicionais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_condicionais" ):
                listener.exitExpr_condicionais(self)




    def expr_condicionais(self):

        localctx = miniportugolParser.Expr_condicionaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_condicionais)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_aritmeticasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniportugolParser.RULE_expr_aritmeticas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_aritmeticas" ):
                listener.enterExpr_aritmeticas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_aritmeticas" ):
                listener.exitExpr_aritmeticas(self)




    def expr_aritmeticas(self):

        localctx = miniportugolParser.Expr_aritmeticasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_aritmeticas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipos_variaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return miniportugolParser.RULE_tipos_variaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipos_variaveis" ):
                listener.enterTipos_variaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipos_variaveis" ):
                listener.exitTipos_variaveis(self)




    def tipos_variaveis(self):

        localctx = miniportugolParser.Tipos_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tipos_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_comandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando_escreva(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_escrevaContext,0)


        def comando_ler(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_lerContext,0)


        def comando_se(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_seContext,0)


        def comando_enquanto(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_enquantoContext,0)


        def comando_definir(self):
            return self.getTypedRuleContext(miniportugolParser.Comando_definirContext,0)


        def getRuleIndex(self):
            return miniportugolParser.RULE_lista_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_comandos" ):
                listener.enterLista_comandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_comandos" ):
                listener.exitLista_comandos(self)




    def lista_comandos(self):

        localctx = miniportugolParser.Lista_comandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lista_comandos)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.comando_escreva()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.comando_ler()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.comando_se()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.comando_enquanto()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.comando_definir()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





