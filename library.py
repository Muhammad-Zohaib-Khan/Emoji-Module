from Language_Specifications import Operators,If_Else,For_loop,While_loop,Print,Input
class EmojiCode:
    def __init__(self):
        # Mapping of emojis to their respective classes
        self.emoji_mapping = {
            '🖨': Print,
            '✍': Input,
            '🤔😅': If_Else,
            '➰': For_loop,
            '➿': While_loop
        }
    def interpret(self, emoji, *args, **kwargs):
        command_class = self.emoji_mapping.get(emoji)

        if not command_class:
            raise ValueError(f"Emoji {emoji} is not a recognized command.")

        command_instance = command_class(*args, **kwargs)

        if hasattr(command_instance, "execute"):
            return command_instance
        else:
            return command_instance

Emoji=EmojiCode()

if __name__=="__main__":
    #FOR LOOP SYNTAX
    def print_(num):
        print("hello",num)
    Emoji.interpret("🔁",0,2).execute(print_)

    #IF ELSE SYNTAX
    def condition():
        return True
    def if_():
        return "Hello World"
    def else_():
        return "HIII"
    print(Emoji.interpret('🤔😅',condition,if_,else_).execute())

    #PRINT
    Emoji.interpret("🖨","everyone have to die one day").execute()

    #INPUT
    Emoji.interpret("✍","Enter Your Name : ").execute()

    #OPERATORS
    print(Emoji.interpret("⏸️",5,5).equal_to())
    print(Emoji.interpret("⏸️",5,5).less_than())
    print(Emoji.interpret("⏸️",5,5).grater_than())

    #While
    def while_condition():
        return False
    def while_print():
        print("Is it true that a human can do anything and everything unless someone or something stops one")
    Emoji.interpret("🔄",while_condition).execute(while_print)

