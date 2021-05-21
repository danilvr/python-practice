import re


def html_delete(hypertext: str) -> str:
    """
    Транслятор, который удаляет HTML-теги и оставляет обычный текст
    """
    return re.sub('<[^>]*>', '', hypertext)