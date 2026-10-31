monthly_sale = 0


def calculate_percentage_sales():
    month1_sales = 130000
    month2_sales = 100000
    percentage_sales = ((month1_sales - month2_sales) / month2_sales) * 100
    return percentage_sales


percentage_sales = calculate_percentage_sales()
print(f"Percentage sales: {percentage_sales}%")
if percentage_sales >= 15:
    print(f"True: {True}")
calculate_percentage_sales()



