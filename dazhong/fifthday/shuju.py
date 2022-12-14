# class excel():
#     #读取Excel数据（xlrd）
#     def readExcelData(self,sheetname,x,y):
#         import xlrd#导入xlrd
#         #路径赋值给excelPath
#         excelPath='../fifthday/yonghu.xls'
#         #打开文件赋值给openfile
#         openfile=xlrd.open_workbook(excelPath)
#         #定位sheet页，通过sheet页名称
#         sheetpage=openfile.sheet_by_name(sheetname)
#         #返回
#         return sheetpage.cell_value(x,y)
#     def readExcelData1(self,sheetname):
#         import xlrd#导入xlrd
#         # 路径赋值给excelPath
#         excelPath='../fifthday/yonghu.xls'
#         # 打开文件赋值给openfile
#         openfile=xlrd.open_workbook(excelPath)
#         # 定位sheet页，通过sheet页名称
#         sheetpage = openfile.sheet_by_name(sheetname)
#         #打印所有行
#         print(sheetpage.nrows)
#         #定义空列表
#         user=[]
#         for i in range(1,sheetpage.nrows):
#          user.append(sheetpage.cell_value(i,0))
#          return user
# # print(excel().readExcelData("user",1,1))
# # print(excel().readExcelData1("user"))
# #写入excel数据（openpyxl）
#     def writeExceldata2(self,write_data):
#         import openpyxl#导入openpyxl
#         #文件路径赋值给excelPath1
#         excelPath1 = '../fifthday/yonghu.xlsx'
#         #加载excelPath1文件（制作替身==可以理解为打开文件），赋值给w
#         w=openpyxl.load_workbook(excelPath1)
#         #基于打开的文件，使用sheet页名称定位sheet页
#         sheetpage1=w["user"]
#         # 打印当前Excel数据总行数
#         print(sheetpage1.max_row)
#         #要写入数据的当前行数（写入数据的当前行数=当前Excel数据总行数+1），赋值给write_row
#         write_row=sheetpage1+1
#         #基于定位的sheet页，往单元格（cell）写入数据，数据是活的使用变量write_data
#         sheetpage1.cell(write_row,1,write_data)
#         #保存Excel
#         w.save(excelPath1)
#调用写入Excel方法，并传入写入的数据
# print(excel.writeExceldata2("张悦"))

# """
# 一、解析xml（xml树结构的标签语言，xml自身提供数据解析库dom）
# 1定位文件
# 2打开文件
# 3解析文件
# 4返回数据
# 二、解析yaml，（文本语言，三方数据库yaml进行解析）
# 1定位文件
# 2打开文件
# 3返回数据
# """


# class data_parsing():
#     # def analysis_xml(self,firstTag,onesex):
#            #导入minidom（解析库）
#     #     from xml.dom import minidom
#            #定位文件
#     #     xmlfile='../fifthday/xmldata.xml'
#            #打开文件
#     #     openfile=minidom.parse(xmlfile)
#            #定位一级标签
#     #     OneNode=openfile.documentElement.getElementsByTagName("onename")[0]
#            #定为二级标签
#     #     twonode=openfile.documentElement.getElementsByTagName("onesex")[0]
#            #获取元素的第一个子元素节点值并返回
#     #     return twonode.childNodes[0].nodeValue
#     def analysis_yaml(self):
#         import yaml#导入yaml
#         #定位文件
#         yamlfile='../fifthday/yamlData.yml'
#         #打开文件
#         c=open(yamlfile)
#         #返回
#         return yaml.safe_load(c)
# analysis=data_parsing()
# # print(analysis.analysis_xml("onename","onesex"))
# print(analysis.analysis_yaml())





