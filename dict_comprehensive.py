keys = [1,'a',2,'b',3,'c']
print('list keys: ',keys)
values = [100,'apple',200,'berry',300,'cherry']
print('list values: ',values)

#### Dict by zip
bundle=dict(zip(keys,values))
print('the bundle is: ',bundle)

#### Dict by comprehention
box = {k:v for (k,v) in zip(keys,values)}
print('box is: ', box)


alpha = {k.upper()+', YES':v for (k,v) in zip(keys,values) if isinstance(k,str)}
print('alpha is: ',alpha)

alpha = {k:v*22 for (k,v) in zip(keys,values) if isinstance(k,int)}
print('alpha is: ',alpha)
