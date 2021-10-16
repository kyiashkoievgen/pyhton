profit = int(input("Какая у вас прибыль? "))
costs = int(input("Какие у вас издержки? "))
if profit > costs:
    profitability = profit / costs
    print("Вы работаете с прибылью", profitability)
    worker = int(input("Сколько сотрудников у вас работают?"))
    print("Каждый сотрудник заработал", (profit-costs)/worker)
else:
    print("Вы работаете в убыток.")