import sys
from art import logo

print(logo)


class Calculator:

    def __init__(self):
        self.operation = ""
        self.operation1 = ""
        self.operation2 = ""
        self.result = 0
        self.operations = {"+":self.add, "-":self.subtract, "*":self.multiply, "/":self.divide}        

    def add(self,num1,num2):
        return num1+num2

    def subtract(self,num1,num2):
        return num1-num2

    def multiply(self,num1,num2):
        return num1*num2
                
    def divide(self,num1,num2):
        return num1/num2

    def check_if_input_is_a_number(self,num):
        is_int = False
        while not is_int:
            try:
                num = int(input("Enter a number: "))
                is_int = True
            except ValueError:
                print("You have not entered a valid Integer. Please try again!")
        return num

    def get_inputs(self,operation,operation1,operation2):    
        self.operation1 = self.check_if_input_is_a_number(self.operation1)
        while self.operation not in self.operations.keys():
            self.operation = input("Enter the operation you want to perform -> (+, -, *, /): ")
        self.operation2 = self.check_if_input_is_a_number(self.operation2)          

    def calculate(self):
        self.get_inputs(self.operation,self.operation1,self.operation2)
        self.result = self.operations[self.operation](self.operation1, self.operation2)

    def main(self):
        self.calculate()
        print(f"The result is {self.result}")

#run the function
if __name__ == "__main__":
    calculator = Calculator()
    calculator.main() 


