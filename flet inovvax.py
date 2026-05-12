import flet as ft

class InnovaXApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "InnovaX - Plataforma Inteligente"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#0f172a"
        self.color_principal = "#2563eb"

        self.build_ui()

    def build_ui(self):
        # FRAMES
        self.frame_inicio = ft.Container(expand=True, visible=True, content=self.inicio())
        self.frame_problema = ft.Container(expand=True, visible=False, content=self.problema())
        self.frame_solucion = ft.Container(expand=True, visible=False, content=self.solucion())
        self.frame_funcionamiento = ft.Container(expand=True, visible=False, content=self.funcionamiento())

        layout = ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    padding=15,
                    bgcolor="#1e293b",
                    content=ft.Row([
                        ft.Text("INNOVAX", size=22, weight="bold", color="white"),
                        ft.Row([
                            ft.TextButton("Inicio", on_click=lambda _: self.cambiar(0)),
                            ft.TextButton("Problema", on_click=lambda _: self.cambiar(1)),
                            ft.TextButton("Solución", on_click=lambda _: self.cambiar(2)),
                            ft.TextButton("Cómo funciona", on_click=lambda _: self.cambiar(3)),
                        ])
                    ], alignment="spaceBetween")
                ),
                ft.Stack([
                    self.frame_inicio,
                    self.frame_problema,
                    self.frame_solucion,
                    self.frame_funcionamiento
                ], expand=True)
            ]
        )

        self.page.add(layout)

    def inicio(self):
        return ft.Column([
            ft.Image(src="imagenpgc.png", width=350),
            ft.Text("InnovaX", size=50, weight="bold", color="white"),
            ft.Text("Plataforma inteligente para gestión de inventarios", size=20, color="white"),
            ft.ElevatedButton("Ver problema", on_click=lambda _: self.cambiar(1), bgcolor=self.color_principal)
        ], alignment="center", horizontal_alignment="center")

    def problema(self):
        return ft.Column([
            ft.Image(src="assets/problema.png", width=250),
            ft.Text("Problema", size=40, weight="bold", color="white"),
            ft.Text("Las microempresas no tienen un control eficiente de su inventario.", color="white"),
            ft.Text("Esto genera pérdidas por productos agotados o sobrestock.", color="white"),
            ft.ElevatedButton("Ver solución", on_click=lambda _: self.cambiar(2))
        ], alignment="center", horizontal_alignment="center")

    def solucion(self):
        return ft.Column([
            ft.Image(src="assets/solucion.png", width=250),
            ft.Text("Solución", size=40, weight="bold", color="white"),
            ft.Text("InnovaX permite registrar productos, entradas y salidas.", color="white"),
            ft.Text("Además, predice cuándo un producto se agotará.", color="white"),
            ft.ElevatedButton("Cómo funciona", on_click=lambda _: self.cambiar(3))
        ], alignment="center", horizontal_alignment="center")

    def funcionamiento(self):
        return ft.Column([
            ft.Image(src="assets/ia.png", width=250),
            ft.Text("¿Cómo funciona?", size=40, weight="bold", color="white"),
            ft.Text("Analiza el historial de ventas.", color="white"),
            ft.Text("Calcula tendencias de consumo.", color="white"),
            ft.Text("Genera alertas antes de que se acabe el stock.", color="white"),
            ft.ElevatedButton("Volver al inicio", on_click=lambda _: self.cambiar(0))
        ], alignment="center", horizontal_alignment="center")

    def cambiar(self, index):
        self.frame_inicio.visible = index == 0
        self.frame_problema.visible = index == 1
        self.frame_solucion.visible = index == 2
        self.frame_funcionamiento.visible = index == 3
        self.page.update()


def main(page: ft.Page):
    InnovaXApp(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets", port=8550)
