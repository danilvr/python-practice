# Нарушения PEP 8

# 1. whitespace before '('.

def first ():
    pass


# 2. missing whitespace around operator.

var = 1+ 1

# 3. missing whitespace after ','.

a,b = 1,2

# 4. unexpected spaces around keyword / parameter equals.

def fourth(a = 0):
    return a

# 5. expected 2 blank lines, found 1.

n = 0

def fifth():
    pass


# 6. multiple statements on one line (colon).

if a > 5: a = 10

# 7. multiple statements on one line (semicolon).

a = 5; b = 10

# 8. comparison to None should be 'if cond is None:'.

a = a == None

# 9. comparison to True should be 'if cond is True:' or 'if cond:'.

a = a == True
