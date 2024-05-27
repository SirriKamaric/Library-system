import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class CatalogManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Catalog Management")
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_label = QLabel("Title:")
        self.title_input = QLineEdit()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)

        self.author_label = QLabel("Author:")
        self.author_input = QLineEdit()
        self.layout.addWidget(self.author_label)
        self.layout.addWidget(self.author_input)

        self.publisher_label = QLabel("Publisher:")
        self.publisher_input = QLineEdit()
        self.layout.addWidget(self.publisher_label)
        self.layout.addWidget(self.publisher_input)

        self.publication_date_label = QLabel("Publication Date:")
        self.publication_date_input = QLineEdit()
        self.layout.addWidget(self.publication_date_label)
        self.layout.addWidget(self.publication_date_input)

        self.add_button = QPushButton("Add Book")
        self.add_button.clicked.connect(self.add_book)
        self.layout.addWidget(self.add_button)

        self.books_list = QListWidget()
        self.layout.addWidget(self.books_list)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        publisher = self.publisher_input.text()
        publication_date = self.publication_date_input.text()

        if title and author and publisher and publication_date:
            book_info = f"{title} - {author} - {publisher} - {publication_date}"
            self.books_list.addItem(book_info)
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")

    def clear_inputs(self):
        self.title_input.clear()
        self.author_input.clear()
        self.publisher_input.clear()
        self.publication_date_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CatalogManagementApp()
    window.show()
    sys.exit(app.exec_())

