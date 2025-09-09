
prior_arrests=int(input('Prior arrests: '))
local_ordinance=str(input('Prior arrests for local ordinance (Y/N): '))
release_age=int(input('Age at release: '))

count=0
if prior_arrests>=2:
    count+=1
if prior_arrests>=5:
    count+=1
if local_ordinance=='Y':
    count+=1
if 18<release_age<24:
    count+=1
if release_age>=40:
    count-=1

print (f'The recidivism risk score is {count}')
