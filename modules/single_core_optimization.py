# ///////////////////////////////////////////////////////////////

# This module is used to optimize the performance of single core CPU
# BY: Miracle Factory

# ///////////////////////////////////////////////////////////////

from main import widgets, selectedFile, window, detect, lock
from cv2 import getTickCount, getTickFrequency
from threading import Thread
from PySide6.QtWidgets import QMessageBox
import sys


class SingleCore():

    def singleCoreFileDetectMode(self):
        status_code = 0
        mission = [[]*10 for i in range(10)]
        widgets.btn_start_file.setEnabled(False)
        if len(selectedFile) == 0:
            QMessageBox.warning(None, "Warning", "Please select a file first!", QMessageBox.Ok)
            return
        else:
            # NEW THREAD FOR FILE DETECT
            for i,j in enumerate(selectedFile):
                idx  = i % 10
                mission[idx].append(j)
            e1 = getTickCount()  # START TIME
            for i in range(10):
                thread = Thread(target=self.singleCoreDetectThread,args=(mission[i],))
                thread.start()
            e2 = getTickCount()  # END TIME
            time = (e2 - e1) / getTickFrequency()
            widgets.textBrowser.append("Detect Mode: " + 
                "Process Finished in " + str(round(time, 3)) + 
                "s, " + "results saved to 'modules/runs/detect'.")
            if status_code == 0:
                window.es.message_box.emit("Success", 
                                    "Success:\n\nProcess Finished in " + str(round(time, 3)) + "s.")
            else:
                window.es.message_box.emit("Warning", 
                                        "Warning:\n\nAn Error Occurred During Process.\nProcess Finished in "
                                        + str(round(time, 3)) + "s.")
        widgets.btn_start_file.setEnabled(True)

    def singleCoreDetectThread(self, mission):
        lock.acquire()
        for i in mission:
            try:
                sys.argv[1:3] = ["--source", i, "--save-txt"]   # SET ARGUMENTS
                input_class = detect()  # RECEIVE Class
                window.es.message_box.emit("Detect Class Result: " + str(input_class))
            except FileNotFoundError:
                window.es.message_box.emit("Detect Mode Error: " + "File Not Found")
                status_code = 1
            except InterruptedError:
                window.es.message_box.emit("Detect Mode Warning: " + "Session Terminated")
                status_code = 99
            except:
                window.es.message_box.emit("Detect Mode Error: " + "Unknown Error")
                status_code = 2
        lock.release()