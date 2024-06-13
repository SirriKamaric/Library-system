import datetime
from idlelib import window
from urllib import request

import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from xlrd import *

ui,_ = loadUiType('library.ui')

login,_ = loadUiType('login.ui')


class Flask:
    pass


app = Flask(__name__)

# Access Control
def jsonify(param):
    pass


@app.before_request
def check_api_key():
    api_key = request.headers.get('X-API-Key')
    if api_key != '12345':
        return jsonify({'message': 'Invalid API key'}), 401

# Main App Endpoints
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the library management system'}), 200

# Additional endpoints for your main app can be added here
class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.Dark_Orange_Theme()

        self.Show_Author()
        self.Show_Category()
        self.Show_Publisher()


        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()

        self.Show_All_Clients()
        self.Show_All_Books()

        self.Show_All_Operations()


    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)


    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_17.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_26.clicked.connect(self.Open_CLients_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_9.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_10.clicked.connect(self.Delete_Books)

        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_12.clicked.connect(self.Login)
        self.pushButton_13.clicked.connect(self.Edit_User)

        self.pushButton_19.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_21.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_20.clicked.connect(self.QDark_Theme)

        self.pushButton_22.clicked.connect(self.Add_New_Client)
        self.pushButton_24.clicked.connect(self.Search_Client)
        self.pushButton_23.clicked.connect(self.Edit_Client)
        self.pushButton_25.clicked.connect(self.Delete_Client)

        self.pushButton_6.clicked.connect(self.Handel_Day_Operations)

        self.pushButton_29.clicked.connect(self.Export_Day_Operations)
        self.pushButton_27.clicked.connect(self.Export_Books)
        self.pushButton_28.clicked.connect(self.Export_Clients)



    def Show_Themes(self):
        self.groupBox_3.show()


    def Hiding_Themes(self):
        self.groupBox_3.hide()

    ########################################
    ######### opening tabs #################
    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_CLients_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(4)


    ########################################
    ######### Day Operations #################
    def Handel_Day_Operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_29.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        print(today_date)
        print(to_date)

        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO dayoperations(book_name, client, type , days , date , to_date )
            VALUES (%s , %s , %s, %s , %s , %s)
        ''' , (book_title ,client_name, type , days_number , today_date  , to_date))

        self.db.commit()
        self.statusBar().showMessage('New Operation Added')

        self.Show_All_Operations()



    def Show_All_Operations(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

    def Show_All_Books(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(
            ''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()

    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s , %s , %s , %s , %s , %s , %s)
        ''', (book_title, book_description, book_code, book_category, book_author, book_publisher, book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')
        self.Show_All_Books()
 def Add_Author(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='toor' , db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()
        self.cur.execute('''
            INSERT INTO authors (author_name) VALUES (%s)
        ''' , (author_name,))
        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage('New Author Addedd ')
        self.Show_Author()
        self.Show_Author_Combobox()


    def Show_Author(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Publisher(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='toor' , db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()
        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''' , (publisher_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage('New Publisher Addedd ')
        self.Show_Publisher()
        self.Show_Publisher_Combobox()


    def Show_Publisher(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

def main():
    app = QApplication(sys.argv)

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
    app.run(debug=True)

