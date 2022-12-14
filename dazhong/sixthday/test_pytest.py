# -*- encoding：utf-8 -*-
# import pytest
# def setup_module(self):#全局模块级别（一个py文件）在开头——写在类外
#     print("全局模快")
# def teardown_module(self):#全局模块级别（一个py文件）在结尾——写在类外
#     print("全局模快1")
# class Test_class():
#     @classmethod
#     def setup_method(cls):#方法级别，类中的每个方法前后各执行一次。（前）
#         print("方法级别")
#     @classmethod
#     def teardown_method(cls):#方法级别，类中的每个方法前后各执行一次（后）
#         print("方法级别1")
#     def setup_class(self):#类级别，在每个类的前后各执行一次（前）
#         print("前类级别")
#     def teardown_class(self):#类级别，在每个类的前后各执行一次（后）
#         print("后类级别")
#     def setup(self):先setup在测试用例在teardown
#         print("初始化")
#     def teardown(self):
#         print("结束清理")
#     def test_young(self):#测试用例
#         print("这是：test_young")
#     def test_name(self):
#         print("这是：test_name")
# if __name__ == '__main__':
#     pytest.main()
#pytest参数化
#单参数：@pytest.mark.parametrize装饰器
#       第一个参数要与用例单参数一致
    #   第二个参数，传的是一个列表，每个值代表一个数据
    #   第三个参数，选传参数，穿的是用例的标题，列表表示，前面几个数据，后面几个标题
# import pytest
# age_liat=["23","24","aaa"]
# @pytest.mark.parametrize("age",["23","21","yy"],ids=['年龄23','年龄21','年龄yy'])
# def test_age(age):
#     assert age in age_liat

#多参数 @pytest.mark.parametrize装饰器
#       第一个参数要与用例单参数一致
#       第二个参数传入列表，每个值需要用可迭代的对象(元组)进行包裹，元组内的数据量与参数相同，代表数据。
#
# import pytest
# @pytest.mark.parametrize("first,second,expvalue",[(1,1,2),(2,3,5)])
# def test_one(first,second,expvalue):
#     assert first+second==expvalue#段言

#笛卡尔积
# import pytest
# @pytest.mark.parametrize("x",[1,2,3])
# @pytest.mark.parametrize("y",["第一组","第二组"])
# def test_two(x,y):
#     print("{}第{}个数".format(y,x))
#用例标记
#场景：只去执行一部分特定的用例
#使用方法：@pytest.mark.标签名
#执行方法：pytest tset_demo.py-m标签名
# import pytest
# @pytest.mark.login
# def test_login_001():
#     print("用户名密码登录成功")
# @pytest.mark.login
# def test_login_002():
#     print("用户名密码登录失败")
# @pytest.mark.login
# def test_login_003():
#     print("手机号一键登录")
# @pytest.mark.reg
# def test_reg_001():
#     print("用户名已存在")
# @pytest.mark.reg
# def test_reg_002():
#     print("注册成功")
# @pytest.mark.reg
# def test_reg_003():
#     print("密码不合规")




