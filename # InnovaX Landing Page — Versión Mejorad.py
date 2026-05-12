import flet as ft
class InnovaX:
    def __init__(self, page: ft.Page):
        self.page = page

        # ---------------- CONFIGURACIÓN ----------------

        self.page.title = "InnovaX"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = "#f8fafc"
        self.page.padding = 0
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.window_width = 1300
        self.page.window_height = 850

        # ---------------- COLORES ----------------

        self.azul = "#2563eb"
        self.azul_claro = "#dbeafe"
        self.blanco = "#ffffff"
        self.negro = "#0f172a"
        self.gris = "#475569"
        self.card = "#ffffff"

        self.ui()

    # ---------------- SCROLL ----------------

    async def ir_inicio(self, e):
        await self.page.scroll_to(offset=0)

    async def ir_problema(self, e):
        await self.page.scroll_to(offset=700)

    async def ir_solucion(self, e):
        await self.page.scroll_to(offset=1400)

    # ---------------- TARJETAS ----------------

    def crear_card(self, icono, titulo, texto):
        return ft.Container(
            width=290,
            padding=25,
            border_radius=20,
            bgcolor=self.card,

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=18,
                color="#00000015",
                offset=ft.Offset(0, 6),
            ),

            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[

                    ft.Container(
                        width=80,
                        height=80,
                        border_radius=40,
                        bgcolor=self.azul_claro,
                        alignment=ft.Alignment(0, 0),

                        content=ft.Icon(
                            icono,
                            size=40,
                            color=self.azul,
                        ),
                    ),

                    ft.Text(
                        titulo,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=self.negro,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    ft.Text(
                        texto,
                        color=self.gris,
                        text_align=ft.TextAlign.CENTER,
                        size=15,
                    ),
                ],
            ),
        )

    # ---------------- INTERFAZ ----------------

    def ui(self):

        self.page.add(

            ft.Column(
                spacing=0,
                controls=[

                    # ---------------- NAVBAR ----------------

                    ft.Container(
    padding=20,
    bgcolor="#1e3a8a",

    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=10,
        color="#00000020",
        offset=ft.Offset(0, 2),
    ),

    content=ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        controls=[

            # LOGO

            ft.Row(
                spacing=10,
                controls=[

                    ft.Icon(
                        ft.Icons.AUTO_GRAPH,
                        color="white",
                        size=35,
                    ),

                    ft.Text(
                        "INNOVAX",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                ],
            ),

            # BOTONES

            ft.Row(
                spacing=20,
                controls=[

                    ft.TextButton(
                        "Inicio",
                        style=ft.ButtonStyle(
                            color="white",
                        ),
                        on_click=self.ir_inicio,
                    ),

                    ft.TextButton(
                        "Problema",
                        style=ft.ButtonStyle(
                            color="white",
                        ),
                        on_click=self.ir_problema,
                    ),

                    ft.TextButton(
                        "Solución",
                        style=ft.ButtonStyle(
                            color="white",
                        ),
                        on_click=self.ir_solucion,
                    ),
                ],
            ),
        ],
    ),
),

                    # ---------------- HERO ----------------

                    ft.Container(
                        padding=50,
                        height=720,

                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,

                            controls=[

                                # -------- TEXTO --------

                                ft.Column(
                                    width=550,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=20,

                                    controls=[

                                        ft.Container(
                                            bgcolor=self.azul_claro,
                                            border_radius=30,
                                            padding=12,

                                            content=ft.Text(
                                                "Plataforma Inteligente",
                                                color=self.azul,
                                                weight=ft.FontWeight.BOLD,
                                            ),
                                        ),

                                        ft.Text(
                                            "Control Inteligente de Inventarios",
                                            size=52,
                                            weight=ft.FontWeight.BOLD,
                                            color=self.negro,
                                        ),

                                        ft.Text(
                                            "InnovaX ayuda a las MiPyMEs a gestionar productos, analizar inventarios y prevenir desabastecimientos usando análisis predictivo.",
                                            size=19,
                                            color=self.gris,
                                        ),

                                        ft.Row(
                                            spacing=15,
                                            controls=[

                                                ft.ElevatedButton(
                                                    "Comenzar",

                                                    bgcolor=self.azul,
                                                    color="white",

                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(
                                                            radius=12
                                                        ),
                                                        padding=20,
                                                    ),

                                                    on_click=self.ir_solucion,
                                                ),

                                                ft.OutlinedButton(
                                                    "Ver más",

                                                    style=ft.ButtonStyle(
                                                        side=ft.BorderSide(
                                                            2,
                                                            self.azul,
                                                        ),
                                                        shape=ft.RoundedRectangleBorder(
                                                            radius=12
                                                        ),
                                                        padding=20,
                                                    ),

                                                    on_click=self.ir_problema,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),

                                # -------- LOGO --------

                                ft.Container(
                                    width=520,
                                    height=450,
                                    border_radius=30,
                                    bgcolor=self.blanco,

                                    shadow=ft.BoxShadow(
                                        spread_radius=1,
                                        blur_radius=25,
                                        color="#00000020",
                                        offset=ft.Offset(0, 10),
                                    ),

                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                                        controls=[

                                            ft.Image(
                                                src="innovax.png",
                                                width=340,
                                                height=340,
                                            ),

                                            ft.Text(
                                                "Logo InnovaX",
                                                size=30,
                                                weight=ft.FontWeight.BOLD,
                                                color=self.negro,
                                            ),

                                            ft.Text(
                                                "Análisis y monitoreo inteligente",
                                                size=16,
                                                color=self.gris,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),

                    # ---------------- PROBLEMA ----------------

                    ft.Container(
                        padding=60,

                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,

                            controls=[

                                ft.Text(
                                    "El Problema",
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    color=self.negro,
                                ),

                                ft.Text(
                                    "Muchas MiPyMEs presentan pérdidas debido a la mala gestión de inventarios.",
                                    size=17,
                                    color=self.gris,
                                    text_align=ft.TextAlign.CENTER,
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    wrap=True,
                                    spacing=25,

                                    controls=[

                                        self.crear_card(
                                            ft.Icons.WARNING_AMBER,
                                            "Desabastecimiento",
                                            "Productos agotados inesperadamente.",
                                        ),

                                        self.crear_card(
                                            ft.Icons.MONEY_OFF,
                                            "Pérdidas",
                                            "Exceso de compras y desperdicio.",
                                        ),

                                        self.crear_card(
                                            ft.Icons.BAR_CHART,
                                            "Falta de análisis",
                                            "No existen predicciones de consumo.",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),

                    # ---------------- SOLUCIÓN ----------------

                    ft.Container(
                        padding=60,
                        bgcolor="#eff6ff",

                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,

                            controls=[

                                ft.Text(
                                    "La Solución",
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    color=self.negro,
                                ),

                                ft.Text(
                                    "InnovaX permite automatizar y optimizar el control de inventarios.",
                                    size=17,
                                    color=self.gris,
                                    text_align=ft.TextAlign.CENTER,
                                ),

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    wrap=True,
                                    spacing=25,

                                    controls=[

                                        self.crear_card(
                                            ft.Icons.INVENTORY_2,
                                            "Inventario",
                                            "Control de entradas y salidas.",
                                        ),

                                        self.crear_card(
                                            ft.Icons.AUTO_GRAPH,
                                            "Predicción",
                                            "Estimación del consumo futuro.",
                                        ),

                                        self.crear_card(
                                            ft.Icons.NOTIFICATIONS_ACTIVE,
                                            "Alertas",
                                            "Avisos antes del agotamiento.",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),

                    # ---------------- FOOTER ----------------

                    ft.Container(
                        padding=35,
                        bgcolor=self.negro,

                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,

                            controls=[

                                ft.Text(
                                    "InnovaX",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),

                                ft.Text(
                                    "Proyecto de Ingeniería de Software",
                                    color="#cbd5e1",
                                ),

                                ft.Text(
                                    "© 2026",
                                    color="#94a3b8",
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )


async def main(page: ft.Page):
    InnovaX(page)


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
        port=8550,
    )