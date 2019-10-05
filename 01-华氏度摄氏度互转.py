#coding=utf-8
def fc():
   while True:
      fc = input("请输入华氏度OR摄氏度，如：37.2C或者5.6F.输入'Q'或'q'退出\n")#获取用户输入的华氏度和摄氏度
      if fc.endswith('C') == True:  # 判断输入的是否为摄氏度
         c = float(fc.split('C')[0])  # 将输入的摄氏度使用split以C分割，将其分割成列表并取第一个值转换成浮点型。等同于 a=fc.split('C')   c=float(a[0])
         print(fc,'的华氏度为:%fF' %(c*(9/5)+32))
      elif fc.endswith('F') == True:#判断输入的是否为华氏度
         f = float(fc.split('F')[0])
         print(fc,'的摄氏度为:%fC' %((f-32)*5/9))
      elif fc=='Q' or fc=='q':
         break
      elif fc.endswith('C') == False or fc.endswith('F') == False:
         print('请输入正确的华氏度(F)或摄氏度(C),以F或C结尾')
fc()
