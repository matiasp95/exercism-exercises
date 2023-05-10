def total(basket):
    multiplier = [0, 800, 1520, 2160, 2560, 3000]
    books = [basket.count(x) for x in set(basket)]
    prices = []
    if len(books) == 1: return books[0] * 800
    while len(books) > 1:
        amount, total = 0, 0
        books.sort()
        for index in range(len(books)):
            total += (books[index] - amount) * multiplier[len(books) - index]
            if books[index] > amount: amount = books[index]
        
        prices.append(total)
        
        books[0]-=1
        books[1]+=1
        if 0 in books: books.remove(0)
    return min(prices) if len(prices) > 0 else 0

total([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5])