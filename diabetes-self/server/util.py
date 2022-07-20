import json, pickle
from msilib import add_stream
import base64
import numpy as np
# random_array = np.random.randn(32,32)
# string_repr = base64.binascii.b2a_base64(random_array).decode("ascii")
# array = np.frombuffer(base64.binascii.a2b_base64(string_repr.encode("ascii"))) 
# array = array.reshape(32,32)

import binascii


__model =None


def get_diabetes(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age):
                                               #  return(__data_columns)

    x = (np.zeros(len(__data_columns)))
    # print(x)
    x[0] = pregnancies
    # print(x[0])
    x[1] = glucose
    # print(x[1])

    x[2] = bloodpressure
    # print(x[2])
    x[3] = skinthickness
    # print(x[3])
    x[4] = insulin
    # print(x[4])
    x[5] = bmi
    # print(x[5])
    x[6] = diabetespedigreefunction
    # print(x[6])
    x[7] =age
    # print(x)
    s=__model.predict([x])
    
    a_str = s.__str__()
    
    # print(a_str)
    if a_str=="[0]":
        return(
            "Not Diabetic" )
    elif a_str=="[1]":
        return( "Diabetic") 
     




def get_data_columns():
    return __data_columns


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns



    with open("C:\\Users\\Zain\\Desktop\\diabetes-self\\server\\artifacts\\features_diabetes2.json", "r") as f:
       __data_columns = json.load(f)['data_columns']




    global __model
        
    with open("C:\\Users\\Zain\\Desktop\\diabetes-self\\server\\artifacts\\Diabetes-LogReg82.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")





if __name__ == '__main__':
  load_saved_artifacts()
#   print(get_diabetes(6,65,70,21,112,50.1,1.1,81))
#   print(get_data_columns())

