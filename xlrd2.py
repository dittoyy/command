# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import unittest

class Ts1(unittest.TestCase):
	def open_excel(self,file= 'file.xlsx'):
		try:
			data = xlrd.open_workbook(file)
			return data
		except Exception,e:
			print str(e)
	#根据索引获取Excel表格中的数据   参数:file：Excel文件路径	 colnameindex：表头列名所在行的所以  ，by_index：表的索引
	def test_excel_table_byindex(self,file= 'file.xlsx',colnameindex=0,by_index=0):
		data = xlrd.open_workbook(file)
		table = data.sheets()[by_index]
		nrows = table.nrows #行数
		ncols = table.ncols #列数
		colnames =  table.row_values(colnameindex) #某一行数据 
		list =[]
		for rownum in range(1,nrows):
			row = table.row_values(rownum)
			if row:
				app = {}
				for i in range(len(colnames)):
				    app[colnames[i]] = row[i]
		list.append(app)
        print list


	#根据名称获取Excel表格中的数据   参数:file：Excel文件路径	 colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
	# def test_excel_table_byname(self,file= 'file.xlsx',colnameindex=0,by_name=u'Sheet1'):
	# 	data = xlrd.open_workbook(file)
	# 	table = data.sheet_by_name(by_name)
	# 	nrows = table.nrows #行数 
	# 	colnames =  table.row_values(colnameindex) #某一行数据 
	# 	list =[]
	# 	for rownum in range(1,nrows):
	# 		row = table.row_values(rownum)
	# 		if row:#row大于0
	# 			app = {}
	# 			for i in range(len(colnames)):
	# 				app[colnames[i]] = row[i]
 #                print app
	# 	list.append(app)
	# 	return list
 #        print list

def main():
    tables = excel_table_byindex()
    for row in tables:
        print row

   # tables = excel_table_byname()
   # for row in tables:
	  #   print row

if __name__=="__main__":
	unittest.main()