

def handle_str_table(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j] = int(ls[i][j])
    return ls

def cal_frac(ls) -> None:
    if len(ls) == 0:
        return None
    cnt = 0
    loss_point = 0
    dam_point = False
    len_ls = len(ls)
    for i in ls:
        if i == 100:
            continue
        if i != 100:
            cnt += 1
        if i < 90 and i > 80:
            loss_point += 1
            continue
        if i < 80:
            dam_point = True
            continue
    frac = cnt/len_ls
    if loss_point >= 2:
        frac += 0.1
    if frac >= 0 and frac <= 0.15 and dam_point == False:
        frac_res_good()
    if frac > 0.15 and frac <= 0.25 and dam_point == False:
        frac_res_average()
    elif frac > 0.25 or dam_point:
        frac_res_worse()
    return None
# quote machine lerning --》 to introduce

def cal_class(ls):
    if len(ls) == 0:
        return None
    cls_pool = [0,0,0]
    cl_mb = 0
    cl_cpu_fan = 0
    cl_fan_port = 0
    for i in range(1,len(ls)):
        for idx,j in enumerate(ls[i]):
            if idx == 0:
                cl_mb += int(j)
            if idx == 1:
                cl_cpu_fan += int(j)
            if idx == 2:
                cl_fan_port += int(j)
    # comment on the res
    cls_pool[0]=cl_mb
    cls_pool[1]=cl_cpu_fan
    cls_pool[2]=cl_fan_port
    tmp_max = cls_pool.index(max(cls_pool))
    tmp_min = cls_pool.index(min(cls_pool))
    # return tmp_max,tmp_min
    class_res_best(tmp_min)
    class_res_worse(tmp_max)

def pre_for_frac():
    pass

def pre_for_class():
    pass

def frac_res_good():
    # text to be shown upper side
    widgets.textBrowser_report.setText("Generally Good.\n\
        Almost No deviation.\n\
        Keep going.\n\
        Predictions are given.")

def frac_res_average():
    # text to be shown upper side
    widgets.textBrowser_report.setText("Generally Not bad.\n\
        deviations should be taken care of.\n\
        Seek the most infective error on the table below\n\
        ")

def frac_res_worse():
    # text to be shown upper side
    widgets.textBrowser_report.setText("<strong>Generally Bad!</strong>\n\
        deviations is unacceptable.\n\
        Seek the most infective error on the table below.\n")

def class_res_best(tmp_min):
    l = ["MB", "CPU Fan", "Fan Port"]
    widgets.def_total_text.append("You are best at " + l[tmp_min])

def class_res_worse(tmp_max):
    l = ["MB", "CPU Fan", "Fan Port"]
    widgets.def_total_text.append("You are worst at " + l[tmp_max])

def general_res_adv():
    # use ml to predicate frac and class res and give a general advice
    pass




# def cal_frac(ls) -> None:
#     if len(ls) == 0:
#         return None
#     cnt = 0
#     loss_point = 0
#     dam_point = False
#     len_ls = len(ls)
#     for i in ls:
#         if i ==100:
#             continue
#         if i != 100:
#             cnt += 1
#         if i < 90 and i > 80:
#             loss_point += 1
#             continue
#         if i < 80:
#             dam_point =True
#             continue
#     frac = cnt/len_ls
#     if loss_point >=2:
#         frac += 0.1
#     if frac >=0 and frac <=0.15 and dam_point == False:
#         print("You are so good at this!")
#         frac_res_good()
#     if frac >0.15 and frac <=0.25 and dam_point == False:
#         frac_res_average()
#     elif frac >0.25 or dam_point:
#         frac_res_worse()
#     return None
# # quote machine lerning --》 to introduce

# def cal_class(ls):
#     pass


# def pre_for_frac():
#     pass

# def pre_for_class():
#     pass

# def frac_res_good():
#     # text to be shown upper side
#     widgets.textBrowser_report.append("You are so good at this!")

# def frac_res_average():
#     # text to be shown upper side
#     pass

# def frac_res_worse():
#     # text to be shown upper side
#     pass

# def class_res_good():
#     pass

# def class_res_average():
#     pass

# def class_res_worse():
#     pass

# def general_res_adv():
#     # use ml to predicate frac and class res and give a general advice
#     pass

# # cal_frac([100.0, 100.0, 100.0])
# def cal_class(ls):
#     if len(ls) == 0:
#         return None
#     cls_pool = [0,0,0]
#     cl_mb = 0
#     cl_cpu_fan = 0
#     cl_fan_port = 0
#     for i in range(1,len(ls)):
#         for idx,j in enumerate(ls[i]):
#             if idx == 0:
#                 cl_mb += int(j)
#             if idx == 1:
#                 cl_cpu_fan += int(j)
#             if idx == 2:
#                 cl_fan_port += int(j)
#     # comment on the res
#     cls_pool[0]=cl_mb
#     cls_pool[1]=cl_cpu_fan
#     cls_pool[2]=cl_fan_port
#     tmp_max = cls_pool.index(max(cls_pool))
#     tmp_min = cls_pool.index(min(cls_pool))
#     print(cls_pool)
#     return tmp_max,tmp_min

# print(cal_class([('0', '0', '0'), ('2', '8', '0'), ('10', '28', '1')]
# ))