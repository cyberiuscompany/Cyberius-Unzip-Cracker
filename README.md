# 🛡️ CyberiusUnzipCracker

Herramienta gráfica en Python para recuperar archivos comprimidos protegidos por contraseña mediante fuerza bruta.  
Soporta los formatos `.zip`, `.rar` y `.7z`. Ideal para entornos forenses, de recuperación o ciberseguridad.

---

## 🎥 Demostración

<p align="center">
  <img src="docs/demo.gif" width="600" alt="Demostración de CyberiusUnzipCracker">
</p>

## Capturas de pantalla

<div style="display: flex; justify-content: space-between; gap: 10px;">
  <img src="Captura_Principal.png" alt="Interfaz Principal" width="48%">
  <img src="Captura_Comprimido_Crackeado.png" alt="Comprimido Crackeado" width="48%">
</div>
---

## ⚙️ Funcionalidades

- ✅ Interfaz gráfica en PyQt5  
- ✅ Modo diccionario o contraseña manual  
- ✅ Soporte para archivos `.zip`, `.rar` y `.7z`  
- ✅ Barra de progreso e historial de intentos  
- ✅ Consola con `dir` y archivo resumen tras extracción  
- ✅ Exporta resultado a `.txt`  
- ✅ Icono personalizado estilo Cyberius  

---

## 🧩 Requisitos del sistema

- Python 3.8 o superior  
- Windows 64-bit  
- `unrar.exe` para extraer archivos `.rar`  

---

## 📄 Documentación adicional

- [🔐 Seguridad](.github/SECURITY.md)
- [📜 Licencia](LICENSE)
- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [📢 Soporte](.github/SUPPORT.md)
- [⚠️ Aviso legal](DISCLAIMER.md)

---

## Configura `unrar.exe` para archivos `.rar`

Para que el programa funcione correctamente con archivos `.rar`, necesitas tener `unrar.exe` en el mismo directorio que `Main.py`. Sigue estos pasos:

1. **Descarga el paquete oficial desde la página de RARLab**:  
   👉 [https://www.rarlab.com/rar_add.htm](https://www.rarlab.com/rar_add.htm)

2. **Elige la opción** _"Unsigned executables"_.  
   Se descargará un archivo llamado `rarlng_unsigned.rar`.

3. **Extrae** el contenido del archivo `.rar` descargado.

4. Dentro de la carpeta `rarlng_unsigned\x64`, **localiza el fichero** `UnRAR.exe`.

5. **Renómbralo** como `unrar.exe`.

6. **Coloca** `unrar.exe` en la misma carpeta donde está tu archivo `Main.py`.

> ✅ Una vez hecho esto, tu programa podrá trabajar con archivos `.rar` sin problemas.

---

## ⚙️ Instalación y Uso

### 1. Instalación desde el código fuente

Puedes clonar o descargar este proyecto y usarlo directamente con Python:

```bash
git clone https://github.com/CyberiusCompany/Cyberius-Unzip-Cracker.git
cd Cyberius-Unzip-Cracker
pip install -r requirements.txt
python Main.py
```

---

### 2. Instalación profesional como paquete

También puedes instalar el proyecto con `setup.py` para habilitar un comando global:

```bash
git clone https://github.com/CyberiusCompany/Cyberius-Unzip-Cracker.git
cd Cyberius-Unzip-Cracker
pip install .
cyberiusunzip
```

---

### 3. Compilación a formato `.exe`

Si deseas generar un archivo ejecutable (`.exe`) de **CyberiusUnzipCracker**  
con su icono personalizado y sin consola, sigue estos pasos:

Esto generará el archivo ejecutable dentro de la carpeta:

```
dist/CyberiusUnzipCracker/CyberiusUnzipCracker.exe
```

#### Pasos:

```bash
cd Cyberius-Unzip-Cracker
pip install pyinstaller
pyinstaller CyberiusUnzipCracker.spec
```

> ⚠️ Asegúrate de que `unrar.exe`, `cyberius.ico` y otros archivos estén en las rutas correctas definidas en el `.spec`.
