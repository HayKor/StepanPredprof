from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import requests
import numpy as np
from PIL import Image, ImageQt
from app.lib.utils.parser_map import fetch_tile

print(fetch_tile("https://olimp.miet.ru/ppo_it/api"))

API_URL = "https://olimp.miet.ru/ppo_it/api"

class MarsCommGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mars Communication System")
        self.setGeometry(100, 100, 800, 600)
        self.map_data = np.zeros((256, 256), dtype=np.uint8)
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.api_input = QLineEdit(self)
        self.api_input.setPlaceholderText("Введите URL API")
        self.api_input.setText(API_URL)
        
        self.map_label = QLabel(self)
        self.map_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.map_label.setText("Здесь будет отображаться карта")
        
        self.load_map_button = QPushButton("Загрузить карту")
        self.load_map_button.clicked.connect(self.load_map)
        
        self.load_coords_button = QPushButton("Загрузить координаты модулей")
        self.load_coords_button.clicked.connect(self.load_coords)
        
        layout.addWidget(self.api_input)
        layout.addWidget(self.map_label)
        layout.addWidget(self.load_map_button)
        layout.addWidget(self.load_coords_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def fetch_tile(self):
        url = self.api_input.text().strip()
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json().get("message", {}).get("data", [])
                return np.array(data, dtype=np.uint8)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при получении данных: {e}")
        return None

    def load_map(self):
        full_map = np.zeros((256, 256), dtype=np.uint8)
        tile_size = 64
        for i in range(4):
            for j in range(4):
                tile = self.fetch_tile()
                if tile is not None:
                    full_map[i * tile_size:(i + 1) * tile_size, j * tile_size:(j + 1) * tile_size] = tile
        
        self.map_data = full_map
        self.display_map()
    
    def display_map(self):
        image = Image.fromarray(self.map_data, mode="L")
        qt_image = ImageQt.ImageQt(image)
        pixmap = QPixmap.fromImage(qt_image)
        self.map_label.setPixmap(pixmap)
        self.map_label.setText("")
    
    def load_coords(self):
        url = f"{self.api_input.text().strip()}/coords"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json().get("message", {})
                sender = data.get("sender", [])
                listener = data.get("listener", [])
                price = data.get("price", [])
                QMessageBox.information(self, "Координаты модулей", f"Отправитель: {sender}\nПолучатель: {listener}\nЦены установки: {price}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при получении координат: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarsCommGUI()
    window.show()
    sys.exit(app.exec())
