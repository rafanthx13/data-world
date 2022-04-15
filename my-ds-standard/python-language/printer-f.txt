# Formato de print `f'`

## Links


## Python f-strings Are More Powerful Than You Might Think

https://towardsdatascience.com/python-f-strings-are-more-powerful-than-you-might-think-8271d3efbd7d

**Imprimir data é masi fácil com `f`**

````
import datetime
today = datetime.datetime.today()
print(f"{today:%Y-%m-%d}")
# 2022-03-11
print(f"{today:%Y}")
# 2022
````

Variable Names and Debugging
One of the more recent additions to f-string features (starting with Python 3.8) is ability to print variable names along with the value:


x = 10
y = 25
print(f"x = {x}, y = {y}")
# x = 10, y = 25
print(f"{x = }, {y = }")  # Better! (3.8+) !!!!!!!!!!!!
# x = 10, y = 25

print(f"{x = :.3f}")
# x = 10.000c !!!!!!!!!!!!!


Formataçâo

text = "hello world"

# Center text:
print(f"{text:^15}")
# '  hello world  '

number = 1234567890
# Set separator
print(f"{number:,}")
# 1,234,567,890

number = 123
# Add leading zeros
print(f"{number:08}")
# 00000123

Nested F-Strings
If basic f-strings aren’t good enough for your formatting needs you can even nest them into each other:

number = 254.3463
print(f"{f'${number:.3f}':>10s}")
# '  $254.346'


Conditionals Formatting
Building on top of the above example with nested f-strings, we can go a bit farther and use ternary conditional operators inside the inner f-string:


import decimal
value = decimal.Decimal("42.12345")
print(f'Result: {value:{"4.3" if value < 100 else "8.3"}}')
# Result: 42.1
value = decimal.Decimal("142.12345")
print(f'Result: {value:{"4.2" if value < 100 else "8.3"}}')
# Result:      142


