from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl,wlexpr

def EvalWolf(self,Expr):
    Expr = 'N[' + Expr + ']'
    session = WolframLanguageSession("/usr/bin/wolfram")
    CalResult = session.evaluate(wlexpr(Expr))
    session.terminate()
    return str(CalResult)
