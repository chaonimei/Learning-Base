## 给定内容：两个正整数 a 和 b（a<b<10000）。
## 要求：返回从 a 到 b（包括 a 和 b）所有奇数整数的和。

# 定义a,b

a = int(3)
b = int(5)

# whiile循环

if a%2==0 :
    i = a+1
else :
    i = a
while i <= b :
        i += 2 + i
else :
        print(i)


