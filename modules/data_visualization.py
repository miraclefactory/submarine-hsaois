from main import *
from shit_algorithm import *
import cv2

'''
This is all the class currently included in the model, 
and they are used to indicate the detected types
'''
all_class =['CPU_FAN_NO_Screws', 'CPU_FAN_Screw_loose', 'CPU_FAN_Screws', 'CPU_fan', \
            'CPU_fan_port', 'CPU_fan_port_detached', 'Incorrect_Screws', 'Loose_Screws', \
            'No_Screws', 'Scratch', 'Screws']

def data_vis(self,
             hashpool,
             input_list,
             is_new_img,
             cnt,
             is_defetced,
             seq,
             class_list,
             cvimg):
    '''
    Data visualization algorithm for the model, 
    corresponding to the code fragement in main.py
    '''
    if len(hashpool) > 1:
        for i in range(len(hashpool)):
            if i+1 < len(hashpool):
                hmd = caculateHammingDistance(hashpool[i], hashpool[i+1])
                if hmd == 0:
                    cnt += 1
                    if len(class_list) > 1:
                        input_list.append(class_list)
                    if cnt > 5 and is_new_img:
                        is_new_img = False
                        if is_defetced == False and len(input_list) > 1:
                            is_defetced = True
                            for i in input_list[len(input_list)-1]:
                                if i in [0,1,5,6,7]:
                                    cv2.imwrite(f"../defected/{seq}.jpg", cvimg)
                    hashpool = hashpool[i+1:]
                    break
                if hmd >= 5:
                    is_defetced = False
                    if len(input_list) > 0:
                        seq += 1
                        a = feature_max_pooling([length_weighted_average_pooling(i)\
                                                    for i in segementation(input_list, 4)])
                        for i in a:
                            if i in [0,1,5,6,7]:
                                self.es.text_print.emit(f'Defected, error: {i}\n')
                        self.es.text_print.emit(f"res of {seq} img "+str(list)+"\n")
                    input_list = []
                    is_new_img = True
                    cnt = 0
                    hashpool = hashpool[i+1:]
                    break

def detect_error(self, list, seq):
    '''
    Detect the defeteced classes in the model output, 
    return True if the defeted classes are found
    '''
    self.es.text_print.emit(f"<span>Class of subject {seq}: {str(list)}</span><\n")
    ret = False
    for i in list:
        if i in [0,1,3,5,6,7,8,9]:
            ret = True
            self.es.text_print.emit(f"<span style='color: rgb(170,55,49);'>\
                                    Defect detected: {all_class[i]}</span>\n")
    if ret:
        self.es.text_print.emit(f"<span style='color: rgb(170,55,49); \
                                font-weight: bold;'>• Result: Defected</span><br/>\n")
    else:
        self.es.text_print.emit(f"<span style='color: rgb(68,140,39); \
                                font-weight: bold;'>• Result: Passed</span><br/>\n")
    return ret

def update_line_graph(y_axis, ls, class_total, seq=None):
    '''
    Update the data field used to draw the line graph(y_axis list)
    '''
    # 0 is mb no screw, 1 is mb loose screw, 2 is cpu fan no screw, 
    # 3 is cpu fan loose screw, 4 is cpu fan detached
    # 0 is mb, 1 is cpu fan, 2 is cpu fan port
    for i in ls:
        if i == 0:
            class_total[0] += 1
        elif i == 1:
            class_total[1] += 1
        elif i == 2:
            class_total[2] += 1
        elif i == 3:
            class_total[3] += 1
        elif i == 4:
            class_total[4] += 1
        elif i == 5:
            class_total[5] += 1
        elif i == 6:
            class_total[6] += 1
        elif i == 7:
            class_total[7] += 1
        elif i == 8:
            class_total[8] += 1
        elif i == 9:
            class_total[9] += 1
        elif i == 10:
            class_total[10] += 1
    if(class_total[0] + class_total[1] + class_total[2]) != 0:
        y_axis[2] = (class_total[0] / (class_total[0] + class_total[1] + class_total[2])) * 100
        y_axis[3] = (class_total[1] / (class_total[0] + class_total[1] + class_total[2])) * 100
    if(class_total[4]+class_total[5])!=0:
        y_axis[4] = class_total[5]/(class_total[4]+class_total[5])*100
    if(class_total[6] + class_total[7] + class_total[8]+class_total[9]+class_total[10]) != 0:
        y_axis[1] = (class_total[7] / (class_total[6] + class_total[7] + class_total[8])) * 100
        y_axis[6] = (class_total[6] / (class_total[6] + class_total[7] + class_total[8])) * 100
        y_axis[0] = (class_total[8] / (class_total[6] + class_total[7] + class_total[8])) * 100
        y_axis[5] = (class_total[9] / (class_total[6] + class_total[7] + class_total[8])) * 100
     
    return y_axis
