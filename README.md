# Repositorio Colaborativo en Python - GrupoB

## Integrantes del Grupo

| # | Miembro | Rol | Módulo |
|---|---------|-----|--------|
| 1 | Jamil Marciaga | Miembro 1 | Operaciones Matemáticas |
| 2 | Gilberto Cano | Miembro 2 | Cuentos |
| 3 | Alexis Lopez | Miembro 3 | Utilidades |
| 4 | Esequiel Gonzalez | Miembro 4 | README |

## Descripción
El presente repositorio colaborativo tiene como objetivo principal desarrollar un proyecto en Python que integre tres módulos fundamentales, cada uno a cargo de un miembro del equipo, con la participación de un cuarto integrante para la ampliación de funcionalidades. Este proyecto busca demostrar las capacidades de trabajo en equipo, la implementación de buenas prácticas de programación y el uso eficiente de herramientas de control de versiones como Git y GitHub.

El proyecto está estructurado para abordar diferentes áreas de la programación en Python, desde operaciones matemáticas básicas hasta el procesamiento de texto y la generación de utilidades prácticas. Cada módulo ha sido diseñado para ser independiente pero complementario, permitiendo que los diferentes equipos trabajen de manera paralela sin interferencias, mientras mantienen una integración coherente en el proyecto final.

Objetivos del Proyecto
Fomentar el trabajo colaborativo: Desarrollar habilidades de programación en equipo utilizando Git y GitHub como plataforma principal de colaboración.

Implementar buenas prácticas: Aplicar principios de programación limpia, documentación adecuada y pruebas unitarias exhaustivas.

Crear un proyecto modular: Desarrollar un sistema con módulos independientes que puedan ser reutilizados en futuros proyectos.

Demostrar competencias técnicas: Mostrar dominio de Python, manejo de librerías estándar y resolución de problemas computacionales.
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
