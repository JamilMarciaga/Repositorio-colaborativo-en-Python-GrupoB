"""Utilidades generales para trabajar con texto, fechas y códigos."""

from datetime import datetime
import re
import secrets
import string
import unicodedata


_PATRON_EMAIL = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+$"
)
_CARACTERES_CODIGO = string.ascii_uppercase + string.digits


def _validar_texto(valor: object, nombre: str) -> None:
    """Comprueba que un valor sea texto y produce un error descriptivo."""
    if not isinstance(valor, str):
        raise TypeError(f"{nombre} debe ser una cadena de texto")


def limpiar_texto(texto: str) -> str:
    """Elimina espacios exteriores y reduce espacios internos a uno solo.

    Args:
        texto: Texto que se desea limpiar.

    Returns:
        El texto sin espacios innecesarios.

    Raises:
        TypeError: Si ``texto`` no es una cadena.
    """
    _validar_texto(texto, "texto")
    return " ".join(texto.split())


def contar_palabras(texto: str) -> int:
    """Cuenta las palabras de un texto después de normalizar sus espacios.

    Args:
        texto: Texto cuyas palabras se contarán.

    Returns:
        El número de palabras; cero cuando el texto está vacío.

    Raises:
        TypeError: Si ``texto`` no es una cadena.
    """
    texto_limpio = limpiar_texto(texto)
    return len(texto_limpio.split()) if texto_limpio else 0


def es_palindromo(texto: str) -> bool:
    """Indica si un texto se lee igual en ambos sentidos.

    Se ignoran los espacios, la puntuación, los signos diacríticos y las
    diferencias entre mayúsculas y minúsculas.

    Args:
        texto: Texto que se desea comprobar.

    Returns:
        ``True`` si los caracteres alfanuméricos forman un palíndromo.

    Raises:
        TypeError: Si ``texto`` no es una cadena.
    """
    _validar_texto(texto, "texto")
    sin_diacriticos = "".join(
        caracter
        for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )
    normalizado = "".join(
        caracter.casefold() for caracter in sin_diacriticos if caracter.isalnum()
    )
    return normalizado == normalizado[::-1]


def validar_email(email: str) -> bool:
    """Valida de manera básica la estructura de un correo electrónico.

    Args:
        email: Dirección de correo que se desea validar.

    Returns:
        ``True`` cuando contiene usuario, dominio y extensión válidos.

    Raises:
        TypeError: Si ``email`` no es una cadena.
    """
    _validar_texto(email, "email")
    return _PATRON_EMAIL.fullmatch(email) is not None


def formatear_fecha(
    fecha: str,
    formato_entrada: str = "%Y-%m-%d",
    formato_salida: str = "%d/%m/%Y",
) -> str:
    """Convierte una fecha de un formato textual a otro.

    Args:
        fecha: Fecha escrita según ``formato_entrada``.
        formato_entrada: Formato que se usará para interpretar la fecha.
        formato_salida: Formato del texto que se devolverá.

    Returns:
        La fecha convertida al formato solicitado.

    Raises:
        TypeError: Si alguno de los argumentos no es una cadena.
        ValueError: Si la fecha no coincide con el formato de entrada.
    """
    _validar_texto(fecha, "fecha")
    _validar_texto(formato_entrada, "formato_entrada")
    _validar_texto(formato_salida, "formato_salida")

    try:
        fecha_convertida = datetime.strptime(fecha, formato_entrada)
    except ValueError as error:
        raise ValueError(
            f"La fecha '{fecha}' no tiene el formato esperado '{formato_entrada}'"
        ) from error

    return fecha_convertida.strftime(formato_salida)


def generar_codigo(longitud: int = 8) -> str:
    """Genera un código aleatorio compuesto por mayúsculas y números.

    Args:
        longitud: Cantidad de caracteres del código; debe ser al menos cuatro.

    Returns:
        Un código alfanumérico de la longitud solicitada.

    Raises:
        TypeError: Si ``longitud`` no es un número entero.
        ValueError: Si ``longitud`` es menor que cuatro.
    """
    if isinstance(longitud, bool) or not isinstance(longitud, int):
        raise TypeError("longitud debe ser un número entero")
    if longitud < 4:
        raise ValueError("longitud debe ser al menos 4")

    return "".join(secrets.choice(_CARACTERES_CODIGO) for _ in range(longitud))
