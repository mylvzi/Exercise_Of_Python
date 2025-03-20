'''
2025-3-17
py 基础语法回顾
'''
from typing import List


# 使用缩进表示代码块
# if True:
#     print("1")
# else:
#     print("2")

# 字符串的访问
# str = '123456'
# print(len(str))
# # 使用字符串切片
# print(str[1 : -1])
# print(str[-1:])
# print(str[::2])

# 输入语句 input 返回类型为string
# name = input("请输入名子：")
# print(name)
#
# height = (float)(input("身高"))
# print(height)

# try:
#     height = (int)(input("l"))
#     print(height)
# except ValueError:
#     print("请输入数字")


# 写一个简单的函数
# def isStrOrDigit(var):
#     if isinstance(var,str):
#         if(var.isdigit()):
#             print(f"{var} is a digit")
#         else:
#             print(f"{var} is a letter")
#     else:
#         print(f"{var} is not a string")
#
# # test
# isStrOrDigit("123")
#
# # 列表
# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# print(type(list1))
# print(len(list1))
# print(list1[-1::-1])


# # reverse words
# def reverwords(str):
#     list1 = str.split()
#     ret = ' '.join(list1[::-1]) # 重新将列表中的元素组织为字符串
#     return ret
# if __name__ == '__main__':
#     print(reverwords('hello world'))


# 写一个类和类方法
class Solution:
    def twoSUM(self, nums : List[int], k : int) -> List[int]:
        # 使用enumerate语法  可以同时打印下标和数组元素  在py中使用[]来表示列表 List
        n = len(nums)
        for i, val in enumerate(nums):
            print(i, val)

if __name__ == '__main__':
    s = Solution()
    s.twoSUM([1,2,3,4,5,6,7,8,9,10], 3)












