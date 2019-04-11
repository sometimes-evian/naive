# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:27:43 2019

@author: lee
"""

import numpy as np
import random
import math
male=1
female=2
def get_children(n,male_portion,fertility):   
    r=[]
    for i in range(n):
        r.append(random.random())
    children=[]
    for i in range(n):
        children.append(0)
    for i in range(n):
        if(r[i]<male_portion):
            children[i]=male
        else:
            children[i]=female
    return children

def advance_generation(parents,policy='one child',male_portion=0.5,fertility=1.0):
    males=0
    females=0
    for i in range(len(parents)):
        if(parents[i]==male):
            males+=1
        else:
            females+=1
    couples=min(males,females)
    if(policy=='one child'):
        children=get_children(couples,male_portion,fertility)
    elif(policy=='one son'):
        children=get_children(couples,male_portion,fertility)
        daughters=0
        for i in range(len(children)):
            if(children[i]==female):
                daughters+=1
        while(daughters>0):
            daughters=0
            new_children=get_children(daughters,male_portion,fertility)
            children=np.concatenate((children,new_children))
            for i in range(len(new_children)):
                if(new_children[i]==female):
                    daughters+=1
    return children

N=1000000
male_portion=0.51
fertility=0.92
parents=get_children(N,male_portion=0.5,fertility=1.0)
print('one son policy, start: %d'%(len(parents)))
for i in range(10):
    l=len(parents)
    right=int(l*0.94)
    parents=advance_generation(parents[:right],'one son',male_portion,fertility)
    p=[]
    for j in range(6):
        pp=get_children(l-right,male_portion,fertility)
        p=np.concatenate((p,pp))
    parents=np.concatenate((parents,p))
    ll=len(parents)
    rr=ll/l
    print('r = %g'%(rr))
    print('%3d: %d'%(i+1,len(parents)))