from library import Emoji

#Program to Find Root Using Bisection Method

def f(x):
    return x**2-2
xL=int(Emoji.interpret("✍","Enter Lower Bound : ").execute())
xU=int(Emoji.interpret("✍","Enter Upper Bound : ").execute())

def bisection(xL,xU):
    def condition():
        return (f(xL)*f(xU))>0
    def if_block():
        return "NO Root Found Because it is a bracking method root always lies between initial bounds"
    def else_block():
        xm=(xL+xU)/2
        def while_condition():
            return abs(xL-xU)<0.001
        def while_print():
            xm=(xL+xU)/2
            def condition():
                return f(xm)==0
            def if_():
                return
            def else_():
                pass
            Emoji.interpret('🤔😅',condition,if_,else_).execute()

            def condition():
                return f(xm)*f(xL)<0
            def if_2():
                xU=xm
            def else_2():
                xL=xm
            Emoji.interpret('🤔😅',condition,if_2,else_2).execute()


            
        Emoji.interpret("➿",while_condition).execute(while_print)

        Emoji.interpret("🖨","The Final Root is: ",xm).execute()

        
    Emoji.interpret('🤔😅',condition,if_block,else_block).execute()
bisection(xL,xU)
