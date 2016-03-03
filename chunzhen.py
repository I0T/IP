#!/usr/bin/env python3
#-*-coding:utf-8-*-
__author__ = 'IOT'
import os
f=open('ip.txt')
f_1=open('result1.txt','a+')
for i in f:
    i=i.strip('\n').split('.')
    I0T='%s.%s.%s.1-%s.%s.%s.254'%(i[0],i[1],i[2],i[0],i[1],i[2])
    f_1.writelines(I0T+'\n')
I0T_1=set([I1 for I1 in open('result1.txt')])
I0T=open('result.txt','a+')
for I0T_1 in I0T_1:
    I0T_2=str(I0T_1).strip('\n')
    I0T.writelines(I0T_2+'\n')
os.remove('result1.txt')
