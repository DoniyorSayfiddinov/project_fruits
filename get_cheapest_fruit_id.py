def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    x=data.split()
    return x[0]
f=open("fruits.csv").read()
print(get_cheapest_fruit_id(f))


