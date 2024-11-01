money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
number_of_months = 0

while True:
    diff = spend - salary
    if diff > money_capital:
        break

    number_of_months += 1
    money_capital -= diff
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", number_of_months)
