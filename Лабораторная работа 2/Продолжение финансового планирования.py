salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_sum = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months):
    total_sum = total_sum + (salary - spend)
    spend = spend * increase + spend

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(abs(total_sum)))
