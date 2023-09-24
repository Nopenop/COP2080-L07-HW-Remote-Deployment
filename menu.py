import run_bash_cmd_function as r

class Menu:
    """Constructs a menu with no options set"""
    def __init__(self):
       """
       Menu class constructor function
       
       @param option the the option to add
       """
       self._options = []
    def addOption(self, option):
        """
        Adds option onto menu object
        """
        self._options.append(option)
        return option
    def getInput(self):
        """
        User input number value between 1 - 4.

        Loops through check for correct input from user.
        """
        num = 0
        while num == 0:
            print(*self._options, sep ='\n')
            num = int(input(' '))
            if num >= 1 and num <= 3:
                r.run_bash_cmd(num)
                num = 0
            elif num == 4:
                return num
            else:
                print("Please input a recognized value\n\n")
                num = 0
