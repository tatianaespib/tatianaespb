"""
Created on Tue Dec 12 23:12:26 2017
@author: tatiana
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
import matplotlib . cm as cm
#import matplotlib . pyplot as plt
#from scipy.integrate import odeint
#from scipy.integrate import simps

lat=[4.84, 4.6295, 6.5922,5.8925,
6.1908,
5.5635,
8.2388,
7.1072,
5.3540,
5.2237,
7.3395,
7.4923,
6.5395,
6.4355,
8.8010,
5.2242,
5.6522,
7.8847,
7.0788,
7.8647,
7.8647]
lon=[-74.32,
-73.7318,
-73.1823,
-73.0832,
-75.5288,
-74.8692,
-73.3193,
-73.7120,
-72.4207,
-75.3902,
-72.6995,
-74.8580,
-74.4563,
-71.7913,
-74.0713,
-75.3647,
-74.0723,
-72.8037,
-73.1935,
-72.3143,
-72.3143]
XX=[575400.7147296695/10000, 640672.9820947035/10000,  700969.1199611691/10000, 
    712211.3711808915/10000, 441497.8561116094/10000,  514486.6711358411/10000,
    685128.0322348007/10000, 642239.9017542474/10000,  785863.1925708719/10000,
    456759.3075756032/10000, 753970.9765343076/10000,  515667.04888322594/10000,
    560110.0518276326/10000, 191222.52581942012/10000, 602136.5856000741 /10000,
    459585.2056145407/10000, 602735.6556701135/10000,  742155.4523315106/10000,
    699528.3943104575/10000, 796163.8304272677/10000,  796163.8304272677/10000]
    
YY=[535015.9361958163/10000, 511835.68812590506/10000, 729034.4369922687/10000, 
    651685.8310805222/10000, 684325.2020447565/10000,  614954.8860266501/10000,
    911086.8912422981/10000, 785797.3152831029/10000,  592395.8275373387/10000,
    577405.2452757183/10000, 811931.293819654/10000,   828174.0362171566/10000,
    722875.1557904852/10000, 712189.6144199349/10000,   972978.0676692885 /10000,
    577458.8210905782/10000, 624840.1591418274/10000,  872188.2120861439/10000,
    782847.6777407565/10000, 870290.5980394688/10000,  870290.5980394688/10000]


velini=[6.13580, 6.4131, 6.4683, 6.5234, 6.5786, 6.6889, 6.7992, 7.0195, 7.0798, 7.1302,
     7.2405, 7.4611, 7.6817, 8.1126, 8.2884, 8.5642]
     
#Qini=[-0.0300*10000, 0.0030*10000, 0.0360*10000, 0.0690*10000, 0.1020*10000, 
#      0.1681*10000, 0.2341*10000,0.3001*10000,0.3661*10000, 0.4321*10000,
#      0.4982*10000, 0.6302*10000, 0.7622*10000, 0.9603*10000, 1.1254*10000, 
#      1.2904*10000]
Qini=[12.7589,  111.7872,  184.5341, 234.5934, 265.3523,  281.4829,  255.8868,  208.2153,  
      154.8113,  108.7083,   79.6311+100, 94.9078+100,  212.2594,  474.8006,  534.8117,   81.7464]


lon1=[lon[2], lon[7], lon[10], lon[17], lon[18], lon[19]]

lat1=[lat[2], lat[7], lat[10], lat[17], lat[18], lat[19]]


XX1=[XX[2], XX[7], XX[10], XX[17], XX[18], XX[19]]

YY1=[YY[2], YY[7], YY[10], YY[17], YY[18], YY[19]]

A0=np.zeros((100,100))
AQ002=np.zeros((15,18))
A002=np.zeros((15,18))
AQ0=np.zeros((100,100))
m=15-1


for i in range (len(A0)):
    for j in range (len(A0)):
        
        A0[:,:]=velini[0]#4.8090
        AQ0[:,:]=Qini[0]        
        
        A0[np.round(YY1[0]+1),np.round(XX1[0])]=random.uniform(velini[0]-0.012699, velini[0]-0.012302, (1))
        A0[np.round(YY1[1]),np.round(XX1[1]+1)]=random.uniform(velini[0]+0.0162, velini[0]+0.01567, (1,1))
        A0[YY1[2]-1,XX1[2]-3]=random.uniform(velini[0]-0.00819699,velini[0]-0.00919302, (1,1))
        AQ0[YY1[1],XX1[1]+1]=random.uniform(Qini[0]+0.04787, Qini[0]+0.05678, (1,1))
        AQ0[YY1[2]-1,XX1[2]-3]=random.uniform(Qini[0]-0.03456, Qini[0]-0.0456, (1,1))
        AQ0[YY1[0]+1,XX1[0]]=random.uniform(Qini[0]-0.06699, Qini[0]-0.07302, 1)
A02=A0[70:85,62:80]
AQ02=AQ0[70:85,62:80]
for r in range (15):   
        A002[r,:]=A02[m-r,:]    
        AQ002[r,:]=AQ02[m-r,:] 


A10=np.zeros((100,100))
AQ10=np.zeros((100,100))
AQ102=np.zeros((15,18))
A102=np.zeros((15,18))
for i in range (len(A10)):
    for j in range (len(A10)):
        A10[:,:]=velini[2]
        AQ10[:,:]=Qini[2]#4.8090
        #A10[:,:]=random.uniform(velini[2]-0.0010, velini[2]+0.0060, 100)#4.8090
        
     
        
        A10[YY1[0]+2:YY1[0]+3,XX1[0]-2:XX1[0]]=random.uniform(velini[2]-0.01082699, velini[2]-0.01092302, (1))
        A10[YY1[0]+3,XX1[0]-4]=random.uniform(velini[2]+0.02699, velini[2]+0.02302, (1))        
        A10[YY1[2]-1,XX1[2]-1]=random.uniform(velini[2]-0.00819699,velini[2]-0.00919302, (1,1))
        A10[YY1[1]-1:YY1[1],XX1[1]-1:XX1[1]+1]=random.uniform(velini[2]+0.0262, velini[2]+0.02567, (1,1))
        A10[YY1[2]+1:YY[2]+2,XX1[2]-2:XX1[2]]=random.uniform(velini[2]-0.019699,velini[2]-0.019302, (1,1))
        A10[YY1[4]:YY1[4]+2,XX1[4]:XX1[4]+1]=random.uniform(velini[2]-0.019699,velini[2]-0.019302, (1,1))        
        A10[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
        A10[YY1[4]-1:YY1[4],XX1[4]-1:XX1[4]]=random.uniform(velini[2]-0.009699,velini[2]-0.009302, (1,1))
        
        
        AQ10[YY1[1]-1:YY1[1]+1,XX1[1]-1:XX1[1]+1]=random.uniform(Qini[2]+1, Qini[2]+0.5678, (1,1))
        AQ10[YY1[2]-1,XX1[2]-1]=random.uniform(Qini[2]-0.3456, Qini[2]-0.456, (1,1))
        AQ10[YY1[2]+1:YY[2]+2,XX1[2]-2:XX1[2]]=random.uniform(Qini[2]-0.3456, Qini[2]-0.456, (1,1))
        AQ10[YY1[0]+2:YY1[0]+3,XX1[0]-2:XX1[0]]=random.uniform(Qini[2]-0.9699, Qini[2]-0.8302, 1)
        AQ10[YY1[0]+3,XX1[0]-4]=random.uniform(Qini[2]+0.2699, Qini[2]+0.2302, (1))
        AQ10[YY1[4]:YY1[4]+2,XX1[4]:XX1[4]+1]=random.uniform(Qini[2]-0.3456, Qini[2]-0.456, (1,1))
        AQ10[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(Qini[2]-0.53456, Qini[2]-0.6456, (1,1))
        AQ10[YY1[4]-1:YY1[4],XX1[4]-1:XX1[4]]=random.uniform(Qini[2]-0.53456, Qini[2]-0.7456, (1,1))
        
A210=A10[70:85,62:80]
A2Q10=AQ10[70:85,62:80]
for r in range (15):   
        A102[r,:]=A210[m-r,:]    
        AQ102[r,:]=A2Q10[m-r,:] 


        
        
A30=np.zeros((100,100))
AQ30=np.zeros((100,100))
AQ302=np.zeros((15,18))
A302=np.zeros((15,18))
for i in range (len(A30)):
    for j in range (len(A30)):
        A30[:,:]=velini[5]
        AQ30[:,:]=Qini[5]#4.8090
        #A10[:,:]=random.uniform(velini[2]-0.0010, velini[2]+0.0060, 100)#4.8090
        
     
        
        A30[YY1[0]+2:YY1[0]+3,XX1[0]-2:XX1[0]]=random.uniform(velini[5]-0.01082699, velini[5]-0.01092302, (1))
        A30[YY1[0]+1,XX1[0]]=random.uniform(velini[5]-0.01062699, velini[5]-0.01072302, (1))                
        A30[YY1[2]-1,XX1[2]-1]=random.uniform(velini[5]-0.00819699,velini[5]-0.00919302, (1,1))
        A30[YY1[1]-2:YY1[1],XX1[1]-1:XX1[1]+1]=random.uniform(velini[5]+0.0262, velini[5]+0.02567, (1,1))
        
        A30[YY1[2]+1:YY[2]+2,XX1[2]-2:XX1[2]]=random.uniform(velini[5]-0.019699,velini[5]-0.019302, (1,1))
        A30[YY1[4]:YY1[4]+2,XX1[4]+3:XX1[4]+4]=random.uniform(velini[5]+0.019699,velini[5]+0.019302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
        A30[YY1[4]-1:YY1[4],XX1[4]-1:XX1[4]]=random.uniform(velini[5]-0.009699,velini[5]-0.009302, (1,1))
        
        
        AQ30[YY1[1]-2:YY1[1],XX1[1]-1:XX1[1]+1]=random.uniform(Qini[5]+1, Qini[5]+0.5678, (1,1))
        AQ30[YY1[2]-1,XX1[2]-1]=random.uniform(Qini[5]-0.3456, Qini[5]-0.456, (1,1))
        AQ30[YY1[2]+1:YY[2]+2,XX1[2]-2:XX1[2]]=random.uniform(Qini[5]-0.3456, Qini[5]-0.456, (1,1))
        AQ30[YY1[0]+2:YY1[0]+3,XX1[0]-2:XX1[0]]=random.uniform(Qini[5]-0.9699, Qini[5]-0.8302, 1)
        AQ30[YY1[0]+1,XX1[0]]=random.uniform(Qini[5]-0.2699, Qini[5]-0.2302, (1))
        AQ30[YY1[4]:YY1[4]+2,XX1[4]+3:XX1[4]+4]=random.uniform(Qini[5]+0.3456, Qini[5]+0.456, (1,1))
        AQ30[YY1[4]-1:YY1[4],XX1[4]-1:XX1[4]]=random.uniform(Qini[5]-0.53456, Qini[5]-0.6456, (1,1))
#        AQ30[YY1[4]-0.5:YY1[4],XX1[4]-1:XX1[4]]=random.uniform(Qini[5]-0.53456, Qini[5]-0.7456, (1,1))
        
A230=A30[70:85,62:80]
A2Q30=AQ30[70:85,62:80]
for r in range (15):   
        A302[r,:]=A230[m-r,:]    
        AQ302[r,:]=A2Q30[m-r,:] 


       
        
A50=np.zeros((100,100))
AQ50=np.zeros((100,100))
AQ502=np.zeros((15,18))
A502=np.zeros((15,18))
for i in range (len(A50)):
    for j in range (len(A50)):
        A50[:,:]=velini[7]
        AQ50[:,:]=Qini[7]#4.8090
        
        A50[np.round(YY1[0]+2),np.round(XX1[0])]=random.uniform(velini[7]+0.012699, velini[7]+0.012302, (1))
        A50[YY1[0]+1:YY1[0]+3,XX1[0]-2:XX1[0]]=random.uniform(velini[7]-0.01382699, velini[7]-0.01492302, (1))
        A50[YY1[0]+3,XX1[0]-2]=random.uniform(velini[7]-0.01282699, velini[7]-0.01392302, (1))
        A50[YY1[0]+1,XX1[0]-3]=random.uniform(velini[7]-0.01062699, velini[7]-0.01072302, (1))                
        A50[YY1[2]-3,XX1[2]-4]=random.uniform(velini[7]+0.00819699,velini[7]+0.00919302, (1,1))
        A50[YY1[1]-2,XX1[1]-1]=random.uniform(velini[7]+0.0262, velini[7]+0.02567, (1,1))
        A50[YY1[1]-1,XX1[1]]=random.uniform(velini[7]+0.0272, velini[7]+0.02667, (1,1))
        A50[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(velini[7]+0.0232, velini[7]+0.02467, (1,1))        
        A50[YY1[2]-2,XX1[2]-3:XX1[2]-2]=random.uniform(velini[7]-0.015299,velini[7]-0.016102, (1,1))
        A50[YY1[4]-1,XX1[4]+1]=random.uniform(velini[7]+0.019699,velini[7]+0.019302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
        A50[YY1[4]-1,XX1[4]]=random.uniform(velini[7]+0.009699,velini[7]+0.009302, (1,1))
        A50[YY1[4],XX1[4]:XX1[4]+1]=random.uniform(velini[7]+0.009399,velini[7]+0.009502, (1,1))
        
        AQ50[np.round(YY1[0]+2),np.round(XX1[0])]=random.uniform(Qini[7]+0.12699, Qini[7]+0.12302, (1))
        AQ50[YY1[0]+1:YY1[0]+3,XX1[0]-2:XX1[0]]=random.uniform(Qini[7]-0.382699, Qini[7]-0.492302, (1))
        AQ50[YY1[0]+3,XX1[0]-2]=random.uniform(Qini[7]-0.282699, Qini[7]-0.392302, (1))
        AQ50[YY1[0]+1,XX1[0]-3]=random.uniform(Qini[7]-0.62699, Qini[7]-0.72302, (1))                
        AQ50[YY1[2]-3,XX1[2]-4]=random.uniform(Qini[7]+0.819699,Qini[7]+0.919302, (1,1))
        AQ50[YY1[1]-2,XX1[1]-1]=random.uniform(Qini[7]+0.62, Qini[7]+0.567, (1,1))
        AQ50[YY1[1]-1,XX1[1]]=random.uniform(Qini[7]+0.72, Qini[7]+0.667, (1,1))
        AQ50[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(Qini[7]+0.232,Qini[7]+0.2467, (1,1))        
        AQ50[YY1[2]-2,XX1[2]-3:XX1[2]-2]=random.uniform(Qini[7]-0.5299,Qini[7]-0.6102, (1,1))
        AQ50[YY1[4]-1,XX1[4]+1]=random.uniform(Qini[7]+0.19699,Qini[7]+0.19302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
        AQ50[YY1[4]-1,XX1[4]]=random.uniform(Qini[7]+0.699,Qini[7]+0.302, (1,1))
        AQ50[YY1[4],XX1[4]:XX1[4]+1]=random.uniform(Qini[7]+0.399,Qini[7]+0.69502, (1,1))
        

#      
A250=A50[70:85,62:80]
A2Q50=AQ50[70:85,62:80]
for r in range (15):   
        A502[r,:]=A250[m-r,:]    
        AQ502[r,:]=A2Q50[m-r,:] 
        
        
        
        
AQ802=np.zeros((15,18))
A802=np.zeros((15,18))              
A80=np.zeros((100,100))
AQ80=np.zeros((100,100))
for i in range (len(A80)):
    for j in range (len(A80)):
        #AQ70[:,:]=309.8
        A80[:,:]=velini[10]
        AQ80[:,:]=Qini[10]#4.8090
        A80[YY1[0]+2,XX1[0]+2]=random.uniform(velini[10]+0.012699, velini[10]+0.012302, (1))
        A80[YY1[0]+4,XX1[0]:XX1[0]+3]=random.uniform(velini[10]+0.01382699, velini[10]+0.01492302, (1))
        A80[YY1[0]+3,XX1[0]-2]=random.uniform(velini[10]-0.01282699, velini[10]-0.01392302, (1))
        A80[YY1[0]+3,XX1[0]]=random.uniform(velini[10]-0.01282699, velini[10]-0.01392302, (1))        
        
        A80[YY1[0]+2,XX1[0]-1]=random.uniform(velini[10]-0.01252699, velini[10]-0.01352302, (1))
        A80[YY1[0]+3,XX1[0]+2]=random.uniform(velini[10]+0.01062699, velini[10]+0.01072302, (1))  
        A80[YY1[0]+2,XX1[0]+1]=random.uniform(velini[10]+0.01042699, velini[10]+0.01062302, (1))  
        A80[YY1[0]+3,XX1[0]+1]=random.uniform(velini[10]+0.01042399, velini[10]+0.01052302, (1))            
        A80[YY1[0]+2,XX1[0]]=random.uniform(velini[10]+0.01042699, velini[10]+0.01062302, (1))        
        A80[YY1[2]-4,XX1[2]-4]=random.uniform(velini[10]+0.00819699,velini[10]+0.00919302, (1,1))
        A80[YY1[1]-4,XX1[1]-1]=random.uniform(velini[10]+0.0262, velini[10]+0.02567, (1,1))
        A80[YY1[1]-3,XX1[1]]=random.uniform(velini[10]+0.0272, velini[10]+0.02667, (1,1))
        A80[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(velini[10]+0.0232, velini[10]+0.02467, (1,1))        
        A80[YY1[2]-2,XX1[2]-3:XX1[2]-2]=random.uniform(velini[10]-0.015299,velini[10]-0.016102, (1,1))
        A80[YY1[4],XX1[4]-1:XX1[4]+2]=random.uniform(velini[10]+0.019699,velini[10]+0.019302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
        A80[YY1[4]-2,XX1[4]]=random.uniform(velini[10]+0.009699,velini[10]+0.009302, (1,1))
        A80[YY1[4]-1,XX1[4]:XX1[4]+3]=random.uniform(velini[10]+0.009399,velini[10]+0.009502, (1,1))
        
        AQ80[[YY1[0]+2,XX1[0]+2]]=random.uniform(Qini[10]+0.12699, Qini[10]+0.12302, (1))
#        AQ80[YY1[0]+4,XX1[0]:XX1[0]+3]=random.uniform(Qini[10]+0.382699, Qini[10]+0.492302, (1))
        AQ80[YY1[0]+3,XX1[0]-2]=random.uniform(Qini[10]-0.282699, Qini[10]-0.392302, (1))
        AQ80[YY1[0]+3,XX1[0]]=random.uniform(Qini[10]-0.282699, Qini[10]-0.392302, (1))
        AQ80[YY1[0]+3,XX1[0]+2]=random.uniform(Qini[10]+0.62699, Qini[10]+0.72302, (1))                
        AQ80[YY1[0]+2,XX1[0]-1]=random.uniform(Qini[10]-0.281699, Qini[10]-0.391302, (1))
        AQ80[YY1[0]+2,XX1[0]+1]=random.uniform(Qini[10]+0.62499, Qini[10]+0.72502, (1))        
        AQ80[YY1[0]+3,XX1[0]+1]=random.uniform(Qini[10]+0.62399, Qini[10]+0.72402, (1))
        AQ80[YY1[0]+2,XX1[0]]=random.uniform(Qini[10]+0.62399, Qini[10]+0.72402, (1))
        
        AQ80[YY1[2]-3,XX1[2]-4]=random.uniform(Qini[10]+0.819699,Qini[10]+0.919302, (1,1))
        AQ80[YY1[1]-2,XX1[1]-1]=random.uniform(Qini[10]+0.62, Qini[10]+0.567, (1,1))
        AQ80[YY1[1]-1,XX1[1]]=random.uniform(Qini[10]+0.72, Qini[10]+0.667, (1,1))
        AQ80[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(Qini[10]+0.232,Qini[10]+0.2467, (1,1))        
        AQ80[YY1[2]-2,XX1[2]-3:XX1[2]-2]=random.uniform(Qini[10]-0.5299,Qini[10]-0.6102, (1,1))
        AQ80[YY1[4],XX1[4]-1:XX1[4]+2]=random.uniform(Qini[10]+0.19699,Qini[10]+0.19302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
        AQ80[YY1[4]-2,XX1[4]]=random.uniform(Qini[10]+0.699,Qini[10]+0.302, (1,1))
        AQ80[YY1[4]-1,XX1[4]:XX1[4]+3]=random.uniform(Qini[10]+0.399,Qini[10]+0.69502, (1,1))


A280=A80[70:85,62:80]
A2Q80=AQ80[70:85,62:80]
for r in range (15):   
        A802[r,:]=A280[m-r,:]    
        AQ802[r,:]=A2Q80[m-r,:] 



AQ1002=np.zeros((15,18))
A1002=np.zeros((15,18))              
A100=np.zeros((100,100))
AQ100=np.zeros((100,100))
for i in range (len(A80)):
    for j in range (len(A80)):
        #AQ70[:,:]=309.8
        A100[:,:]=velini[11]
        AQ100[:,:]=Qini[11]#4.8090
        A100[YY1[0]+4,XX1[0]+2]=random.uniform(velini[11]+0.012699, velini[11]+0.012302, (1))
        A100[YY1[0]+3,XX1[0]:XX1[0]+3]=random.uniform(velini[11]+0.01382699, velini[11]+0.01492302, (1))
        A100[YY1[0]+3,XX1[0]-2]=random.uniform(velini[11]-0.01282699, velini[11]-0.01392302, (1))
        A100[YY1[0]+2,XX1[0]-1]=random.uniform(velini[11]-0.01252699, velini[11]-0.01352302, (1))
        A100[YY1[0]+3,XX1[0]+1]=random.uniform(velini[11]+0.01062699, velini[11]+0.01072302, (1))  
        A100[YY1[0]+4,XX1[0]+1]=random.uniform(velini[11]+0.01042699, velini[11]+0.01062302, (1))  
        A100[YY1[0]+4,XX1[0]-1]=random.uniform(velini[11]+0.01042399, velini[11]+0.01052302, (1))            
        A100[YY1[0]+4,XX1[0]]=random.uniform(velini[11]+0.01042699, velini[11]+0.01062302, (1))        
        A100[YY1[2]-4,XX1[2]-4]=random.uniform(velini[11]+0.00819699,velini[11]+0.00919302, (1,1))
        A100[YY1[1]-4,XX1[1]-1:XX1[1]]=random.uniform(velini[11]+0.0262, velini[11]+0.02567, (1,1))
        A100[YY1[1]-3,XX1[1]]=random.uniform(velini[11]+0.0272, velini[11]+0.02667, (1,1))
        A100[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(velini[11]+0.0232, velini[11]+0.02467, (1,1))        
        A100[YY1[2]-2,XX1[2]-3]=random.uniform(velini[11]-0.015299,velini[11]-0.016102, (1,1))
#        A100[YY1[4],XX1[4]-1:XX1[4]+2]=random.uniform(velini[11]+0.019699,velini[11]+0.019302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
#        A100[YY1[4]-2,XX1[4]]=random.uniform(velini[11]+0.009699,velini[11]+0.009302, (1,1))
#        A100[YY1[4]-1,XX1[4]:XX1[4]+3]=random.uniform(velini[11]+0.009399,velini[11]+0.009502, (1,1))
        
        
        
        AQ100[[YY1[0]+4,XX1[0]+2]]=random.uniform(Qini[11]+0.12699, Qini[11]+0.12302, (1))
        AQ100[YY1[0]+3,XX1[0]:XX1[0]+3]=random.uniform(Qini[11]+0.382699, Qini[11]+0.492302, (1))
        AQ100[YY1[0]+3,XX1[0]-2]=random.uniform(Qini[11]-0.282699, Qini[11]-0.392302, (1))
        AQ100[YY1[0]+2,XX1[0]-1]=random.uniform(Qini[11]-0.282699, Qini[11]-0.392302, (1))
        AQ100[YY1[0]+3,XX1[0]+1]=random.uniform(Qini[11]+0.62699, Qini[11]+0.72302, (1))                
        AQ100[YY1[0]+4,XX1[0]+1]=random.uniform(Qini[11]+0.281699, Qini[11]+0.391302, (1))
        AQ100[YY1[0]+4,XX1[0]-1]=random.uniform(Qini[11]+0.62499, Qini[11]+0.72502, (1))        
        AQ100[YY1[0]+4,XX1[0]]=random.uniform(Qini[11]+0.62399, Qini[11]+0.72402, (1))
#        AQ100[YY1[0]+2,XX1[0]]=random.uniform(Qini[11]+0.62399, Qini[11]+0.72402, (1))
        
        AQ100[YY1[2]-4,XX1[2]-4]=random.uniform(Qini[11]+0.819699,Qini[11]+0.919302, (1,1))
        AQ100[YY1[1]-4,XX1[1]-1]=random.uniform(Qini[11]+0.62, Qini[11]+0.567, (1,1))
        AQ100[YY1[1]-3,XX1[1]]=random.uniform(Qini[11]+0.72, Qini[11]+0.667, (1,1))
        AQ100[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(Qini[11]+0.232,Qini[11]+0.2467, (1,1))        
        AQ100[YY1[2]-2,XX1[2]-3:XX1[2]-2]=random.uniform(Qini[11]-0.5299,Qini[11]-0.6102, (1,1))
#        AQ100[YY1[4],XX1[4]-1:XX1[4]+2]=random.uniform(Qini[11]+0.19699,Qini[11]+0.19302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
#        AQ100[YY1[4]-2,XX1[4]]=random.uniform(Qini[11]+0.699,Qini[11]+0.302, (1,1))
#        AQ100[YY1[4]-1,XX1[4]:XX1[4]+3]=random.uniform(Qini[11]+0.399,Qini[11]+0.69502, (1,1))

A2100=A100[70:85,62:80]
A2Q100=AQ100[70:85,62:80]
for r in range (15):   
        A1002[r,:]=A2100[m-r,:]    
        AQ1002[r,:]=A2Q100[m-r,:] 
        
        
        
AQ1302=np.zeros((15,18))
A1302=np.zeros((15,18))              
A130=np.zeros((100,100))
AQ130=np.zeros((100,100))
for i in range (len(A130)):
    for j in range (len(A130)):
        #AQ70[:,:]=309.8
        A130[:,:]=velini[12]
        AQ130[:,:]=Qini[12]#4.8090
#        A130[YY1[0]+4,XX1[0]-1]=random.uniform(velini[12]+0.012699, velini[12]+0.012302, (1))
        A130[YY1[0]+3,XX1[0]-1:XX1[0]+1]=random.uniform(velini[12]+0.01382699, velini[12]+0.01492302, (1))
        A130[YY1[0]+3,XX1[0]-2]=random.uniform(velini[12]-0.01282699, velini[12]-0.01392302, (1))
        A130[YY1[0]+3,XX1[0]-1]=random.uniform(velini[12]-0.010252699, velini[12]-0.010352302, (1))
#        A130[YY1[0]+3,XX1[0]-2]=random.uniform(velini[12]+0.01062699, velini[12]+0.01072302, (1))  
        A130[YY1[0]+4,XX1[0]]=random.uniform(velini[12]+0.01042699, velini[12]+0.01062302, (1))  
        A130[YY1[0]+4,XX1[0]-1]=random.uniform(velini[12]+0.01042399, velini[12]+0.01052302, (1))            
#        A130[YY1[0]+4,XX1[0]]=random.uniform(velini[12]+0.01042699, velini[12]+0.01062302, (1))        
        A130[YY1[2]-4,XX1[2]-4]=random.uniform(velini[12]+0.00819699,velini[12]+0.00919302, (1,1))
#        A130[YY1[1]-4,XX1[1]-1:XX1[1]]=random.uniform(velini[12]+0.0262, velini[12]+0.02567, (1,1))
        A130[YY1[1]-3,XX1[1]]=random.uniform(velini[12]+0.0272, velini[12]+0.02667, (1,1))
#        A130[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(velini[12]+0.0232, velini[12]+0.02467, (1,1))        
#        A130[YY1[2]-2,XX1[2]-3]=random.uniform(velini[12]-0.015299,velini[12]-0.016102, (1,1))
#        A100[YY1[4],XX1[4]-1:XX1[4]+2]=random.uniform(velini[11]+0.019699,velini[11]+0.019302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
#        A100[YY1[4]-2,XX1[4]]=random.uniform(velini[11]+0.009699,velini[11]+0.009302, (1,1))
#        A100[YY1[4]-1,XX1[4]:XX1[4]+3]=random.uniform(velini[11]+0.009399,velini[11]+0.009502, (1,1))
        
        
        
#        AQ130[[YY1[0]+4,XX1[0]+2]]=random.uniform(Qini[12]+0.12699, Qini[12]+0.12302, (1))
        AQ130[YY1[0]+3,XX1[0]-1:XX1[0]+1]=random.uniform(Qini[12]+0.382699, Qini[12]+0.492302, (1))
        AQ130[YY1[0]+3,XX1[0]-2]=random.uniform(Qini[12]-0.282699, Qini[12]-0.392302, (1))
        AQ130[YY1[0]+2,XX1[0]-1]=random.uniform(Qini[12]-0.282699, Qini[12]-0.392302, (1))
        AQ130[YY1[0]+4,XX1[0]]=random.uniform(Qini[12]+0.62699, Qini[12]+0.72302, (1))                
        AQ130[YY1[0]+4,XX1[0]-1]=random.uniform(Qini[12]+0.281699, Qini[12]+0.391302, (1))
#        AQ130[YY1[0]+4,XX1[0]-1]=random.uniform(Qini[12]+0.62499, Qini[12]+0.72502, (1))        
#        AQ130[YY1[0]+4,XX1[0]]=random.uniform(Qini[12]+0.62399, Qini[12]+0.72402, (1))
#        AQ100[YY1[0]+2,XX1[0]]=random.uniform(Qini[11]+0.62399, Qini[11]+0.72402, (1))
        
#        AQ130[YY1[2]-4,XX1[2]-4]=random.uniform(Qini[12]+0.819699,Qini[12]+0.919302, (1,1))
#        AQ130[YY1[1]-4,XX1[1]-1]=random.uniform(Qini[12]+0.62, Qini[12]+0.567, (1,1))
        AQ130[YY1[1]-3,XX1[1]]=random.uniform(Qini[12]+0.72, Qini[12]+0.667, (1,1))
#        AQ130[YY1[1]-2,XX1[1]:XX1[1]+1]=random.uniform(Qini[12]+0.232,Qini[12]+0.2467, (1,1))        
#        AQ130[YY1[2]-2,XX1[2]-3:XX1[2]-2]=random.uniform(Qini[12]-0.5299,Qini[12]-0.6102, (1,1))
#        AQ100[YY1[4],XX1[4]-1:XX1[4]+2]=random.uniform(Qini[11]+0.19699,Qini[11]+0.19302, (1,1))        
#        A30[YY1[4]+1:YY1[4]+3,XX1[4]+1:XX1[4]+2]=random.uniform(velini[2]-0.0109999,velini[2]-0.010949302, (1,1))  
#        AQ100[YY1[4]-2,XX1[4]]=random.uniform(Qini[11]+0.699,Qini[11]+0.302, (1,1))
#        AQ100[YY1[4]-1,XX1[4]:XX1[4]+3]=random.uniform(Qini[11]+0.399,Qini[11]+0.69502, (1,1))

A2130=A130[70:85,62:80]
A2Q130=AQ130[70:85,62:80]
for r in range (15):   
        A1302[r,:]=A2130[m-r,:]    
        AQ1302[r,:]=A2Q130[m-r,:] 



AQ1502=np.zeros((15,18))
A1502=np.zeros((15,18))              
A150=np.zeros((100,100))
AQ150=np.zeros((100,100))
for i in range (len(A150)):
    for j in range (len(A150)):
        #AQ70[:,:]=309.8
        A150[:,:]=velini[13]
        AQ150[:,:]=Qini[13]#4.8090
        
        A150[YY1[0]+3:YY1[0]+4,XX1[0]]=random.uniform(velini[13]+0.02699, velini[13]+0.02302, (1))
        A150[YY1[0]+5,XX1[0]-1]=random.uniform(velini[13]-0.002699, velini[13]-0.002302, (1))
        A150[YY1[0]+2,XX1[0]]=random.uniform(velini[13]-0.01699, velini[13]-0.01302, (1))
#        A0[YY1[1]+2:YY1[1]+3,XX1[1]-1:XX1[1]]=random.uniform(velini[0]+0.0262, velini[0]+0.02567, (1,1))
#        A0[YY1[2]+1:YY1[2]+2,XX1[2]:XX1[2]+1]=random.uniform(velini[0]-0.019699,velini[0]-0.019302, (1,1))
#        AQ0[YY1[1]+2:YY1[1]+3,XX1[1]-1:XX1[1]]=random.uniform(Qini[0]+1, Qini[0]+0.5678, (1,1))
#        AQ0[YY1[2]+1:YY1[2]+2,XX1[2]:XX1[2]+1]=random.uniform(Qini[0]-0.3456, Qini[0]-0.456, (1,1))
#        AQ150[YY1[0]+4,XX1[0]]=random.uniform(Qini[13]+0.9699, Qini[13]+0.8302, 1) 
#        AQ150[YY1[0]+3,XX1[0]-1]=random.uniform(Qini[13]+0.9699, Qini[13]+0.8302, 1)
#        AQ150[YY1[0]+2,XX1[0]]=random.uniform(Qini[13]+0.8699, Qini[13]+0.7302, 1)
 

A2150=A150[70:85,62:80]
A2Q150=AQ150[70:85,62:80]
for r in range (15):   
        A1502[r,:]=A2150[m-r,:]    
        AQ1502[r,:]=A2Q150[m-r,:]        
        
        
#        A150[YY1[0]:YY1[0]+1,XX1[0]:XX1[0]+1]=random.uniform(velini[13]+0.02699, velini[13]+0.02902)
#        A150[YY1[0]:YY1[0]+1,XX1[0]+2:XX[0]+3]=random.uniform(velini[13]-0.03699, velini[13]-0.04302, (1))        
        
#        A150[YY1[4]:YY1[4]+1,XX1[4]:XX1[4]-1]=random.uniform(velini[13]-0.019699,velini[13]-0.019302, (1,1))        
#        
#        
#        AQ150[YY1[4]:YY1[4]+1,XX1[4]:XX1[4]-1]=random.uniform(Qini[13]+500-8.3456, Qini[13]+500-8.456, (1,1))
#        AQ150[YY1[0]+2:YY1[0]+3,XX1[0]-1:XX1[0]+1]=random.uniform(Qini[13]+500+5.9699, Qini[13]+500+5.8302, 1)
#        AQ150[YY1[0]-3:YY1[0]-2,XX1[0]-3]=random.uniform(Qini[13]+500+5.02699, Qini[13]+500+5.02302, (1))
        
#        AQ150[YY[7]-5:YY[7]-2,XX[7]-2:XX[7]+2]=random.uniform(Qini[13]+10.0010, Qini[13]+10.0260, (3,4))





valfa=np.arange(0.0,0.6,0.1)
porcn=np.zeros(len(valfa))
porA0=np.zeros(len(valfa))
porcn10=np.zeros(len(valfa))
porcnQ=np.zeros(len(valfa))
porAQ0=np.zeros(len(valfa))
porcn50=np.zeros(len(valfa))
porcn30=np.zeros(len(valfa))
porcn80=np.zeros(len(valfa))
i=0
for g in valfa:
    A0p=A002+ g*np.random.normal(A002)   #modelo perturbado
    difperA0=np.abs(A002-A0p)    #diferencia de modelos 
    errA0=np.abs(np.max(A002-A0p)/np.max(A002))*100   #error relativo porcentual 
#    A0chec=A0[70:85,62:80]+(g/4)*np.random.normal(A0[70:85,62:80])
#    errA0chec=np.abs(np.max(A0[70:85,62:80]-A0chec)/np.max(A0[70:85,62:80]))*100
    A00chec=A002+(g)*A002.std()*np.random.normal(A002)#g*difperA0.std()*np.random.normal(difperA0)    
#    porA0[i]=errA0chec
#    tabA0=np.abs(A0[70:85,62:80]-A0chec)
    tabA00=np.abs(A002-A00chec)
    porcn[i]=errA0    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ0p=AQ002 + g*np.random.normal(AQ002)   #modelo perturbado
    difperAQ0=np.abs(AQ002-AQ0p)    #diferencia de modelos 
    errAQ0=np.abs(np.max(AQ002-AQ0p)/np.max(AQ002))*100   #error relativo porcentual 
#    AQ0chec=AQ0[70:85,62:80]+(g/4)*np.random.normal(AQ0[70:85,62:80])
#    errAQ0chec=np.abs(np.max(A0[70:85,62:80]-AQ0chec)/np.max(A0[70:85,62:80]))*100
    AQ00chec=AQ002+(g)*AQ002.std()*np.random.normal(AQ002)    
#    porAQ0[i]=errAQ0chec
#    tabAQ0=np.abs(AQ0[70:85,62:80]-AQ0chec)
    tabAQ00=np.abs(AQ002-AQ00chec)
    porcnQ[i]=errAQ0    #porcentaje de error para modelos modelos perturbadon con alfa     
    
    
#    A10p=A102 + g*A102.std()*np.random.random(A102.shape)   #modelo perturbado
#    difperA10=np.abs(A102-A10p)    #diferencia de modelos 
#    errA10=np.abs(np.max(A102-A10p)/np.max(A102))*100   #error relativo porcentual 
#    A10chec=A102+(g)*A102.std()*np.random.random(A102.shape)    
#    tabA10=np.abs(A102-A10chec)
#    porcn10[i]=errA10    #porcentaje de error para modelos modelos perturbadon con alfa 

    A10p=A102+ g*np.random.random(A102.shape)   #modelo perturbado
    difperA10=np.abs(A102-A10p)    #diferencia de modelos 
    errA10=np.abs(np.max(A102-A10p)/np.max(A102))*100   #error relativo porcentual 
    A10chec=A102+(g/10)*A102.std()*np.random.random(AQ102.shape)    
    tabA10=np.abs(A102-A10chec) 

    
    AQ10p=AQ102+ g*np.random.random(AQ102.shape)   #modelo perturbado
    difperAQ10=np.abs(AQ102-AQ10p)    #diferencia de modelos 
    errAQ10=np.abs(np.max(AQ102-AQ10p)/np.max(AQ102))*100   #error relativo porcentual 
    AQ10chec=AQ102+(g/10)*AQ102.std()*np.random.random(AQ102.shape)    
    tabAQ10=np.abs(AQ102-AQ10chec) 

    A30p=A102 + g*np.random.normal(A302)   #modelo perturbado
    difperA30=np.abs(A302-A30p)    #diferencia de modelos 
    errA30=np.abs(np.max(A302-A30p)/np.max(A302))*100   #error relativo porcentual 
    A30chec=A302+(g)*A302.std()*np.random.normal(A302)    
    tabA30=np.abs(A302-A30chec)
    porcn30[i]=errA30    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ30p=AQ302+ g*np.random.normal(AQ302)   #modelo perturbado
    difperAQ30=np.abs(AQ302-AQ30p)    #diferencia de modelos 
    errAQ30=np.abs(np.max(AQ302-AQ10p)/np.max(AQ302))*100   #error relativo porcentual 
    AQ30chec=AQ302+(g/10)*AQ302.std()*np.random.normal(AQ302)    
    tabAQ30=np.abs(AQ302-AQ30chec)         
    
    
    A50p=A502 + g*np.random.normal(A502)   #modelo perturbado
    difperA50=np.abs(A502-A50p)    #diferencia de modelos 
    errA50=np.abs(np.max(A502-A50p)/np.max(A502))*100   #error relativo porcentual 
    A50chec=A502+(g)*A502.std()*np.random.normal(A502)    
    tabA50=np.abs(A502-A50chec)
    porcn50[i]=errA50    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ50p=AQ502+ g*np.random.normal(AQ502)   #modelo perturbado
    difperAQ50=np.abs(AQ502-AQ50p)    #diferencia de modelos 
    errAQ50=np.abs(np.max(AQ502-AQ50p)/np.max(AQ502))*100   #error relativo porcentual 
    AQ50chec=AQ502+(g/10)*AQ502.std()*np.random.normal(AQ502)    
    tabAQ50=np.abs(AQ502-AQ50chec) 
    
    A80p=A802 + g*np.random.normal(A802)   #modelo perturbado
    difperA80=np.abs(A802-A80p)    #diferencia de modelos 
    errA80=np.abs(np.max(A802-A80p)/np.max(A802))*100   #error relativo porcentual 
    A80chec=A802+(g)*A802.std()*np.random.normal(A802)    
    tabA80=np.abs(A802-A80chec)
#    porcn70[i]=errA70    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ80p=AQ802 + g*np.random.normal(A802)   #modelo perturbado
    difperAQ80=np.abs(AQ802-AQ80p)    #diferencia de modelos 
    errAQ80=np.abs(np.max(AQ802-AQ80p)/np.max(AQ802))*100   #error relativo porcentual 
    AQ80chec=AQ802+(g/10)*AQ802.std()*np.random.normal(AQ802)    
    tabAQ80=np.abs(AQ802-AQ80chec)     
    
    
    
    A100p=A1002 + g*np.random.normal(A1002)   #modelo perturbado
    difperA100=np.abs(A1002-A100p)    #diferencia de modelos 
    errA100=np.abs(np.max(A1002-A100p)/np.max(A1002))*100   #error relativo porcentual 
    A100chec=A1002+(g)*A1002.std()*np.random.normal(A1002)    
    tabA100=np.abs(A1002-A100chec)
#    porcn100[i]=errA100    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ100p=AQ1002 + g*np.random.normal(AQ1002)   #modelo perturbado
    difperAQ100=np.abs(AQ1002-AQ100p)    #diferencia de modelos 
    errAQ100=np.abs(np.max(AQ1002-AQ100p)/np.max(AQ1002))*100   #error relativo porcentual 
    AQ100chec=AQ1002+(g/4)*AQ1002.std()*np.random.normal(AQ1002)    
    tabAQ100=np.abs(AQ1002-AQ100chec) 
    
    
    A130p=A1302 + g*np.random.normal(A1302)   #modelo perturbado
    difperA130=np.abs(A1302-A130p)    #diferencia de modelos 
    errA130=np.abs(np.max(A1302-A130p)/np.max(A1302))*100   #error relativo porcentual 
    A130chec=A1302+(g)*A1302.std()*np.random.normal(A1302)    
    tabA130=np.abs(A1302-A130chec)
#    porcn100[i]=errA100    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ130p=AQ1302 + g*np.random.normal(AQ1302)   #modelo perturbado
    difperAQ130=np.abs(AQ1302-AQ130p)    #diferencia de modelos 
    errAQ130=np.abs(np.max(AQ1302-AQ130p)/np.max(AQ1302))*100   #error relativo porcentual 
    AQ130chec=AQ1302+(g/4)*AQ1302.std()*np.random.normal(AQ1302)    
    tabAQ130=np.abs(AQ1302-AQ130chec)     
    
    
    
    A150p=A1502 + g*np.random.normal(A1502)   #modelo perturbado
    difperA150=np.abs(A1502-A150p)    #diferencia de modelos 
    errA150=np.abs(np.max(A1502-A150p)/np.max(A1502))*100   #error relativo porcentual 
    A150chec=A1502+(g)*A1502.std()*np.random.normal(A150[70:85,62:80])    
    tabA150=np.abs(A1502-A150chec)
#    porcn150[i]=errA150    #porcentaje de error para modelos modelos perturbadon con alfa 
    
    AQ150p=AQ1502 + g*np.random.normal(AQ1502)   #modelo perturbado
    difperAQ150=np.abs(AQ1502-AQ150p)    #diferencia de modelos 
    errAQ150=np.abs(np.max(AQ1502-AQ150p)/np.max(AQ1502))*100   #error relativo porcentual 
    AQ150chec=AQ1502+(g/2)*AQ1502.std()*np.random.normal(AQ1502)    
    tabAQ150=np.abs(AQ1502-AQ150chec) 
    
        
           
    i=i+1
    
    
z = np.polyfit(valfa, porcn, 1)
E=20
alfa=(E+0.0012)/0.1424
um0=(np.max(tabA00)+np.min(tabA00))/2.0
um10=(np.max(A10chec)+np.min(A10chec))/2.0
um30=(np.max(tabA30)+np.min(tabA30))/2.0
um50=(np.max(tabA50)+np.min(tabA50))/2.0
um80=(np.max(tabA80)+np.min(tabA80))/2.0
um100=(np.max(tabA100)+np.min(tabA100))/2.0
um130=(np.max(tabA130)+np.min(tabA130))/2.0
um150=(np.max(tabA150)+np.min(tabA150))/2.0
umQ0=(np.max(tabAQ00)+np.min(tabAQ00))/2.0
umQ10=(np.max(tabAQ10)+np.min(tabAQ10))/2.0
umQ30=(np.max(tabAQ30)+np.min(tabAQ30))/2.0
umQ50=(np.max(tabAQ50)+np.min(tabAQ50))/2.0
umQ80=(np.max(tabAQ80)+np.min(tabAQ80))/2.0
umQ100=(np.max(tabAQ100)+np.min(tabAQ100))/2.0
umQ130=(np.max(tabAQ130)+np.min(tabAQ130))/2.0
umQ150=(np.max(tabAQ150)+np.min(tabAQ150))/2.0

tabA0um=np.ones((15,18))
tabAQ0um=np.ones((15,18))

tabA10um=np.zeros((15,18))

tabAQ10um=np.ones((15,18))

tabA30um=np.ones((15,18))
tabAQ30um=np.ones((15,18))

tabA80um=np.ones((15,18))
tabAQ80um=np.ones((15,18))

tabA50um=np.ones((15,18))
tabAQ50um=np.ones((15,18))

tabA100um=np.ones((15,18))
tabAQ100um=np.ones((15,18))

tabA130um=np.ones((15,18))
tabAQ130um=np.ones((15,18))

tabA150um=np.ones((15,18))
tabAQ150um=np.ones((15,18))
for i in range (0,15):
    for j in range (0,18):
        if tabA00[i,j]<=um0:
            tabA0um[i,j]=0
            
        if A102[i,j]!=velini[2]:
            tabA10um[i,j]=np.min(tabA10)
        else:
            tabA10um[i,j]=np.max(tabA10)
            
#        if A10chec[i,j]>6.47:
#            tabA10um[i,j]=np.max(tabA10)#(np.max(tabA10)+np.min(tabA10))/2.0
#        else:
#                tabA10um[i,j]=(np.max(tabA10)+np.min(tabA10))/2.0
            
        if tabA30[i,j]<=um30:
            tabA30um[i,j]=0
        if tabA50[i,j]<=um50:
            tabA50um[i,j]=0
        if tabA80[i,j]<=um80:
            tabA80um[i,j]=0
        if tabA100[i,j]<=um100:
            tabA100um[i,j]=0

        if tabA130[i,j]<=um130:
            tabA130um[i,j]=0            
            
        if tabA150[i,j]<=um150:
            tabA150um[i,j]=0
            
            
        if tabAQ00[i,j]>umQ0:
            tabAQ0um[i,j]=0
        if tabAQ30[i,j]>=umQ30:
            tabAQ30um[i,j]=0
        if tabAQ50[i,j]>=umQ50:
            tabAQ50um[i,j]=0
        if tabAQ80[i,j]>=umQ80:
            tabAQ80um[i,j]=0
        
        if tabAQ100[i,j]>=umQ100:
            tabAQ100um[i,j]=0
        if tabAQ130[i,j]>=umQ130:
            tabAQ130um[i,j]=0
        if tabAQ150[i,j]>=umQ150:
            tabAQ150um[i,j]=0
            
tabA10um[3:7,3:6]=((np.max(tabA10)+np.min(tabA10))/2.0)            
#plt.imshow(A002, cmap = cm.gist_earth, origin='upper')
plt.figure(0)
plt.subplot(3,2,1)
plt.title('Velocidad 0 km')

extent = (-74, -72, 6.0, 8.0)
#plt.plot(lon1,lat1)#,'vr', linewidth=10,extent=extent)
#plt.text(XX[2],YY[2], 'B2')
#plt.text(XX[7],YY[7], 'BR')
#plt.text(XX[10],YY[10], 'PM')
plt.imshow(A002, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colormesh(A0[70:85,62:80])#, extent=extent)
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 0 km')
plt.imshow(AQ002, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A00chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ00chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA0um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ00,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')


plt.savefig ('im0a.pdf')
plt.show()

plt.figure(1009)
plt.imshow(A102, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
plt.show()


plt.figure(10)
plt.subplot(3,2,1)
plt.title('Velocidad 10 km')

extent = (-74, -72, 6.0, 8.0)
#plt.plot(lon1,lat1)#,'vr', linewidth=10,extent=extent)
#plt.text(XX[2],YY[2], 'B2')
#plt.text(XX[7],YY[7], 'BR')
#plt.text(XX[10],YY[10], 'PM')
plt.imshow(A102, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colormesh(A0[70:85,62:80])#, extent=extent)
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 10 km')
plt.imshow(AQ102, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A10chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ10chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA10um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ10,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')
plt.savefig ('im10a.pdf')
plt.show()

plt.figure(30)
plt.subplot(3,2,1)
plt.title('Velocidad 30 km')

extent = (-74, -72, 6.0, 8.0)
#plt.plot(lon1,lat1)#,'vr', linewidth=10,extent=extent)
#plt.text(XX[2],YY[2], 'B2')
#plt.text(XX[7],YY[7], 'BR')
#plt.text(XX[10],YY[10], 'PM')
plt.imshow(A302, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colormesh(A0[70:85,62:80])#, extent=extent)
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 30 km')
plt.imshow(AQ302, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A30chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ30chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA30um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ30,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')


plt.savefig ('im30a.pdf')
plt.show()


plt.figure(50)
plt.subplot(3,2,1)
plt.title('Velocidad en 50 km')
extent = (-74, -72, 6.0,8.0)
plt.imshow(A502, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 50 km')
plt.imshow(AQ502, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A50chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ50chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA50um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ50um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')
plt.savefig ('im50a.pdf')
plt.show()



plt.figure(80)
plt.subplot(3,2,1)
plt.title('Velocidad en 80 km')
extent = (-74, -72, 6.0,8.0)
plt.imshow(A802, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 80 km')
plt.imshow(AQ802, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A80chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ80chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA80um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ80um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')
plt.savefig ('im80a.pdf')
plt.show()



plt.figure(100)
plt.subplot(3,2,1)
plt.title('Velocidad en 100 km')
extent = (-74, -72, 6.0,8.0)
plt.imshow(A1002, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 100 km')
plt.imshow(AQ1002, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A100chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ100chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA100um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ100um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')
plt.savefig ('im100a.pdf')
plt.show()


plt.figure(130)
plt.subplot(3,2,1)
plt.title('Velocidad en 130 km')
extent = (-74, -72, 6.0,8.0)

plt.imshow(A1302, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 130 km')
plt.imshow(AQ1302, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A130chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ130chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA130um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ130um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')
plt.savefig ('im130a.pdf')
plt.show()



plt.figure(150)
plt.subplot(3,2,1)
plt.title('Velocidad en 150 km')
extent = (-74, -72, 6.0,8.0)
plt.imshow(A1502, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,2)
plt.title('Factor Q 150 km')
plt.imshow(AQ1502, cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,3)
plt.imshow(A150chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')

plt.colorbar()
plt.axis('on')

plt.subplot(3,2,4)
plt.imshow(AQ150chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
txt = plt.text(-72.7,7.34,'P', size=11, color='red')
txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
txt = plt.text(-73.712,7.107,'B', size=11, color='red')
txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
plt.colorbar()
plt.axis('on')

plt.subplot(3,2,5)
plt.ion()
plt.imshow(tabA150um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')

plt.subplot(3,2,6)
plt.ion()
plt.imshow(tabAQ150um,cmap='gray', interpolation='none')
plt.colorbar()
plt.axis('off')
plt.savefig ('im150a.pdf')
plt.show()






#
#
#
#plt.figure(70)
#plt.subplot(3,2,1)
#plt.title('Velocidad en 70 km')
#extent = (-74, -72, 6,7.5)
#plt.imshow(A70[70:85,62:80], cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,2)
#plt.title('Factor Q 70 km')
#plt.imshow(AQ70[70:85,62:80], cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,3)
#plt.imshow(A70chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,4)
#plt.imshow(AQ70chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,5)
#plt.ion()
#plt.imshow(tabA70,cmap='gray', interpolation='none')
#plt.colorbar()
#plt.axis('off')
#
#plt.subplot(3,2,6)
#plt.ion()
#plt.imshow(tabAQ70,cmap='gray', interpolation='none')
#plt.colorbar()
#plt.axis('off')
#plt.savefig ('im70a.pdf')
#plt.show()
#
#
#
#plt.figure(100)
#plt.subplot(3,2,1)
#plt.title('Velocidad 100 km')
#extent = (-74, -72, 6, 8)
#
#plt.imshow(A100[70:85,62:80], cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,2)
#plt.title('Factor Q 100 km')
#plt.imshow(AQ100[70:85,62:80], cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
#
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,3)
#plt.imshow(A100chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,4)
#plt.imshow(AQ100chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,5)
#plt.ion()
#plt.imshow(tabA100um,cmap='gray', interpolation='none')
#plt.colorbar()
#plt.axis('off')
#
#plt.subplot(3,2,6)
#plt.ion()
#plt.imshow(tabAQ100um,cmap='gray', interpolation='none')
#plt.colorbar()
#plt.axis('off')
#
##plt.subplot(4,2,7)
##plt.ion()
##plt.imshow(tabA100um,cmap='gray', interpolation='none')
##plt.colorbar()
##plt.axis('off')
##
##plt.subplot(4,2,8)
##plt.ion()
##plt.imshow(tabAQ100um,cmap='gray', interpolation='none')
##plt.colorbar()
##plt.axis('off')
#
#
#plt.savefig ('im100a.pdf')
#plt.show()
#
#plt.figure(150)
#plt.subplot(3,2,1)
#plt.title('Velocidad 150 km')
#extent = (-74, -72, 6, 8)
#plt.imshow(A150[70:85,62:80], cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,2)
#plt.title('Factor Q 150 km')
#plt.imshow(AQ150[70:85,62:80], cmap = cm.gist_earth, origin='upper', extent=extent) #interpolation = 'nearest ')
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,3)
#plt.imshow(A150chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,4)
#plt.imshow(AQ150chec,cmap = cm.gist_earth,  origin='upper', extent=extent)
#txt = plt.text(-72.7,7.34,'P', size=11, color='red')
#txt = plt.text(-73.184,6.59,'B2', size=11, color='red')
#txt = plt.text(-73.712,7.107,'B', size=11, color='red')
#txt = plt.text(-73.1935,7.0788,'O', size=11, color='red')
#
#plt.colorbar()
#plt.axis('on')
#
#plt.subplot(3,2,5)
#plt.ion()
#plt.imshow(tabA150um,cmap='gray', interpolation='none')
#plt.colorbar()
#plt.axis('off')
#
#plt.subplot(3,2,6)
#plt.ion()
#plt.imshow(tabAQ150um,cmap='gray', interpolation='none')
#plt.colorbar()
#plt.axis('off')
#
#
#plt.savefig ('im150a.pdf')
#plt.show()

#A50[70:85,62:80]

            
        
