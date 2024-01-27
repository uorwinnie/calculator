#ask input-->calculate using eval()
#store thr results in storage
#ask for more input
#check what does the user want to do- clear/undo/power off(ctrl+d)
#clear--> rerun the program from the beginning
#undo --> check undo count(undo just once), does the result to undo exist(if no-> exit with message, if yes-> undo)
#ctrl+d--> check EOFError with try-except  -> thank you and exit
class Calculator:
    def __init__(self):
        try:
            self.storage = []
            self.undo_count = 0
            self.cal = input("Input: ")
            self.calculation()
        except EOFError:
            print()
            self.bye()
            exit("Power Off :|")

    @staticmethod
    def bye():
        print("Thank you for using our calculator ><")


    def calculation(self):
        while True:
            self.value = eval(self.cal)
            self.storage.append(self.value)
            self.new = input(f"Input: {self.value} ")
            if self.new.lower().strip() == "clear":
                self.clear()
            if self.new.lower().strip() == "undo" :
                self.undo()
            self.cal = f"{self.value}{self.new}"


    def clear(self):
            Calculator()


    def undo(self):
        try:
            if self.undo_count == 0:
                self.value = self.storage[-2]
                self.new = ""
                self.undo_count = 1
            else:
                print("You can't undo twice")
                self.new = ""
                self.undo_count = 0
        except IndexError:
            exit("There is no value to undo!!!!")


calculator = Calculator()
