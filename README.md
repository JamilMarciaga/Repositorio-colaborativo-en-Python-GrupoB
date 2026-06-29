# Repositorio Colaborativo en Python - GrupoB

## Integrantes del Grupo

| # | Miembro | Rol | Módulo |
|---|---------|-----|--------|
| 1 | Jamil Marciaga | Miembro 1 | Operaciones Matemáticas |
| 2 | Gilberto Cano | Miembro 2 | Cuentos |
| 3 | Alexis Lopez | Miembro 3 | Utilidades |
| 4 | Esequiel González | Miembro 4 | Documentación (README) |

## Descripción
Repositorio colaborativo desarrollado en Python utilizando Git y GitHub para practicar el trabajo en equipo mediante el uso de ramas, commits, pull requests y revisiones de código.

Cada integrante del grupo participa en el desarrollo de un módulo específico y colabora en la mejora del código de sus compañeros siguiendo buenas prácticas de control de versiones.

## Estructura
Repositorio-colaborativo-en-Python-GrupoB/
│
├── src/
│   ├── __init__.py
│   ├── operaciones_matematicas.py
│   ├── cuento.py
│   └── utilidades.py
│
├── tests/
│   ├── __init__.py
│   ├── test_operaciones.py
│   ├── test_cuento.py
│   └── test_utilidades.py
│
├── docs/
│
├── README.md
├── .gitignore
└── requirements.txt

## Módulo de Utilidades

**Responsable: Alexis López**

El archivo `src/utilidades.py` reúne funciones generales para procesar texto,
validar datos, convertir fechas y generar códigos. Está implementado únicamente
con la librería estándar de Python.

### Funciones

- `limpiar_texto`: elimina espacios innecesarios.
- `contar_palabras`: cuenta las palabras de un texto limpio.
- `es_palindromo`: comprueba palíndromos ignorando espacios, tildes, mayúsculas y puntuación.
- `validar_email`: realiza una validación básica del formato de un correo.
- `formatear_fecha`: convierte una fecha de un formato textual a otro.
- `generar_codigo`: genera un código aleatorio con letras mayúsculas y números.

### Ejemplos de uso

```python
from src.utilidades import (
    contar_palabras,
    es_palindromo,
    formatear_fecha,
    generar_codigo,
    limpiar_texto,
    validar_email,
)

print(limpiar_texto("  Hola    mundo  "))       # Hola mundo
print(contar_palabras("Python es divertido"))    # 3
print(es_palindromo("Anita lava la tina"))       # True
print(validar_email("usuario@dominio.com"))       # True
print(formatear_fecha("2026-06-29"))              # 29/06/2026
print(generar_codigo(8))                           # Ejemplo: 7A2PX9QF
```

### Ejecutar las pruebas

Desde la raíz del repositorio, instala `pytest` si todavía no está disponible y
ejecuta la suite:

```bash
python -m pip install pytest
python -m pytest
```
