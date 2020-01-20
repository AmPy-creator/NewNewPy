print("Python", sep='')
print("P","Y","T","H","o","N", sep='')
print('010','324','0089',sep='-')
print('pdh411', end='@google.com\n')
print('Authorized By ', end='Bump DooHee Park\n')

import sys

print('Learning Python', file=sys.stdout)
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', 'two'))
print('{1}{0}'.format(2,1))
#%s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print('%10s' %('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('%10s' % ('nice'))
print('{:-^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('PythonStudy'))
print('%5s' % ('PythonStudy'))

print('%-.5s' % ('PythonStudy'))
print('{:10.5}' .format('PythonStudy'))
#%d
print('%d %d' %(1,2))
print('{} {}'.format(2,3))

print('%5d' %(292))
print('{:^4d}'.format(42))


#%f
print('%1.3f' %(3.1415925))
print('{:1.3f}'.format(3.1415925))

print('%06.2f' %(3.141627182764))
print('{:06.2f}'.format(3.141627182764))


print('%d' %(32))
print('%-.1s' %(32))
print('{:<5}'.format('32'))
print('{:1.5f}'.format(383.1223))
print('{:3.2}'.format('study'))
print('%-3.2s' %('study'))
