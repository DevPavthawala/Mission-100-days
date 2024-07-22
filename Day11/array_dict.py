Type = input("Enter a type(array,dict) : ")

if Type == "array":
    stock_prices = []

    with open("stock_prices.csv") as f:
        for line in f:
            tokens = line.split(",")
            day = tokens[0]
            price = float(tokens[1])
            stock_prices.append([day, price])

    print(stock_prices)

    # for getting price on particular day at order of n complexity
    data = input("enter a date : ")

    for element in stock_prices:
        if element[0] == data:
            print(element[1])




# by converting this array to dictionary the complexity reduce to order of 1

if Type == "dict":
    stock_prices = {}

    with open("stock_prices.csv") as f:
        for line in f:
            tokens = line.split(",")
            day = tokens[0]
            price = float(tokens[1])
            stock_prices[day] = price

    print(stock_prices)

    data = input("enter a date : ")
    print(stock_prices[data])  # no need of loops

