from vkbottle import Keyboard, Text


def get_two_buttons_inline_keyboard(
        text_first_button: str,
        text_second_button: str,
) -> Keyboard:
    """
    Возвращает две inline-кнопки.
    Параметр inline при создании кнопок задан True.
    """
    return (
        Keyboard(inline=True)
        .add(Text(text_first_button))
        .add(Text(text_second_button))
    )


def get_menu_button() -> Keyboard:
    """
    Меню с четырьмя кнопка: Погода, Валюта.
    """
    return (
        Keyboard()
        .add(Text("Погода"))
        .add(Text("Валюта"))
    )
