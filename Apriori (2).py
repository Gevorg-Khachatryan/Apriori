import xlrd
from _datetime import datetime

def Import_product():
    excel_list = xlrd.open_workbook('./Data.xlsx')
    sheet = excel_list.sheet_by_index(0)
    product_list = []
    for i in range(sheet.nrows):
        product_list.append(str(sheet.row(i)[0]).replace('text:', '').replace("'", ''))
    return product_list
def Import_Buy_list():
    excel_list = xlrd.open_workbook('./Data.xlsx')
    sheet = excel_list.sheet_by_index(0)
    buy_list1=[]
    buy_list2=[]

    for i in range(sheet.nrows):
        buy_list1.append(str(sheet.row(i)[1]).replace('text:', '').replace("'", '').replace(",", ''))
    for i in buy_list1:
        x=[]
        for j in i:
            k=int(j)
            x.append(k)
        buy_list2+=[x]
    return buy_list2

lst=[]

for i in range(len(Import_product())):
    t=[i+1]
    lst+=[t]

def List(ls):
    lt=[]
    for i in lst:
        for j in ls:

            if i[0] not in j:
                li=i+j
                lt+=[li]

    return lt


def Print():
    xl = List(lst)
    n = int(input('Enter the number of products:'))
    minimum=int(input('Enter the minimum coincide number:'))
    start = datetime.now()
    for i in range(n - 2):
        xl = List(xl)
    for sublist in xl:
        for i in range(len(sublist)):
            sublist[i] = int(sublist[i])
        x = 0
        for i in Import_Buy_list():

            if sublist == list(set(i).intersection(set(sublist))):
                x += 1
        if x >= minimum:
            for j in range(len(sublist)):
                sublist[j] = Import_product()[sublist[j]]
            print(sublist, ': number of concidence', x)
    print(datetime.now()-start,'seconds')

while True:

    Print()
