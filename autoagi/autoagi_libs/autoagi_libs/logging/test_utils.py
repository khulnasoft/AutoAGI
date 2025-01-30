import pytest

from .utils import remove_color_codes


@pytest.mark.parametrize(
    "raw_text, clean_text",
    [
        (
            "COMMAND = \x1b[36mbrowse_website\x1b[0m  "
            "ARGUMENTS = \x1b[36m{'url': 'https://www.google.com',"
            " 'question': 'What is the capital of France?'}\x1b[0m",
            "COMMAND = browse_website  "
            "ARGUMENTS = {'url': 'https://www.google.com',"
            " 'question': 'What is the capital of France?'}",
        ),
        (
            "{'Schaue dir meine Projekte auf github () an, als auch meine Webseiten': "
            "'https://github.com/KhulnaSoft/AutoAGI,"
            " https://discord.gg/autoagi und https://twitter.com/KhulnaSoft'}",
            "{'Schaue dir meine Projekte auf github () an, als auch meine Webseiten': "
            "'https://github.com/KhulnaSoft/AutoAGI,"
            " https://discord.gg/autoagi und https://twitter.com/KhulnaSoft'}",
        ),
        ("", ""),
        ("hello", "hello"),
        ("hello\x1b[31m world", "hello world"),
        ("\x1b[36mHello,\x1b[32m World!", "Hello, World!"),
        (
            "\x1b[1m\x1b[31mError:\x1b[0m\x1b[31m file not found",
            "Error: file not found",
        ),
    ],
)
def test_remove_color_codes(raw_text, clean_text):
    assert remove_color_codes(raw_text) == clean_text
