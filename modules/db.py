
import sqlite3
import cv2
from PIL import Image
from io import BytesIO
import base64
from matplotlib import image
import numpy as np


CREAT_TABLE_ERROR_DETAILS = """CREATE TABLE IF NOT EXISTS error_details ( 
    id_error INTEGER PRIMARY KEY AUTOINCREMENT,
    Vector_output TEXT,
    serial_number TEXT
)"""  # to be argument in create_table

# CREART_TOTAL_RECORD = """CREATE TABLE IF NOT EXISTS total_record (
#     Total_num_of_mb INTEGER

# )"""

CREAT_GENERAL_TABLE = """CREATE TABLE IF NOT EXISTS general_table (
    batch_number INTEGER,
    defective TEXT,
    mb TEXT,
    cpu_fan TEXT,
    fan_port TEXT
);

"""

CREAT_CLASS_TABLE = """CREATE TABLE IF NOT EXISTS class_table (
    id_three INTEGER PRIMARY KEY AUTOINCREMENT,
    class_mb INTEGER,
    class_cpu_fan INTEGER,
    class_fan_port INTEGER
)"""


CREAT_ERROR_PIC = """CREATE TABLE IF NOT EXISTS error_pic (
    id_error INTEGER PRIMARY KEY AUTOINCREMENT,
    img BLOB
)"""


def init_table():
    create_table(CREAT_TABLE_ERROR_DETAILS)
    # create_table(CREART_TOTAL_RECORD)
    create_table(CREAT_GENERAL_TABLE)
    create_table(CREAT_CLASS_TABLE)
    create_table(CREAT_ERROR_PIC)


def create_table(table_creator) -> None:
    # init_to_be_done on the cloud side
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute(table_creator)
    conn.commit()
    conn.close()


def init_batch() -> None:
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    # c.execute('''SELECT batch_number FROM general_table
    # ORDER BY batch_number DESC LIMIT 1''')
    # last_batch = c.fetchall()
    c.execute("INSERT INTO general_table VALUES (0,'0',0,0,0)")
    conn.commit()
    conn.close()


def verify_general_table() -> bool:
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute('''SELECT batch_number FROM general_table
    ORDER BY batch_number DESC LIMIT 1''')
    last_batch = c.fetchall()
    conn.close()
    if len(last_batch) == 0:
        return True
    else:
        return False


def update_general_table(batch_number, defective) -> None:  # change after update
    if batch_number != 0:
        # print(batch_number)
        # print(defective)
        # deploy it on the cloud
        conn = sqlite3.connect(
            'hsaois.db')
        c = conn.cursor()
        thp = "SELECT * FROM class_table ORDER BY id_three DESC LIMIT 1"
        c.execute(thp)
        data = c.fetchall()
        if data != []:
            data_to_update = data[0][1], data[0][2], data[0][3]
            a = data_to_update[0]
            b = data_to_update[1]
            cx = data_to_update[2]
            plh = f"INSERT INTO general_table VALUES ({batch_number},'{defective}',{a},{b},{cx})"
        else:
            plh = f"INSERT INTO general_table VALUES ({batch_number},'{defective}',0,0,0)"
        c.execute(plh)
        conn.commit()
        conn.close()
    else:
        return None


def delete_class_table() -> None:
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute("DELETE FROM class_table")
    conn.commit()
    conn.close()


def get_bacth_defective() -> int:
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute('''SELECT batch_number FROM general_table
    ORDER BY batch_number DESC LIMIT 1''')
    last_batch = c.fetchall()
    conn.close()
    return last_batch[len(last_batch)-1][0]


def update_class_table(class_mb, class_cpu_fan, class_fan_port) -> None:
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    s = f"INSERT INTO class_table(class_mb,class_cpu_fan,class_fan_port) VALUES ({class_mb},{class_cpu_fan},{class_fan_port})"
    c.execute(s)
    conn.commit()
    conn.close()


def fecth_defective_data() -> list:
    data_fecthed = []
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute("SELECT defective FROM general_table ")
    data = c.fetchall()
    # ['0.0', '0.0%', '100.0%', '100.0%', '0.0%']
    data_fecthed = [str(i[0]) for i in data]
    conn.close()
    return data_fecthed[1:]


def update_error_details(Vector_output, serial_number) -> None:
    # deploy it on the cloud
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    s = f"INSERT INTO error_details(Vector_output,serial_number) VALUES ('{Vector_output}','{serial_number}')"
    c.execute(s)
    conn.commit()
    conn.close()


def fetch_last_batch_num() -> int:
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute(
        "SELECT batch_number FROM general_table ORDER BY batch_number DESC LIMIT 1")
    data = c.fetchall()
    conn.close()
    return data[0][0]


def update_error_pic(img):
    img_x = cv2.imread(img)
    img_blob = sqlite3.Binary(img_x)
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    s = f"INSERT INTO error_pic(img) VALUES ('{img_blob}')"
    # print(s)
    c.execute(s)
    conn.commit()
    conn.close()

# def update_error_pic(img): #currently as img_blob
#     conn = sqlite3.connect('/Users/mac/Downloads/sub_GUI/modules/hsaois.db')
#     c = conn.cursor()
#     with open(img, 'rb') as f:
#         img_byte = f.read()
#         content = base64.b64encode(img_byte)
#         print(type(content))
#     s = f"INSERT INTO error_pic(img) VALUES ({content})"
#     c.execute(s)
#     conn.commit()
#     conn.close()


def retrieve_pic():  # need to be change after cloud deployment
    image = []
    conn = sqlite3.connect('hsapis.db')
    c = conn.cursor()
    c.execute("SELECT img FROM error_pic")
    data = c.fetchall()
    for i in data:
        image.append(np.array(i[0]))
    # cv2.imwrite('/Users/mac/Downloads/sub_GUI/modules/img.jpg', image[0])
    # print(image)
    # print(data)
    conn.close()
    return data


def fetch_general_class():
    conn = sqlite3.connect('hsaois.db')
    c = conn.cursor()
    c.execute(
        "SELECT mb,cpu_fan,fan_port FROM general_table order by batch_number ")
    data = c.fetchall()
    conn.close()
    return data

def fetch_batch_num():
    conn = sqlite3.connect("hsaois.db")
    c = conn.cursor()
    c.execute("SELECT batch_number FROM general_table")
    data = c.fetchall()
    data = [i[0] for i in data]
    return data[1:]

# print(fecth_defective_data())
# fetch_batch_num()

def fetch_frac_limited(lim_num):
    num = int(lim_num)+1
    conn = sqlite3.connect("hsaois.db")
    c = conn.cursor()
    s = f"SELECT defective FROM general_table ORDER BY batch_number LIMIT {num}"
    c.execute(s)
    data = c.fetchall()
    data = [i[0] for i in data]
    return data[1:]

def fetch_general_class_limited(lim_num):
    num = int(lim_num)
    conn = sqlite3.connect("hsaois.db")
    c = conn.cursor()
    s = f"SELECT mb,cpu_fan,fan_port FROM general_table ORDER BY batch_number LIMIT {num+1}"
    c.execute(s)
    data = c.fetchall()
    conn.close()
    return data

def fetch_limited_batch_num(lim_num):
    num = int(lim_num)+1
    # 异常处理
    conn = sqlite3.connect("hsaois.db")
    c = conn.cursor()
    c.execute("SELECT batch_number FROM general_table order by batch_number limit {num}".format(num=num))
    data = c.fetchall()
    data = [i[0] for i in data]
    return data[1:num]

# print(fetch_limited_batch_num(3))
# print(fetch_batch_num())

# print(fetch_frac_limited(3))
# print(fecth_defective_data())