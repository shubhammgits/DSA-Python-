def intTostr(i):
    if i==0:
        return '0'
    digits = '0123456789'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i//10
    return result