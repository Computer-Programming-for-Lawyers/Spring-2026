print("You just ran the lec6_library file")

def times_two(number_parameter: int) -> tuple:
    """
    Takes as a parameter a number and returns that number and itself times two.
    """
    return(number_parameter, number_parameter*2)

def greet(name, greeting="Hello"): #greeting will always be hello unless another value provided
    print(greeting, name)

def message(year,date):
    s = f"The year is {year}. The date is {date}."
    print(s)

# define a function -- hello_world -- with no arguments, print "Hello, World!"

def hello_world():
    print("Hello world!")
    
def hello_world_multiple(number_of_times):
    """
    print hello world the amount of times the user says
    """
    for i in range(number_of_times):
        hello_world() # call original function