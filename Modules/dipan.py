class Di_Pan():

    def __init__(self):
        self.address = {1:(2,1),2:(0,2),3:(1,0),4:(0,0),5:(1,1),6:(2,2),7:(1,2),8:(2,0),9:(0,1)}

    def _gan_zhi(self):
        return self.gan + self.zhi

    def _month_date(self):
        return self.month + self.date *0.01

    def get_date(self):
        while True:
            print('请输入阳历日期:<月份>.<日期>\nep:11.04')
            date_str = input().split('.')
            if len(date_str) == 1:
                print('请注意格式为<月份>.<日期>')
                continue
            elif int(date_str[0]) > 12:
                print('月份输入不合法,月份不能大于12')
                continue
            elif int(date_str[1]) > 31:
                print('日期输入不合法,日期不能大于31')
                continue
            break

        while True:
            print('请输入阴历月份:<月份>\nep:10')
            luner_month = input()
            if int(luner_month) > 12:
                print('月份输入不合法,月份不能大于12')
                continue
            elif int(luner_month) <= 0:
                print('月份输入不合法,月份不能小于1')
                continue
            break

        self.month,self.date,self.luner_month = int(date_str[0]),int(date_str[1]),int(luner_month)
        print('###日期:{0}'.format(self._month_date()))
        return 

    def get_ganzhi(self):
        """
        quickly get ganzhi of the date
        input:None
        return:str,2 chinese word,the date of ganzhi
        """
        def simple_input():
            """
            make the input easily
            input:None
            return:str
            """
            x = input()
            if len(x) == 2:
                return f'{x[0]} {x[1]}'
            else:
                return x
        
        gan_dict = {'1':'甲','2':'乙','3':'丙','4':'丁','5':'戊','6':'己','7':'庚','8':'辛','9':'壬','10':'癸'}
        zhi_dict = {'1':'子','2':'丑','3':'寅','4':'某','5':'辰','6':'巳','7':'午','8':'未','9':'申','10':'酉','11':'戌','12':'亥'}
        print('请输入干支日:<int> <int>\n1:甲2:乙3:丙4:丁5:戊6:己7:庚8:辛9:壬10:癸\n1:子2:丑3:寅4:某5:辰6:巳7:午8:未9:申10:酉11:戌12:亥')
        ganzhi = simple_input()
        ganzhi = ganzhi.split(' ')
        ganzhi_str = '{0}{1}'.format(gan_dict[ganzhi[0]],zhi_dict[ganzhi[1]])

        while True:
            print('请确认干支日为: {0} 日.正确请输1,错误请更正'.format(ganzhi_str)+'\n1:甲2:乙3:丙4:丁5:戊6:己7:庚8:辛9:壬10:癸\n1:子2:丑3:寅4:某5:辰6:巳7:午8:未9:申10:酉11:戌12:亥')
            check= simple_input()
            if check == '1'or check == '':
                break
            else:
                ganzhi = check.split(' ')
                ganzhi_str = '{0}{1}'.format(gan_dict[ganzhi[0]],zhi_dict[ganzhi[1]])
        
        self.gan,self.zhi = gan_dict[ganzhi[0]],zhi_dict[ganzhi[1]]
        return ganzhi_str

    def qi_ju(self):

        yuan_check = {'甲子':'上元','乙丑':'上元','丙寅':'上元','丁某':'上元','戊辰':'上元',
                    '己巳':'中元','庚午':'中元','辛未':'中元','壬申':'中元','癸酉':'中元',
                    '甲戌':'下元','乙亥':'下元','丙子':'下元','丁丑':'下元','戊寅':'下元',
                    '己某':'上元','庚辰':'上元','辛巳':'上元','壬午':'上元','癸未':'上元',
                    '甲申':'中元','乙酉':'中元','丙戌':'中元','丁亥':'中元','戊子':'中元',
                    '己丑':'下元','庚寅':'下元','辛某':'下元','壬辰':'下元','癸巳':'下元',
                    '甲午':'上元','乙未':'上元','丙申':'上元','丁酉':'上元','戊戌':'上元',
                    '己亥':'中元','庚子':'中元','辛丑':'中元','壬寅':'中元','癸某':'中元',
                    '甲辰':'下元','乙巳':'下元','丙午':'下元','丁未':'下元','戊申':'下元',
                    '己酉':'上元','庚戌':'上元','辛亥':'上元','壬子':'上元','癸丑':'上元',
                    '甲寅':'中元','乙某':'中元','丙辰':'中元','丁巳':'中元','戊午':'中元',
                    '己未':'下元','庚申':'下元','辛酉':'下元','壬戌':'下元','癸亥':'下元'}
        solar_terms = {12.22:{'solar_term':'冬至','上元':[1,1],'中元':[1,7],'下元':[1,4]}
                    ,12.07:{'solar_term':'大雪','上元':[0,4],'中元':[0,7],'下元':[0,1]}
                    ,11.22:{'solar_term':'小雪','上元':[0,5],'中元':[0,8],'下元':[0,2]}
                    ,11.07:{'solar_term':'立冬','上元':[0,6],'中元':[0,9],'下元':[0,3]}
                    ,10.23:{'solar_term':'霜降','上元':[0,5],'中元':[0,8],'下元':[0,2]}
                    ,10.08:{'solar_term':'寒露','上元':[0,6],'中元':[0,9],'下元':[0,3]}
                    ,9.23:{'solar_term':'秋分','上元':[0,7],'中元':[0,1],'下元':[0,4]}
                    ,9.08:{'solar_term':'白露','上元':[0,9],'中元':[0,3],'下元':[0,6]}
                    ,8.23:{'solar_term':'处暑','上元':[0,1],'中元':[0,4],'下元':[0,7]}
                    ,8.07:{'solar_term':'立秋','上元':[0,2],'中元':[0,5],'下元':[0,8]}
                    ,7.23:{'solar_term':'大暑','上元':[0,7],'中元':[0,1],'下元':[0,4]}
                    ,7.07:{'solar_term':'小暑','上元':[0,8],'中元':[0,2],'下元':[0,5]}
                    ,6.21:{'solar_term':'夏至','上元':[0,9],'中元':[0,3],'下元':[0,6]}
                    ,6.05:{'solar_term':'芒种','上元':[1,6],'中元':[1,3],'下元':[1,9]}
                    ,5.2:{'solar_term':'小满','上元':[1,5],'中元':[1,2],'下元':[1,8]}
                    ,5.05:{'solar_term':'立夏','上元':[1,4],'中元':[1,1],'下元':[1,7]}
                    ,4.2:{'solar_term':'谷雨','上元':[1,5],'中元':[1,2],'下元':[1,8]}
                    ,4.05:{'solar_term':'清明','上元':[1,4],'中元':[1,1],'下元':[1,7]}
                    ,3.2:{'solar_term':'春分','上元':[1,3],'中元':[1,9],'下元':[1,6]}
                    ,3.05:{'solar_term':'惊蛰','上元':[1,1],'中元':[1,7],'下元':[1,4]}
                    ,2.19:{'solar_term':'雨水','上元':[1,9],'中元':[1,6],'下元':[1,3]}
                    ,2.04:{'solar_term':'立春','上元':[1,8],'中元':[1,5],'下元':[1,2]}
                    ,1.2:{'solar_term':'大寒','上元':[1,3],'中元':[1,9],'下元':[1,6]}
                    ,1.05:{'solar_term':'小寒','上元':[1,2],'中元':[1,8],'下元':[1,5]}}

        date = self._month_date()
        if date in [1.01,1.02,1.03,1.04]:
            self.term = '冬至'
            print('###当前处于冬至节气')
            res = solar_terms[12.22][yuan_check[self.gan_zhi()]]
        else:
            for i in solar_terms:
                if date <= i:
                    continue
                else:
                    last_term = i
                    break

            self.term = solar_terms[last_term]['solar_term']
            print('###当前处于{0}节气'.format(self.term))
            res = solar_terms[last_term][yuan_check[self._gan_zhi()]]
        
        self.yin_yang,self.start = res
        res_dict1 = {0:'阴',1:'阳'}
        res_dict2 = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}
        print('###应起 {0} {1} 局'.format(res_dict1[res[0]],res_dict2[res[1]]))
        return res

    def pai_pan(self):
        platform = [[4,9,2]
                   ,[3,5,7]
                   ,[8,1,6]]
        
        # self.address = {1:(2,1),2:(0,2),3:(1,0),4:(0,0),5:(1,1),6:(2,2),7:(1,2),8:(2,0),9:(0,1)}
        address = self.address
        jiugong_wuxing = {1:'水',2:'土',3:'木',4:'木',5:'土',6:'金',7:'金',8:'土',9:'火'}
        tian_gan_yang = ['戊','己','庚','辛','壬','癸','丁','丙','乙']
        tian_gan_yin = ['戊','乙','丙','丁','癸','壬','辛','庚','己']
        jiu_gong = list(range(1,10))*2
        array = jiu_gong[self.start - 1:self.start + 8]
        gan_address = {}
        if self.yin_yang == 1:
            for i in range(9):
                platform[address[array[i]][0]][address[array[i]][1]] = tian_gan_yang[i]
                gan_address[tian_gan_yang[i]] = address[array[i]]
                if tian_gan_yang[i] == self.gan:
                    self.gan_jiugong_wuxing = jiugong_wuxing[array[i]]


        elif self.yin_yang == 0:
            for i in range(9):
                platform[address[array[i]][0]][address[array[i]][1]] = tian_gan_yin[i]
                gan_address[tian_gan_yin[i]] = address[array[i]]
                if tian_gan_yin[i] == self.gan:
                    self.gan_jiugong_wuxing = jiugong_wuxing[array[i]]

        self.platform,self.gan_address = platform,gan_address
        print(f'###排盘应为\
            \n{platform[0][0]} {platform[0][1]} {platform[0][2]}\
            \n{platform[1][0]} {platform[1][1]} {platform[1][2]}\
            \n{platform[2][0]} {platform[2][1]} {platform[2][2]}')
        return platform

    def fortune_judge(self):     
        sheng_Ke = {'金':{'金':2,'木':-1,'水':0,'火':-2,'土':1}
                ,'木':{'金':-2,'木':2,'水':1,'火':0,'土':-1}
                ,'水':{'金':1,'木':0,'水':2,'火':-1,'土':-2}
                ,'火':{'金':-1,'木':0,'水':-2,'火':2,'土':1}
                ,'土':{'金':1,'木':-2,'水':-1,'火':0,'土':2}}
        
            
        tiangan_wuxing = {'甲':'木','乙':'木','丙':'火','丁':'火','戊':'土','己':'土','庚':'金','辛':'金','壬':'水','癸':'水'}
        lunar_wuxing = {'1':'木','2':'木','3':'土','4':'火','5':'火','6':'土','7':'金','8':'金','9':'土','10':'水','11':'水','12':'土'}
        fortun = {2:'旺',1:'相',0:'休',-1:'囚',-2:'死'}
        result = {2:'大吉',1:'小吉',0:'一般',-1:'小凶',-2:'大凶'}

        self.gan_wuxing,self.luner_month_wuxing = tiangan_wuxing[self.gan],lunar_wuxing[str(self.luner_month)]
        print('###日干五行为:{0}\n###日干九宫五行为:{1}\n###阴历月份五行为:{2}'\
              .format(self.gan_wuxing,self.gan_jiugong_wuxing,self.luner_month_wuxing))
        self.res = [sheng_Ke[self.gan_wuxing][self.gan_jiugong_wuxing]
            ,sheng_Ke[self.gan_wuxing][self.luner_month_wuxing]]
        
        print('###日干与日干九宫五行关系为:{0}\n###日干与阴历月份五行关系为:{1}'.format(fortun[self.res[0]],fortun[self.res[1]]))
        print('###日干与九宫的凶吉:{0}\n###日干与月份的凶吉:{1}\n###最终凶吉为:{2}'\
              .format(result[self.res[0]],result[self.res[1]],result[self.res[0] + self.res[1]]))

        return self.res
    
    def Run(self,Date = 0,Lunar_Month = 0,Gan_Zhi = ''):
        if Date == 0 or Lunar_Month == 0:
            self.get_date()
        else:
            x = str(Date)
            self.month = int(x.split('.')[0])
            self.date = (Date - self.month) * 100
            self.luner_month = Lunar_Month
        
        if Gan_Zhi == '':
            self.get_ganzhi()
        else:
            self.gan = Gan_Zhi[0]
            self.zhi = Gan_Zhi[1]

        self.qi_ju()
        self.pai_pan()
        self.fortune_judge()



if __name__ =='__main__':
    a = Di_Pan()
    a.Run(11.4,10,'戊申')