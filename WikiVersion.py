# Signature Python Quine
x = 'x = %r\nprint (x%%x)'
print (x%x)
