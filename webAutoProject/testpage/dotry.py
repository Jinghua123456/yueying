#coding='utf-8'
#处理异常信息的练习(捕获异常由小范围到大范围）
def dotry():
    try:
        print("除法之前--------")
        i=1/0
        #i="123"
        print("除法之后-----")
    except ZeroDivisionError as z:
        print("除零异常错误，信息是:%s" % z)
    except ArithmeticError as a:
        print("算术计算异常错,误信息是:%s"%a)
    except Exception as e:
        print("基础异常,信息内容是:%s" %e)
    except:
        print("发生异常了！！")
    else:
        print("未发生异常————————")
    finally:
        print("除法之后—-----————")

if __name__=="__main__":
    print("调用方法之前————————")
    dotry()
    print("调用方法之后—-------")