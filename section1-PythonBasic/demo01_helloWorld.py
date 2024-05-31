# '''
# File:demo01_helloWorld.py
# Time:2024/5/25 14:18
# IDE:PyCharm
# Author:Barranzi
# email:awc19930818@outlook.com
# github:https://github.com/La0bALanG
# Barranzi's Blog:aibarranzi.com.cn
# requirement:(Please describle your requirement here) -->
# '''
# # print(123,'hello world',sep='    GHHG    ')
# # print('hello world !','heihei world!',end=' ')
# # print('hahahahahhaah',end=' ')
#
#
#
# # ins = input('请输入你的姓名：')
# # print('我的名字是：',input('请输入你的姓名：'))
#
#
#
# # a = input('请输入一个数值：')
# # b = 2
# # c = 'b'
# # # print(id(b))
# # # # print(id(c))
# #
# # print(int(a) + b)
#
# class 逻辑回归类(object):
#
#     def 训练方法(self):
#         print('哈哈卧槽了')
#
# 逻辑回归类().训练方法()
#
#
#
#
#
# # run test UseCase if current modules is main
# if __name__ == '__main__':
#     pass






#
# num = int(input('请输入：'))
# print(num + 12)
# print(type(123))
# print(abs(-12.3))



# class DNNModels(object):
#     """
#     sadadasdasdasd
#     """
#
#     pass
#
# print(DNNModels.__doc__)
#
#











name = '楚兄'
state = '不高兴'
age = 18

# print('我叫{},我今年{}岁，我现在{}'.format(name,age,state));a = 2;print(a + 23)
# print('ajdklasjkdhakljdlkajkdljaksdj'
#       'kasjkldjaskldjklasjdkljaskdjlkasjdlkja'
#       'skldjklajdkljaskldjlaksjdklasjkldjlaksjdkla'
#       'sjdkljaskldjklasjdklasjkldjaskldjakl'
#       'sjdlkasjlkdj')
#
# s = 'shdlaskldjakldjklajdkl' \
#      'jakljdklasjdkljaskldjklasjdklja' \
#      'skldjklajkldjakldjlkshfkhdslkfghkjsdhfgljk' \
#       'khsdkjghskhjfdhgkjdsfhkjhghsdjhg'
# print(s)


'''
if 条件表达式1:
    做条件成立的事情
elif 条件表达式2:
    做条件成立的事情
...
else:
    做所有条件都不成立的事情

if条件表达式
result = 条件成立的事情 if 条件表达式 else 做条件不成立的事情

'''

'''

给定abc三个数字，输出其中的最大值
'''

# a = int(input('请输入第一个数值：'))
# b = int(input('请输入第二个数值：'))
# c = int(input('请输入第三个数值：'))
#
# print(f'当前a:{a},b:{b},c:{c}三个数值中的最大值是：{(a if a > c else c) if a > b else (b if b > c else c)}')


'''
while 循环条件表达式:

else:
    循环条件不成立时的事情

while循环的结束分为两种方式：
1.优雅的让循环自己个结束：设计一下循环条件表达式，让循环控制着某循环变量向着循环条件不满足的方向进行变化，直至某时刻循环条件不再成立，循环自动终止
2.暴力的强制结束循环：循环条件无需设计，只要给个True，保证循环能够开启就行；在循环执行到某些步骤时，如果希望终止，直接break即可
'''

# 输出1-100内所有的数值

# i = 0
# while True:
#     print(i)
#     i += 1
#


'''
for (int i = 0;i < arr.length;i++){
}

range(start,end,step)

'''

# # 1-100内的所有奇数
# for i in range(1,101):
#     for j in range(10):
#         for x in range(5):
#             for y in range(3):
#     if i % 2 == 1:
#         print(i)


# d = dict()


import requests
import json

d = {
    'name':'laoan',
    'address':[
        {'name':'wuhan'},
        {'name':'beijing'}
    ],
    'phone':{
        'num1':'13333333333',
        'num2':'12222222222'
    }
}
json_str = json.dumps(d)
print(type(json_str))
