from PySide2.QtWidgets import *
from PySide2.QtCore import *
from mainUI import Ui_MainWindow
import mysql.connector

DB_IP = 'aws server ip'
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.db = mysql.connector.connect(host=DB_IP, user='mysql user name', password='mysql pw', database='DB name', auth_plugin='mysql_native_password')
        self.cur = self.db.cursor()

        # timer
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.pollingQuery)
        print("INIT")
        self.statusBar().showMessage('Ready')
    def start(self):
        self.timer.start()
        print("START")

    def stop(self):
        self.insertCommand("stop", "0")
        self.showStatusBar('stop')

    def go(self):
        self.insertCommand("go", "0")
        self.showStatusBar('forward')

    def left(self):
        self.insertCommand("left", "0")
        self.showStatusBar('left')

    def mid(self):
        self.insertCommand("mid", "0")
        self.showStatusBar('forward')

    def right(self):
        self.insertCommand("right", "0")
        self.showStatusBar('right')

    def back(self):
        self.insertCommand("back", "0")
        self.showStatusBar('backward')

    def pollingQuery(self):
        self.cur.execute("select * from command order by time desc limit 15")
        self.ui.logText.clear()
        for (id, time, cmd_string, arg_string, is_finish) in self.cur:
            string = "%d | %s | %6s | %6s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), cmd_string, arg_string, is_finish)
            self.ui.logText.appendPlainText(string)

        self.cur.execute("select * from sensing order by time desc limit 15")
        self.ui.sensingText.clear()
        for (id, time, num1, num2, num3, meta_string, is_finish) in self.cur:
            string = "%d | %s | %6s | %6s | %6s | %10s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), num1, num2, num3, meta_string, is_finish)
            self.ui.sensingText.appendPlainText(string)

        self.cur.execute("select time, num1, num2, meta_string from sensing order by time desc limit 1")
        for(time,num1, num2, meta_string) in self.cur:
            parse_string = meta_string.split('|')
            danger_flag = int(parse_string[3])
            print(time, meta_string, danger_flag)
            temp = round(float(num1) * 100, 2)
            string = "temperature: " + str(temp) + " C"
            self.ui.temp_label.setText(string)
            humi = round(float(num2) * 100, 2)
            string = "humidity: " + str(humi)+ " %"
            self.ui.humi_label.setText(string)
            if(danger_flag==1):
                self.showStatusBar('danger')
                self.stop()
            elif(danger_flag==2):
                self.showStatusBar('warning')
                self.stop()
            else:
                self.showStatusBar('safe')

        self.db.commit()
    def insertCommand(self, cmd_string, arg_string):
        time = QDateTime().currentDateTime().toPython()
        is_finish = 0

        query = "insert into command(time, cmd_string, arg_string, is_finish) values (%s, %s, %s, %s)"
        value = (time, cmd_string, arg_string, is_finish)

        self.cur.execute(query, value)
        self.db.commit()

    def showStatusBar(self, status):
        global status_cur, direction_cur
        if(status == "danger"):
            self.statusBar().showMessage("DANGER!!!!")
            self.statusBar().setStyleSheet("color: red")
            self.ui.status_text.setText("DANGER!!")
            self.ui.status_text.setStyleSheet("color : red")
        elif(status == "warning"):
            self.statusBar().showMessage("WARNING!!!!")
            self.statusBar().setStyleSheet("color: orange")
            self.ui.status_text.setText("WARNING!!")
            self.ui.status_text.setStyleSheet("color : orange")

        elif(status == "left"):
            self.statusBar().showMessage("LEFT")
            self.statusBar().setStyleSheet("color: blue")
            status_cur = status
            self.ui.direction_text.setText("LEFT")
            self.ui.direction_text.setStyleSheet("color : blue")

        elif(status == "right"):
            self.statusBar().showMessage("RIGHT")
            self.statusBar().setStyleSheet("color: blue")
            status_cur = status
            self.ui.direction_text.setText("RIGHT")
            self.ui.direction_text.setStyleSheet("color : blue")

        elif(status == "forward"):
            self.statusBar().showMessage("FORWARD")
            self.statusBar().setStyleSheet("color: green")
            status_cur = status
            self.ui.direction_text.setText("FORWARD")
            self.ui.direction_text.setStyleSheet("color : green")

        elif(status == "backward"):
            self.statusBar().showMessage("BACKWARD")
            self.statusBar().setStyleSheet("color: green")
            status_cur = status
            self.ui.direction_text.setText("BACKWARD")
            self.ui.direction_text.setStyleSheet("color : green")

        elif(status == "safe"):
            self.statusBar().showMessage("SAFE")
            self.statusBar().setStyleSheet("color: green")
            self.ui.status_text.setText("SAFE")
            self.ui.status_text.setStyleSheet("color : green")
        elif(status == "stop"):
            self.statusBar().showMessage("STOP")
            self.statusBar().setStyleSheet("color: black")
            self.ui.direction_text.setText("STOP")
            self.ui.direction_text.setStyleSheet("color : black")

    def clsoeEvent(self, event):
        print("CLOSE")
        self.cur.close()
        self.db.close()

app = QApplication()
win = MyApp()
win.show()
app.exec_()
