gold = 96 / 16
silv = 96
total = int(input('total: '))
silv_price = 48
gold_price = (total - 96 * 48) // (gold)
print(gold_price)