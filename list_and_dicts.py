def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Jose", "lastname": "MEdina"}

    super_list =[
        {"firstname": "miguel", "lastname": "torres"},
        {"firstname": "pepe", "lastname": "rodelo"},
        {"firstname": "susana", "lastname": "martinez"}

    ]
    super_dict = { 
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]

    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()