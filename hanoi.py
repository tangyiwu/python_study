#汉诺塔的移动可以用递归函数非常简单地实现
#编写move(n,a,b,c)函数，它接受参数n，
#表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出所有盘子从A借助B移动到C的方法

def move(n,a,b,c):
    if n==1:
        print(a,' --> ',c)
    else:
        move(n-1,a,c,b)
        print(a,' --> ',c)
        move(n-1,b,a,c)
