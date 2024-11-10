# Курсор

В задании доступны следующие таблицы:

`orders`

- `order_id` - id заказа
- `customer_id` - id покупателя
- `order_date` - дата заказа
- `total_amount` - сумма заказа

`customers`

- `customer_id` - id покупателя
- `customer_name` - имя покупателя

## src/solution.py

Допишите функцию `get_order_sum()`, которая принимает соединение и месяц, и возвращает общую сумму заказов каждого покупателя за этот месяц. Функция должна вернуть результат в виде строки:

```
Покупатель Emily White совершил покупок на сумму 290
Покупатель John Smith совершил покупок на сумму 130
```
```python
conn = psycopg2.connect('..')

month = 2
get_order_sum(conn, month)
# Покупатель Emily White совершил покупок на сумму 290
```