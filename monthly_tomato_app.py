from flask import Flask, request, render_template
import pickle
import numpy as np

#[0 'April',1 'August',2'December',3 feb ,4 jan ,5'July',6'June',7'March',8'May',9'November',10'October',11'September']
#my_dict = {1: 'apple', 2: 'ball'}  print(my_dict['age'])
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('monthly_tomato_home.html')

@app.route('/price',methods=['POST','GET'])
def get_price():
    mp =0
    Mp =0
    if request.method=='POST':
        result=request.form
        area = int(result['area'])
        tonnes = result['tonnes']
        month = result['month']
        if (area == 0):
            Mp = 1375
            mp = 1375
        elif (area == 1):
            Mp = 1191.507048
            mp = 580.8535726
        elif (area == 2):
            Mp =1563.848987 
            mp =344.6171062
        elif (area == 3):
            Mp =895.8333333 
            mp =795.8333333
        elif (area == 4):
            Mp =1919.230989 
            mp =1483.486015
        elif (area == 5):
            Mp =1744.998376 
            mp =1156.993664
        elif (area == 6):
            Mp =230.4630952 
            mp =218.2285714
        elif (area ==7 ):
            Mp =1998.423029 
            mp =435.0582387
        elif (area == 8):
            Mp =1737.052471
            mp = 1385.101972
        elif (area == 9):
            Mp =1905.910617 
            mp =715.544136
        elif (area == 10):
            Mp =1134.860569 
            mp =921.8600394
        elif (area == 11):
            Mp =1594.126513 
            mp =1142.041874
        elif (area == 12):
            Mp =1070.641685 
            mp =793.7680376
        elif (area == 13):
            Mp =926.8477237 
            mp =757.9387222
        elif (area == 14):
            Mp =1447.04339 
            mp = 1047.781889
        elif (area ==15 ):
            Mp =1000
            mp =1000
        elif (area ==16 ):
            Mp =1000
            mp =1000
        elif (area == 17):
            Mp =1282.650171 
            mp =1043.494398
        elif (area == 18):
            Mp =1472.222222 
            mp =1311.111111
        elif (area == 19):
            Mp =941.684859  
            mp =529.6421957
        elif (area == 20):
            Mp =750
            mp =750
        elif (area == 21):
            Mp =328.3333333 
            mp =328.3333333
        elif (area == 22):
            Mp =1026.646644 
            mp =979.1120476
        elif (area ==23 ):
            Mp =1325.833333
            mp = 916.6666666
        elif (area == 24):
            Mp =1988.276068 
            mp =469.4386319
        elif (area == 25):
            Mp =1000    
            mp =800
        elif (area ==26 ):
            Mp =4500
            mp =3900
        elif (area ==27 ):
            Mp =400
            mp =400
        elif (area == 28):
            Mp =1824.247657 
            mp =610.7069904
        elif (area == 29):
            Mp =1810.834088 
            mp =526.9959191
        elif (area ==30 ):
            Mp =1703.3766   
            mp =1379.153607
        elif (area == 31):
            Mp =619.5491415 
            mp =545.7367361
        elif (area == 32):
            Mp =1759.482255 
            mp =1421.193658
        elif (area == 33):
            Mp =1163.336289 
            mp =962.5298378
        elif (area == 34):
            Mp =1250
            mp =1250
        elif (area == 35):
            Mp =1751.992111 
            mp =500.7272558
        elif (area ==36 ):
            Mp =1909.583333 
            mp =1826.25
        elif (area ==37 ):
            Mp =750
            mp =750
        elif (area ==38 ):
            Mp =900
            mp =450
        elif (area == 39):
            Mp =1810.361953 
            mp =1553.000842


        months = {0: 'April',1: 'August',2:'December',3: 'February' ,4: 'January' ,5: 'July',6: 'June',7: 'March',8: 'May',9: 'November',10: 'October',11:'September'}

        areas = {0:'Arasikere', 1:'Bagepalli', 2:'Bangarpet', 3:'Belur',
         4:'Binny Mill (F&V), Bangalore', 5:'Channapatana', 6:'Channarayapatna',
         7:'Chickkaballapura', 8:'Chikkamagalore', 9:'Chintamani', 10:'Davangere',
        11:'Doddaballa Pur', 12:'Gowribidanoor', 13:'Gundlupet', 14:'Hassan',
        15:'Holalkere', 16:'Holenarsipura',17: 'Honnali', 18:'Hoskote',19: 'Hospet',
        20:'Hunsur', 21:'K.R. Pet',22:'K.R.Nagar', 23:'Kanakapura', 24:'Kolar',
        25:'Kollegal', 26:'Kudchi', 27:'Maddur', 28:'Malur', 29:'Mulabagilu',
        30:'Mysore (Bandipalya)', 31:'Nagamangala', 32:'Ramanagara', 33:'Shimoga',
        34:'Somvarpet', 35:'Srinivasapur', 36:'T. Narasipura', 37:'Tarikere',38: 'Tumkur',
        39:'Udupi'}



        mon = months[int(month)]
        market = areas[int(area)]
        ton = tonnes
        pkl_file = open('monthly_gbr_model3.pkl', 'rb')
        logmodel = pickle.load(pkl_file)

        array = np.array([int(month),int(area),float(tonnes),float(Mp),float(mp)])
        new_array = array.reshape(1,-1)
        prediction2 = logmodel.predict(new_array)
    
        return render_template('tomato_result.html', prediction=prediction2, mon=mon, market=market, ton=ton)
        
        #return render_template('tomato_result.html',prediction=prediction2)

    
if __name__ == '__main__':
    app.debug = True
    app.run()


