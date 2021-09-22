#'^From .*@([^ ]*)'
import re
x = 'From stephenmarquard@uct.ac.za Sat Jan  5  09:14:16 2008 stephenmarquard@uct.ac.za'
y = re.findall('^From .*@([^ ]*)', x)
print(y)