import glob

strata = (glob.glob("/Applications/*.app"))
strata.sort()
l = []
for i in strata:
    print(i[14:-4])



