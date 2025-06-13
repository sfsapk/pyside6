from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 App")
        
        # Создаем две кнопки
        self.button1 = QPushButton("Кнопка 1")
        self.button2 = QPushButton("Кнопка 2")
        
        # Подключаем функции к кнопкам
        self.button1.clicked.connect(self.on_button1_click)
        self.button2.clicked.connect(self.on_button2_click)
        
        # Размещаем кнопки в layout
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        
        # Устанавливаем layout в центральный виджет
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def on_button1_click(self):
        print("Кнопка 1 нажата!")
    
    def on_button2_click(self):
        print("Кнопка 2 нажата!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
