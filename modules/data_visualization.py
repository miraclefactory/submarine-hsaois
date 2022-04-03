from main import *
from shit_algorithm import *
import cv2

from utils.general import clean_str


# all_class = ['CPU_FAN_NO_Screws', 'CPU_FAN_Screw_loose', 'CPU_FAN_Screws', 'CPU_fan', 'CPU_fan_port', 'CPU_fan_port_detached', 'Loose_Screws', 'No_Screws', 'Screws']

all_class =['CPU_FAN_NO_Screws', 'CPU_FAN_Screw_loose', 'CPU_FAN_Screws', 'CPU_fan', 'CPU_fan_port', 'CPU_fan_port_detached', 'Incorrect_Screws', 'Loose_Screws', 'No_Screws', 'Scratch', 'Screws']

def data_vis(self,
             hashpool,
             input_list,
             is_new_img,
             cnt,
             is_defetced,
             seq,
             class_list,
             cvimg):
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
                                    cv2.imwrite(f"../defected/defected{seq}.jpg", cvimg)
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
    ret = False
    for i in list:
        if i in [0,1,3,5,6,7,8,9]:
            ret = True
            self.es.text_print.emit(f'Defected Class: {i}')
    self.es.text_print.emit("\n" + f"Result of subject {seq}: " + str(list) + "\n")
    return ret

def update_line_graph(y_axis, ls, class_total, seq=None):
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
    # if (class_total[6] + class_total[7] + class_total[8]) != 0:
    #     y_axis[0] = (class_total[7] / (class_total[6] + class_total[7] + class_total[8])) * 100
    #     y_axis[1] = (class_total[6] / (class_total[6] + class_total[7] + class_total[8])) * 100
    # if (class_total[0] + class_total[1] + class_total[2]) != 0:
    #     y_axis[2] = (class_total[0] / (class_total[0] + class_total[1] + class_total[2])) * 100
    #     y_axis[3] = (class_total[1] / (class_total[0] + class_total[1] + class_total[2])) * 100
    # if class_total[4] != 0 and seq != 1:
    #     y_axis[4] = (((seq - 1) - class_total[4]) / (seq - 1)) * 100
    # mb : mbs,mbns,mbls,mbws
    # cpu: cpfn,cpls
    # cpu port: cpfp,cpfd
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

# def update_line_graph_batch(y_axis_batch,ls):
#     len_ls = len(ls)

