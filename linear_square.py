##implement linear square in Python

observation=[]

linear_model=[]

a,b,lse,ls_error=0
for x in observation:
    idx=observation.index(x)
    a+=x*linear_model[idx]
    b+=pow(linear_model[idx],2)

lse=a/b ##compute linear square estimator

for i in range(len(observation)):
    ls_error+=pow(observation[i]-lse*linear_model[i],2) ##compute linear square error




