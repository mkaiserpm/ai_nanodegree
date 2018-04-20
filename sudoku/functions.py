from utils import *

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    checkNums = '987654321'
    for box,units_ in units.items():
        numcount = 0
        for num in checkNums:
            for pbox in units_:
                if num in values[pbox]:
                    numcount+=1
            if numcount == 1:
                values[box] = num
                
    return values
