# 7. Write a Python program to find the first appearance of the substring 'not' and
#  'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#  substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


def string_modify(str):
  string_not = str.find('not')
  string_poor = str.find('poor')
  

  if string_poor > string_not and string_not>0 and string_poor>0:
    str = str.replace(str[string_not:(string_poor+4)], 'good')
    return str
  else:
    return str


print(string_modify('The lyrics is not that poor!'))
print(string_modify('The lyrics is poor!'))