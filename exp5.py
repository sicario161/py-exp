#'@([^ ]*)'
import re
x = 'From stephenmarquard@uct.ac.za Sat Jan  5  09:14:16 2008'
y = re.findall('@([^ ]*)', x)     #equivalent code: re.findall('@(\S*)', x)
print(y)
#output: ['uct.ac.za']