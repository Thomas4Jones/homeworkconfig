"""СИНТАКСИС\ПРАВИЛА PYTHON"""

# переменные
x = 104314
y = 53255
a = True
b = False
c = [1, 2, 3, 4, 5, 10]
d = [x, y]
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# арифметические операторы
add = x + y # сложение
sub = x - y # вычетание
multi = x * y # умножение
divis = x / y # деление
modus = x % y # остаток от деления
exponent = x ** y # возведение в степень

# операторы сравнения
less = x < y # меньше
great = x > y # больше
eque = x == y # равно
not_eque = x != y # не равно
less_or_eque = x <= y # меньше или равно
great_or_eque = x >= y # больше или равно

# логические операторы
logi_and = a and b # И
logi_or = a or b # ИЛИ
logi_not = not a # НЕ

# операторы принадлежности
member = x in d # ЭТО В
thismember = 2 in c
same = x is y # ЭТО ТО

# прочее
union = set1 | set2
divis_result = round(divis, 2) # округление до знака после запятой
divis_result_2 = "{:.2f}".format(divis) # округление до знака после запятой

local_var = locals() # создание словаря локальных переменных
local_var_copy = local_var.copy() # сделали копию словаря

for var_name, var_value in local_var_copy.items():
    print(f"var_name: {var_value}") # фильтр вывода значений словаря

print()