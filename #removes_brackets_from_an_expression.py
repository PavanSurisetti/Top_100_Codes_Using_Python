#removes_brackets_from_an_expression
str=input('Enter an Expression:')
brackets=['(',')', '{','}','[',']']
print(f'Before removing spaces:{str}')
new_str=''
for i in str:
    if i in brackets:
       new_str+=''
    else:
        new_str+=i
print(f'After removing spaces:{new_str}')