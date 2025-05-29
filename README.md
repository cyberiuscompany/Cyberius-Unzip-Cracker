# 🛡️ CyberiusUnzipCracker

Herramienta gráfica en Python para recuperar archivos comprimidos protegidos por contraseña mediante fuerza bruta.  
Soporta los formatos `.zip`, `.rar` y `.7z`. Ideal para entornos forenses, de recuperación o ciberseguridad.

---

## 🎥 Capturas de pantalla

### Interfaz principal
![Interfaz Principal](Captura_Principal.png)

### Resultado tras descomprimir
![Comprimido Crackeado](Captura_Comprimido_Crackeado.png)

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

### 1. Clona o descarga este proyecto

```bash
git clone https://github.com/CyberiusUnzipCracker.git
cd CyberiusUnzipCracker
pip install -r requirements.txt
python Main.py
