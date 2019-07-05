import sys

# arg = sys.argv[0]
# print(arg)

li = [arg for arg in sys.argv]
print(li)

print(sys.path)
print(sys.platform)

def test(*args,**kwargs):
    print(args)
    print(kwargs)


test(1,2,3, x=1,y=2)