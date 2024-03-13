class Operators(object):
    def __init__(self,value_1,value_2):
        self.value_1=value_1
        self.value_2=value_2
    def equal_to(self):
        return self.value_1==self.value_2
    def less_than(self):
        return self.value_1<self.value_2
    def grater_than(self):
        return self.value_1>self.value_2

class If_Else(object):
    def __init__(self, condition, true_block, false_block):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def execute(self):
        if (self.condition()):
            return self.true_block()
        else:
            return self.false_block()
class For_loop(object):
    def __init__(self,start,end,step=1):
        self.start=start
        self.end=end
        self.step=step

    def execute(self,callback):
        for i in range(self.start,self.end,self.step):
            callback(i)
    
class While_loop(object):
    def __init__(self,condition):
        self.condition=condition

    def execute(self,callback):
        while (self.condition()):
            callback()

class Print(object):
    def __init__(self, *args, sep=" ", end="\n"):
        self.args = args
        self.sep = sep
        self.end = end

    def execute(self):
        output = self.sep.join(map(str, self.args)) + self.end
        print(output, end="")


class Input(object):
    def __init__(self, prompt=''):
        self.prompt = prompt

    def execute(self):
        return input(self.prompt)



##################################################################
#a=Operators(2,2)
#print(a.equal_to())
#print(a.less_than())
#print(a.grater_than())
##################################################################
#def condition():
#    return True
#def if_():
#    return "Hello World"
#def else_():
#    return "HIII"
    
#a=If_Else(condition,if_,else_)        
#print(a.execute())
#################################################################
#a=For_loop(0,2)
#def print_(num):
#    print(num)
#a.execute(print_)
################################################################
#def check(*args):
#    return False
#def print_():
#    print("name")
#a=While_loop(check)
#a.execute(print_)

