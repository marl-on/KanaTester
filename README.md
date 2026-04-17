# KanaPy
Memoriza y aprende el alfabeto Hiragana usando la terminal de tu equipo.

## Características
* Tamaño de cuestionario personalizado.
* Registro de intentos y calificación.
* Tabla de hiragana integrada para estudiar.

## Instalación

### Opción 1 — Descargar release
1. Ve a la sección [Releases](https://github.com/marl-on/KanaPy/releases)
2. Descarga el archivo correspondiente a tu sistema operativo
3. Extrae los archivos en una carpeta de tu elección

### Opción 2 — Compilar desde el código fuente
Requiere Python 3.12+:
```bash
git clone https://github.com/marl-on/KanaPy.git
cd KanaPy
pip install pyinstaller
pyinstaller --onefile main.py
```

## Uso

### Linux
Doble click en `KanaTester.sh` y ejecutar en terminal o ejecutar directamente en la terminal:
```bash
./KanaTester.sh
```

### Windows
Abrir `KanaTester.bat` o ejecuta desde la terminal:
```
KanaTester.bat
```

### Mac
Abrir `KanaTester.command` o ejecuta desde la terminal:
```bash
./KanaTester.command
```

#### Puedes agregar estos archivos al PATH de tu equipo para así poder correrlo directamente en la terminal.

### Desde el código fuente
```bash
python main.py
```

## Roadmap
- [ ] Implementación de dakuten/handakuten.
- [ ] Implementación de Katakana.
- [ ] Implementación de combinación de Kanas (Yo-on)

## Trabajando en
* [ ] Estructura de archivos más limpia.
* [ ] Documentación más organizada.