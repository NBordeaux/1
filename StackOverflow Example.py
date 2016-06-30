# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:49:18 2016

@author: Nick
"""
import pandas as pd
import xlsxwriter as xw

# random dataframe
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([5., 6., 7., 8.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)


# write data to file
writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter')
df.to_excel(writer,"sheet with table and header")

# get sheets to add the tables
workbook  = writer.book
worksheet_table_header = writer.sheets['sheet with table and header']

# the range in which the table is
end_row = len(df.index)
end_column = len(df.columns)
cell_range = xw.utility.xl_range(0, 0, end_row, end_column)

######################################
# The hack

# Using the index in the Table
df.reset_index(inplace=True)
header = [{'header': di} for di in df.columns.tolist()]
worksheet_table_header.add_table(cell_range,{'header_row': True,'first_column': True,'columns':header})

writer.save()