import json, pickle

import numpy as np

__model =None

def get_crop_name(n, p, k, temperature, humidity, ph, rainfall):
                                               #  return(__data_columns)

    x = np.zeros(len(__data_columns))
    # print(x)
    x[0] = n
    # print(x[0])
    x[1] = p
    # print(x[1])

    x[2] = k
    # print(x[2])
    x[3] = temperature
    # print(x[3])
    x[4] = humidity
    # print(x[4])
    x[5] = ph
    # print(x[5])
    x[6] = rainfall
    # print(x[6])
    # x=x.tolist()
    # print(x)
      
    return type(__model.predict([x])[0])


 

def get_data_columns():
    return __data_columns
    


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    # global __n
    # global __p
    # global __k
    # global __temperature
    # global __humidity
    # global __ph
    # global __rainfall


    with open("C:\\Users\\Zain\\Desktop\\Crop\\server\\artifacts\\features.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # __n = __data_columns[0]
        # __p = __data_columns[1] 
        # __k = __data_columns[2] 
        # __temperature=__data_columns[3] 
        # __humidity=__data_columns[4]
        # __ph=__data_columns[5] 
        # __rainfall=__data_columns[6] 
    

    global __model
    
    with open("C:\\Users\\Zain\\Desktop\\Crop\\server\\artifacts\\Crop-RF.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
  load_saved_artifacts()
#   print(get_data_columns())
#   print(get_crop_name(104,18, 30, 23.603016, 60.3, 6.7, 140.91))
  print(get_crop_name(83, 45, 60, 28, 70.3, 7.0, 150.9))
