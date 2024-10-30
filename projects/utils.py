# Utility functions


def valid_name(name):
    """
    Checks the string input to ensure that it is non-numeric.

    Parameters:
    name (str): The name of the user

    Returns:
    name (str): The name of the user

    Raises:
    TypeError: If the name is numeric
    """

    if name.replace(" ", "").isalpha() == False:
        raise TypeError('Name must be non-numeric')
    return name
    
