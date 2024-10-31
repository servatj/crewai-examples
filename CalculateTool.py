from langchain_community.tools import tool

@tool("Calculate")
def calculate(equation):
    """ Useful to solve equtions and math problems. """
 	
    print("Equation: ", equation)
    
    return eval(equation)
