import rs
coder = rs.RSCoder(20,13)
c = coder.encode("Hello, world!")
print (repr(c))
r = "\0"*3 + c[3:]
print (repr(r))
coder.decode(r)