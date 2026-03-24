yeses = ["yes","y","yeah","yup","yea"]

def parse_yn(prompt: str) -> bool:
    """
    Take as an input a string provided by the user
    and return a boolean value that says whether the string 
    is in the list of valid yeses
    """
    if prompt.lower() in yeses:
        return(True)
    else:
        return(False)
    
def validate(input_prompt: str, lower_bound: int, upper_bound: int):
    """
    Takes as an input a string for a user input prompt.
    Also takes as an input the lower and upper bound of the user's response.
    If the user's response is outside of that range, it continues to ask the user to submit 
    another input until the input is correct.
    Returns the user's response once correct.
    """

    answer = int(input(input_prompt))

    while not (lower_bound <= answer <= upper_bound):
        print(f"Your value must be between {lower_bound} and {upper_bound}. Try again.")
        answer = int(input(input_prompt))
    
    return(answer)