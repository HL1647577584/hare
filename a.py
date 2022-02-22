def peach_heart(a,b):
    print('\n'.join([''.join([(a[(x-y)%len(a)] \
    if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**b*(y*0.1)**3\
    <= 0 else' ')for x in range(-30,30)])\
            for y in range(30,-12,-1)]))

peach_heart("hecai",2)