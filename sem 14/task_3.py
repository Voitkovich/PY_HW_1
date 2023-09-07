from task_1 import clear_text
import pytest


def test_no_change():
    assert clear_text('some text') == 'some text'


def test_registre_change():
    assert clear_text('SoMe TexT') == 'some text'


def test_punctuation_delete():
    assert (clear_text('SoMe, TexT') == 'some text'), """Пунктуация\
    - корявая. Поправь её"""


if __name__ == "__main__":
    pytest.main(['-v'])