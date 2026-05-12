import flet as ft
from datetime import datetime
import sqlite3

# =========================
# BASE DE DATOS
# =========================

conn = sqlite3.connect("parqueadero.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    placa TEXT,
    tipo TEXT,
    hora_entrada TEXT
)
""")

conn.commit()

# =========================
# TARIFAS
# =========================

TARIFAS = {
    "Carro": 3000,
    "Moto": 1000,
    "Cicla": 1000
}

# =========================
# APP PRINCIPAL
# =========================

def main(page: ft.Page):

    page.title = "Sistema Parqueadero"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 900
    page.window_height = 700
    page.padding = 20
    page.bgcolor = "#0f172a"

    # =========================
    # LOGO
    # =========================

    logo = ft.Image(
        src="parqueadero",   # nombre de tu imagen
        width=140,
        height=140,
    )

    titulo = ft.Text(
        "Sistema de Parqueadero",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="white"
    )

    subtitulo = ft.Text(
        "Control de entrada y salida de vehículos",
        size=16,
        color="grey"
    )

    placa_input = ft.TextField(
        label="Placa del vehículo",
        width=300
    )

    tipo_dropdown = ft.Dropdown(
        label="Tipo de vehículo",
        width=300,
        options=[
            ft.dropdown.Option("Carro"),
            ft.dropdown.Option("Moto"),
            ft.dropdown.Option("Cicla"),
        ]
    )

    resultado = ft.Text(size=18)

    tabla_vehiculos = ft.Column()

    # =========================
    # ACTUALIZAR TABLA
    # =========================

    def actualizar_tabla():

        tabla_vehiculos.controls.clear()

        cursor.execute("SELECT placa, tipo, hora_entrada FROM vehiculos")
        datos = cursor.fetchall()

        if not datos:
            tabla_vehiculos.controls.append(
                ft.Text(
                    "No hay vehículos registrados",
                    color="white"
                )
            )

        for vehiculo in datos:

            placa, tipo, hora = vehiculo

            tarjeta = ft.Container(
                content=ft.Column([
                    ft.Text(
                        f"Placa: {placa}",
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    ),
                    ft.Text(
                        f"Tipo: {tipo}",
                        color="white"
                    ),
                    ft.Text(
                        f"Entrada: {hora}",
                        color="white"
                    )
                ]),
                padding=15,
                border_radius=15,
                bgcolor="#1e293b"
            )

            tabla_vehiculos.controls.append(tarjeta)

        page.update()

    # =========================
    # REGISTRAR ENTRADA
    # =========================

    def registrar_entrada(e):

        placa = placa_input.value.upper()
        tipo = tipo_dropdown.value

        if not placa or not tipo:
            resultado.value = "⚠️ Completa todos los campos"
            resultado.color = "red"
            page.update()
            return

        hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
        INSERT INTO vehiculos (placa, tipo, hora_entrada)
        VALUES (?, ?, ?)
        """, (placa, tipo, hora_entrada))

        conn.commit()

        resultado.value = f"✅ Vehículo {placa} registrado"
        resultado.color = "green"

        placa_input.value = ""
        tipo_dropdown.value = None

        actualizar_tabla()

    # =========================
    # REGISTRAR SALIDA
    # =========================

    def registrar_salida(e):

        placa = placa_input.value.upper()

        if not placa:
            resultado.value = "⚠️ Ingresa una placa"
            resultado.color = "red"
            page.update()
            return

        cursor.execute("""
        SELECT tipo, hora_entrada
        FROM vehiculos
        WHERE placa = ?
        """, (placa,))

        vehiculo = cursor.fetchone()

        if not vehiculo:
            resultado.value = "❌ Vehículo no encontrado"
            resultado.color = "red"
            page.update()
            return

        tipo, hora_entrada = vehiculo

        hora_entrada = datetime.strptime(
            hora_entrada,
            "%Y-%m-%d %H:%M:%S"
        )

        hora_salida = datetime.now()

        tiempo = hora_salida - hora_entrada

        horas = tiempo.total_seconds() / 3600

        if horas < 1:
            horas = 1
        else:
            horas = int(horas) + 1

        total = horas * TARIFAS[tipo]

        cursor.execute("""
        DELETE FROM vehiculos
        WHERE placa = ?
        """, (placa,))

        conn.commit()

        resultado.value = (
            f"🚪 Salida registrada\n"
            f"Vehículo: {placa}\n"
            f"Tipo: {tipo}\n"
            f"Horas: {horas}\n"
            f"Total a pagar: ${total}"
        )

        resultado.color = "orange"

        placa_input.value = ""

        actualizar_tabla()

    # =========================
    # BOTONES
    # =========================

    boton_entrada = ft.ElevatedButton(
        "Registrar Entrada",
        icon=ft.Icons.LOGIN,
        on_click=registrar_entrada
    )

    boton_salida = ft.ElevatedButton(
        "Registrar Salida",
        icon=ft.Icons.LOGOUT,
        on_click=registrar_salida
    )

    # =========================
    # INTERFAZ
    # =========================

    page.add(

        ft.Column(
            [
                logo,
                titulo,
                subtitulo
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),

        ft.Divider(),

        placa_input,
        tipo_dropdown,

        ft.Row([
            boton_entrada,
            boton_salida
        ]),

        resultado,

        ft.Divider(),

        ft.Text(
            "Vehículos en parqueadero",
            size=22,
            weight=ft.FontWeight.BOLD,
            color="white"
        ),

        tabla_vehiculos
    )

    actualizar_tabla()


# =========================
# EJECUTAR APP
# =========================

ft.app(
    target=main,
    assets_dir="assets"
)