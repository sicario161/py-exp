#non-greedy
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
#output: ['From:']