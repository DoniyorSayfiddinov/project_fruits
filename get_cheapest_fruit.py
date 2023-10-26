def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    x=data.split()
    return x[1]
f=open("fruits.csv").read()
print(get_cheapest_fruit(f))




    