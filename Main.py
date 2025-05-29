import sys
import os
import threading
import pyzipper
import zipfile
import rarfile
import py7zr
import getpass
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QTextEdit, QProgressBar, QMessageBox, QLineEdit, QHBoxLayout, QRadioButton, QButtonGroup
)
from PyQt5.QtCore import Qt, QTimer

script_dir = os.path.dirname(os.path.abspath(__file__))
rarfile.UNRAR_TOOL = os.path.join(script_dir, 'unrar.exe')

class ZipBruteForcer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyberius - BruteForce ZIP/RAR/7Z")
        self.setGeometry(100, 100, 580, 500)
        self.setWindowIcon(QIcon(os.path.join(script_dir, "cyberius.ico")))

        self.username = getpass.getuser()
        self.archive_path = None
        self.dict_path = None
        self.output_path = None
        self.correct_password = None
        self.logs = []

        self.log_updater = QTimer()
        self.log_updater.timeout.connect(self.update_log)
        self.log_updater.start(100)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"👤 Usuario actual: {self.username}"))
        layout.addWidget(QLabel(f"📂 Carpeta de trabajo: {script_dir}"))

        self.label = QLabel("📎 Archivo comprimido: No seleccionado")
        layout.addWidget(self.label)

        self.zip_button = QPushButton("Seleccionar archivo comprimido (.zip, .rar, .7z)")
        self.zip_button.clicked.connect(self.select_archive)
        layout.addWidget(self.zip_button)

        self.dict_button = QPushButton("Seleccionar Diccionario (.txt)")
        self.dict_button.clicked.connect(self.select_dict)
        layout.addWidget(self.dict_button)

        self.manual_pass = QLineEdit()
        self.manual_pass.setPlaceholderText("🔐 Contraseña manual (opcional)")
        layout.addWidget(self.manual_pass)

        mode_layout = QHBoxLayout()
        self.mode_group = QButtonGroup(self)
        self.radio_brute = QRadioButton("🧠 Usar diccionario")
        self.radio_manual = QRadioButton("🔑 Usar contraseña manual")
        self.radio_brute.setChecked(True)
        self.mode_group.addButton(self.radio_brute)
        self.mode_group.addButton(self.radio_manual)
        mode_layout.addWidget(self.radio_brute)
        mode_layout.addWidget(self.radio_manual)
        layout.addLayout(mode_layout)

        self.output_label = QLabel("📁 Carpeta de extracción: No seleccionada")
        layout.addWidget(self.output_label)

        self.output_button = QPushButton("Seleccionar carpeta de extracción")
        self.output_button.clicked.connect(self.select_output)
        layout.addWidget(self.output_button)

        self.start_button = QPushButton("🚀 Iniciar Proceso")
        self.start_button.clicked.connect(self.start_process)
        layout.addWidget(self.start_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

        self.setLayout(layout)

    def update_log(self):
        while self.logs:
            self.log.append(self.logs.pop(0))

    def safe_log(self, message):
        try:
            print(message.encode('utf-8', errors='replace').decode('utf-8'))
        except Exception:
            print("[!] Error imprimiendo mensaje en consola.")
        self.logs.append(message)

    def select_archive(self):
        path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo comprimido", "", "Compressed Files (*.zip *.rar *.7z)")
        if path:
            self.archive_path = path
            self.label.setText(f"📎 Archivo: {os.path.basename(path)}")

    def select_dict(self):
        path, _ = QFileDialog.getOpenFileName(self, "Seleccionar diccionario", "", "Text Files (*.txt)")
        if path:
            self.dict_path = path
            self.dict_button.setText(f"📘 Diccionario: {os.path.basename(path)}")

    def select_output(self):
        path = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de extracción")
        if path:
            self.output_path = path
            self.output_label.setText(f"📁 Carpeta: {path}")

    def start_process(self):
        if not self.archive_path:
            QMessageBox.warning(self, "Error", "Debes seleccionar un archivo comprimido.")
            return
        if not self.output_path:
            QMessageBox.warning(self, "Error", "Debes seleccionar una carpeta de extracción.")
            return
        if self.radio_manual.isChecked() and not self.manual_pass.text().strip():
            QMessageBox.warning(self, "Falta contraseña", "Escribe una contraseña para modo manual.")
            return
        if self.radio_brute.isChecked() and not self.dict_path:
            QMessageBox.warning(self, "Falta diccionario", "Selecciona un diccionario o cambia al modo manual.")
            return

        self.start_button.setEnabled(False)

        if self.radio_manual.isChecked():
            threading.Thread(target=self.try_password, args=(self.manual_pass.text().strip(),), daemon=True).start()
        else:
            threading.Thread(target=self.brute_force_archive, daemon=True).start()

    def try_password(self, password):
        try:
            ext = os.path.splitext(self.archive_path)[1].lower()
            self.safe_log(f"🔎 Probando contraseña: {password}")

            if ext == ".zip":
                with pyzipper.AESZipFile(self.archive_path) as zf:
                    zf.pwd = password.encode('utf-8')
                    zf.extractall(path=self.output_path)

            elif ext == ".rar":
                rf = rarfile.RarFile(self.archive_path)
                rf.extractall(path=self.output_path, pwd=password)

            elif ext == ".7z":
                with py7zr.SevenZipFile(self.archive_path, mode='r', password=password) as archive:
                    archive.extractall(path=self.output_path)

            else:
                self.safe_log("❌ Formato no soportado")
                return

            self.safe_log(f"✅ Contraseña correcta: {password}")
            QTimer.singleShot(0, lambda: QMessageBox.information(self, "Éxito", f"Contraseña correcta: {password}"))

        except Exception as e:
            msg = str(e)
            if "req=12 got=0" in msg:
                self.safe_log(f"❌ Contraseña incorrecta: {password}")
            else:
                self.safe_log(f"❌ Error al probar contraseña: {msg}")
            QTimer.singleShot(0, lambda: QMessageBox.warning(self, "Error", msg))

        QTimer.singleShot(0, lambda: self.start_button.setEnabled(True))

    def brute_force_archive(self):
        try:
            with open(self.dict_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]

            total = len(passwords)
            self.progress_bar.setMaximum(total)

            ext = os.path.splitext(self.archive_path)[1].lower()
            self.safe_log(f"🔎 Tipo de archivo: {ext}")

            for i, password in enumerate(passwords):
                QTimer.singleShot(0, lambda val=i+1: self.progress_bar.setValue(val))
                self.safe_log(f"🔑 Intentando: {password}")

                try:
                    if ext == ".zip":
                        with pyzipper.AESZipFile(self.archive_path) as zf:
                            zf.pwd = password.encode('utf-8')
                            zf.extractall(path=self.output_path)
                    elif ext == ".rar":
                        rf = rarfile.RarFile(self.archive_path)
                        rf.extractall(path=self.output_path, pwd=password)
                    elif ext == ".7z":
                        with py7zr.SevenZipFile(self.archive_path, mode='r', password=password) as archive:
                            archive.extractall(path=self.output_path)
                    else:
                        self.safe_log("❌ Formato no soportado")
                        break

                    self.correct_password = password
                    self.safe_log(f"✅ Contraseña encontrada: {password}")
                    QTimer.singleShot(0, lambda: QMessageBox.information(self, "¡Éxito!", f"Contraseña encontrada: {password}"))
                    break

                except Exception as e:
                    msg = str(e)
                    if "req=12 got=0" in msg:
                        self.safe_log(f"❌ Contraseña incorrecta: {password}")
                    else:
                        self.safe_log(f"❌ Fallo con {password}: {msg}")
                    continue

            else:
                self.safe_log("⛔ Contraseña no encontrada en el diccionario")
                QTimer.singleShot(0, lambda: QMessageBox.warning(self, "Fallido", "No se encontró la contraseña."))

        except Exception as e:
            self.safe_log(f"⚠️ Error general: {str(e)}")

        QTimer.singleShot(0, lambda: self.start_button.setEnabled(True))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ZipBruteForcer()
    window.show()
    sys.exit(app.exec_())
