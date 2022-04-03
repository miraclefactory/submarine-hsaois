import pstats


all_class =['CPU_FAN_NO_Screws', 'CPU_FAN_Screw_loose', 'CPU_FAN_Screws', 'CPU_fan', 'CPU_fan_port', 'CPU_fan_port_detached', 'Incorrect_Screws', 'Loose_Screws', 'No_Screws', 'Scratch', 'Screws']

def decode_num_input(ls)->list:
    for i in range(len(ls)):
        if i == 0:
            ls[i] = 'CPU_FAN_NO_Screws'
        elif i == 1:
            ls[i] = 'CPU_FAN_Screw_loose'
        elif i == 2:
            ls[i] = 'CPU_FAN_Screws'
        elif i == 3:
            ls[i] = 'CPU_fan'
        elif i == 4:
            ls[i] = 'CPU_fan_port'
        elif i == 5:
            ls[i] = 'CPU_fan_port_detached'
        elif i == 6:
            ls[i] = 'Incorrect_Screws' 
        elif i == 7:
            ls[i] = 'Loose_Screws'
        elif i == 8:
            ls[i] = 'No_Screws'
        elif i == 9:
            ls[i] = 'Scratch'
        elif i == 10:
            ls[i] = 'Screws'
        return ls

def set_style_sheet_for_correct(self, widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #00ff00;
        }
    """)
    pass
def set_style_sheet_for_incorrect(self, widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #ff0000;
        }
    """)
    pass