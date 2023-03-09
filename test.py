s = "10-20"
 
result = ' '.join(format(c, 'b') for c in bytearray(s, "utf-8"))
print(result)