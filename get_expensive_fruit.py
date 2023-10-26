def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    x=data.split()
    return x[2]
f=open("fruits.csv").read()
print(get_expensive_fruit(f))



