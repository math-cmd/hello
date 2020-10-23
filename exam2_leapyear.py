# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

t=int(input('请输入年份：'))
if t%4==0 and t%100!=0 or t%400==0:
    print(str(t)+'年是闰年')
else:
    print(t,'年不是闰年')