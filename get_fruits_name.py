def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
     x=data.split()
     l=[]
     l.append()
    return x[3]
f=open("fruits.csv").read()
print(get_frutis_name(f))


    