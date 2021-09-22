#[0-9]+
import re
x = 'My favorite 2 numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
#output: ['2', '19', '42']
