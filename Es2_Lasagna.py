EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(tempo_passato):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - tempo_passato 
def preparation_time_in_minutes(layers_number):
    """
    return the preparation time.
    it is calculated through the product between the costant PREPARATION_TIME and layers_number
    
    """
    return PREPARATION_TIME * layers_number
def elapsed_time_in_minutes(layers_number, elapsed_time):
    """
    Return elapsed cooking time.
 
    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return elapsed_time + preparation_time_in_minutes(layers_number)