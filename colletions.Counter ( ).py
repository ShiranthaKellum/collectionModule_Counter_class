from collections import Counter

def findShoe (shoeCount, sizeAndAmount):
    if sizeAndAmount [0] in shoeCount.keys () and shoeCount [sizeAndAmount [0]] > 0:
        return True

if __name__ == '__main__':
    income = 0
    noOfshoes = int (input ())
    allShoesInSizes = list (map (int, (input ().split ())))
    noOfcustomers = int (input ())
    # print (Counter (allShoesInSizes))
    # print (Counter (allShoesInSizes).items ())
    shoeCount = Counter (allShoesInSizes)
    # print (shoeCount)
    for i in range (noOfcustomers):
        sizeAndAmount = list (map (int, input ().split ()))
        if findShoe (shoeCount, sizeAndAmount):
            shoeCount.update ({sizeAndAmount [0] : -1})
            income += sizeAndAmount [1]

    print (income)
        