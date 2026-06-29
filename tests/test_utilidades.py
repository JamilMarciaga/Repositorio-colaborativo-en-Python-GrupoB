"""Pruebas unitarias para el módulo de utilidades."""

import re

import pytest

from src.utilidades import (
    contar_palabras,
    es_palindromo,
    formatear_fecha,
    generar_codigo,
    limpiar_texto,
    validar_email,
)


@pytest.mark.parametrize(
    ("entrada", "esperado"),
    [
        ("  Hola    mundo  ", "Hola mundo"),
        ("\tHola\n mundo\r\n", "Hola mundo"),
        ("", ""),
        ("     ", ""),
        ("Python", "Python"),
    ],
)
def test_limpiar_texto(entrada: str, esperado: str) -> None:
    assert limpiar_texto(entrada) == esperado


def test_limpiar_texto_rechaza_valor_no_textual() -> None:
    with pytest.raises(TypeError, match="texto debe ser una cadena"):
        limpiar_texto(123)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("texto", "cantidad"),
    [
        ("uno dos tres", 3),
        ("  uno    dos  ", 2),
        ("", 0),
        (" \t\n ", 0),
        ("palabra", 1),
    ],
)
def test_contar_palabras(texto: str, cantidad: int) -> None:
    assert contar_palabras(texto) == cantidad


def test_contar_palabras_rechaza_valor_no_textual() -> None:
    with pytest.raises(TypeError, match="texto debe ser una cadena"):
        contar_palabras(None)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "texto",
    [
        "Anita lava la tina",
        "¿Acaso hubo búhos acá?",
        "A man, a plan, a canal: Panama!",
        "",
    ],
)
def test_es_palindromo_acepta_palindromos(texto: str) -> None:
    assert es_palindromo(texto) is True


def test_es_palindromo_rechaza_texto_que_no_es_palindromo() -> None:
    assert es_palindromo("Hola mundo") is False


def test_es_palindromo_rechaza_valor_no_textual() -> None:
    with pytest.raises(TypeError, match="texto debe ser una cadena"):
        es_palindromo(["ana"])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "email",
    [
        "usuario@dominio.com",
        "nombre.apellido+curso@sub.dominio.edu",
        "usuario_123@dominio.com.pa",
    ],
)
def test_validar_email_acepta_formatos_validos(email: str) -> None:
    assert validar_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "usuario",
        "usuario@",
        "@dominio.com",
        "usuario@dominio",
        "usuario@.com",
        "usuario@dominio.",
        "usuario @dominio.com",
        "usuario@-dominio.com",
        "",
    ],
)
def test_validar_email_rechaza_formatos_invalidos(email: str) -> None:
    assert validar_email(email) is False


def test_validar_email_rechaza_valor_no_textual() -> None:
    with pytest.raises(TypeError, match="email debe ser una cadena"):
        validar_email(10)  # type: ignore[arg-type]


def test_formatear_fecha_con_formatos_predeterminados() -> None:
    assert formatear_fecha("2026-06-29") == "29/06/2026"


def test_formatear_fecha_con_formatos_personalizados() -> None:
    assert formatear_fecha("29/06/2026", "%d/%m/%Y", "%Y.%m.%d") == "2026.06.29"


@pytest.mark.parametrize("fecha", ["29-06-2026", "2026-02-30", ""])
def test_formatear_fecha_rechaza_fecha_incorrecta(fecha: str) -> None:
    with pytest.raises(ValueError, match="no tiene el formato esperado"):
        formatear_fecha(fecha)


@pytest.mark.parametrize(
    ("argumentos", "nombre"),
    [
        ((20260629,), "fecha"),
        (("2026-06-29", None), "formato_entrada"),
        (("2026-06-29", "%Y-%m-%d", None), "formato_salida"),
    ],
)
def test_formatear_fecha_rechaza_tipos_incorrectos(
    argumentos: tuple[object, ...], nombre: str
) -> None:
    with pytest.raises(TypeError, match=nombre):
        formatear_fecha(*argumentos)  # type: ignore[arg-type]


@pytest.mark.parametrize("longitud", [4, 8, 20])
def test_generar_codigo_respeta_longitud_y_alfabeto(longitud: int) -> None:
    codigo = generar_codigo(longitud)

    assert len(codigo) == longitud
    assert re.fullmatch(r"[A-Z0-9]+", codigo)


def test_generar_codigo_usa_longitud_predeterminada() -> None:
    assert len(generar_codigo()) == 8


@pytest.mark.parametrize("longitud", [3, 0, -1])
def test_generar_codigo_rechaza_longitud_menor_que_cuatro(longitud: int) -> None:
    with pytest.raises(ValueError, match="al menos 4"):
        generar_codigo(longitud)


@pytest.mark.parametrize("longitud", [8.0, "8", None, True])
def test_generar_codigo_rechaza_tipo_incorrecto(longitud: object) -> None:
    with pytest.raises(TypeError, match="número entero"):
        generar_codigo(longitud)  # type: ignore[arg-type]
