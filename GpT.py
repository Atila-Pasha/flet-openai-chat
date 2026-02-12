from openai import OpenAI
import flet as ft
from API_KEY import api_token

# ================== OpenAI Clients ==================
client = OpenAI(
    api_key=api_token,
    base_url="https://api.gapgpt.app/v1"
)



# ================== Flet App ==================
def main(page: ft.Page):
    page.title = "AtA GPT"
    page.window.height = 600
    page.window.width = 600
    page.padding = 0
    page.bgcolor = "#1e1e2f"

    # ---------- Message Text ----------
    message_text = ft.Text(
        value="Hi! My name is AtA GPT.\nHow can I help you?",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",
        align=ft.Alignment.CENTER,
        selectable=True,
    )

    # ---------- Image ----------
    img = ft.Image(
        src="",
        width=480,
        height=360,
    )

    # ---------- Scrollable Content ----------
    content_column = ft.Column(
        controls=[message_text],
        scroll=ft.ScrollMode.AUTO,
    )

    # ---------- Center Box ----------
    center_box = ft.Container(
        width=500,
        height=400,
        padding=15,
        border_radius=20,
        gradient=ft.LinearGradient(
            colors=["#ff6a00", "#ee0979"],
        ),
        shadow=ft.BoxShadow(
            blur_radius=25,
            color=ft.Colors.BLACK54,
            offset=ft.Offset(0, 8),
        ),
        content=content_column,
    )

    # ---------- TextField ----------
    textfield = ft.TextField(
        hint_text="Enter your text here...",
        width=350,
        text_size=16,
        color="white",
        cursor_color="white",
        bgcolor="#2a2a40",
        border_radius=15,
        border_color="#6a5acd",
        focused_border_color="#ff6a00",
        hint_style=ft.TextStyle(color="#aaaaaa"),
        prefix_icon=ft.Icons.EDIT,
        filled=True,
    )

    # ---------- Text Generator ----------
    def show_text(e):
        if not textfield.value.strip():
            message_text.value = "Please enter a message."
            page.update()
            return

        message_text.value = "Wait..."
        content_column.controls.clear()
        content_column.controls.append(message_text)
        page.update()

        try:
            response = client.responses.create(
                model="o4-mini",
                input=textfield.value
            )
            message_text.value = response.output_text
        except Exception as ex:
            message_text.value = f"Error: {ex}"

        textfield.value = ""
        page.update()

    # ---------- Image Generator ----------
    def generate_image(e):
        pass
        #if not textfield.value.strip():
        #    message_text.value = "Please enter a prompt."
        #    page.update()
        #    return

        #message_text.value = "Wait..."
        #content_column.controls.clear()
        #content_column.controls.append(message_text)
        #page.update()

        #try:
        #    response = img_client.images.generate(
        #        model="gapgpt/z-image",
        #        prompt=textfield.value,
        #        size="500x400"
        #    )
        #    img.src = response.data[0].url

        #    content_column.controls.clear()
        #    content_column.controls.append(img)

        #except Exception as ex:
        #    message_text.value = f"Error: {ex}"
        #    content_column.controls.clear()
        #    content_column.controls.append(message_text)

        #textfield.value = ""
        #page.update()

    # ---------- Buttons ----------
    send_button = ft.ElevatedButton(
        content="SEND",
        icon=ft.Icons.SEND,
        on_click=show_text,
        height=50,
        width=150,
        style=ft.ButtonStyle(
            bgcolor="#4facfe",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=15),
        ),
    )

    generate_button = ft.ElevatedButton(
        content="GENERATE",
        icon=ft.Icons.GENERATING_TOKENS,
        on_click=generate_image,
        height=50,
        width=150,
        style=ft.ButtonStyle(
            bgcolor="#5c6f80",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=15),
        ),
        disabled=True
    )

    # ---------- Layout ----------
    page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(expand=True),
                center_box,
                ft.Container(height=15),
                textfield,
                ft.Container(height=15),
                ft.Row(
                    [send_button, generate_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=25),
            ],
        )
    )


ft.app(target=main)
