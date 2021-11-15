def param_count(*args,**kwargs):
    return len(args) + len(kwargs)

print(param_count(2,3,4))
print(param_count())
print(param_count(2141,41241,1,41,41,41))
