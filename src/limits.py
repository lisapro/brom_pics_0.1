'''
Created on 8. jul. 2016

@author: ELP
'''
#depth limits for Water,BBL, and Sediment
y1min = 0
y1max = 109
y2min = 109
y2max = 110 #(sed_wat interface)
y3min = -10 #109.91
y3max = 10 #110.10
ysedmin = -8 #for depth in cm
ysedmax = 10

#limits for x at Water and BBL axes:
kzmin = 1.e-7
kzmax = 1.e-0
salmin = 34.6
salmax = 35.2
tempmin = 6
tempmax =9
so4min = 10000
so4max = 30000
h2smax = 3
s0max = 3
s2o3max = 12 
o2max = 500
nh4max = 10
no2max = 2
no3max = 100
mnco3max = 1
mnsmax = 0.5
mn4max = 1
mn3max = 0.5
mn2max = 1
phymax = 2
hetmax = 10
baaemax = 1
bhaemax = 2
bhanmax = 1
baanmax = 2
nh4max = 50
ponmax = 80
donmax = 20
po4max = 20
fes2max = 5
fesmax = 5
fe3max = 5
fe2max = 5
ch4max = 1
dicmin = 1000
dicmax = 6000
alkmin = 2200
alkmax = 2800
simax = 500
si_partmax = 400
ch4max = 0.5
phmin = 5
phmax = 9
pco2max = 8000
om_camax = 10
om_armax = 10
co3max = 10
camax = 10
#limits for x Sediment axes:
sed_kzmin = 0#1.e-11
sed_kzmax = 1.e-5
sed_tempmin = 7.3
sed_tempmax = 8.3
sed_salmin = 34.6
sed_salmax = 35.2
sed_so4min = 10000
sed_so4max = 30000
sed_h2smax = 1200
sed_s0max = 200
sed_s2o3max = 160
sed_o2max = 200
sed_nh4max = 1500
sed_no2max = 10
sed_no3max = 50
sed_mnco3max = 10
sed_mnsmax = 10
sed_mn4max = 100
sed_mn3max = 10
sed_mn2max = 12
sed_phymax = 10
sed_hetmax = 20
sed_baaemax = 10
sed_bhaemax = 1000
sed_bhanmax = 4500
sed_baanmax = 500
sed_ponmax = 50000
sed_donmax = 250
sed_po4max = 200
sed_fes2max = 50
sed_fesmax = 50
sed_fe3max = 500
sed_fe2max = 100
sed_ch4max = 10
sed_dicmin = 1100
sed_dicmax = 15000
sed_alkmin = 2000
sed_alkmax = 14000
sed_simax = 2600
sed_si_partmax = 75000
sed_ch4max = 0.5
sed_phmin = 5
sed_phmax = 9
sed_pco2max = 25000
sed_om_camax = 10
sed_om_armax = 5
sed_co3max = 10
sed_camax = 10

#positions for different axes, sharing one subplot
axis1 = 0
axis2 = 27
axis3 = 53
axis4 = 79
axis5 = 105

labelaxis_x =  1.10 #positions of labels 
labelaxis1_y = 1.02
labelaxis2_y = 1.15
labelaxis3_y = 1.26
labelaxis4_y = 1.38
labelaxis5_y = 1.48