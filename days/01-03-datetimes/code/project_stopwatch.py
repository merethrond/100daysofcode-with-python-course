from datetime import datetime

"""
This program shows the working of a stopwatch.
Press SpaceBar to Start or Stop.
Press 'S' to show the current elapsed time between start and stop.
"""
def register_time():
    """
    This is custom start functiom
    :return:
    """
    present_time = datetime.today()
    return present_time


def displaywatch():
    """
    Using the function above to display the options present
    to operate the stopwatch using SpaceBar.
    :return: None
    """
    start_char = input("Press Spacebar to start the stopwatch:")
    while not start_char == " ":
        start_char = input("Wrong input, Press Spacebar to start the stopwatch:")
    start_time = register_time()
    print("The time you started: ", str(start_time.time()))
    end_char = input("Press Spacebar to stop the stopwatch or 'S' to show the time elapsed ")
    while not end_char == " ":
        if end_char == 'S' or end_char == 's':
            end_time = register_time()
            print("The time elapsed: ", str(end_time - start_time))
            end_char = input("Press Spacebar to stop the stopwatch or 'S' to show the time elapsed ")
        else:
            end_char = input("Wrong input, Press Spacebar to stop the stopwatch:")
    end_time = register_time()
    print("The time you ended: ", str(end_time.time()))
    print("The time elapsed: ", str(end_time - start_time))

displaywatch()