from django.conf import settings

from . import aes


def decode_card_number(encode_str: str) -> str:
    if encode_str != '':
        return bytes.decode(aes.decrypt(aes.make_dict_from_str(encode_str), settings.PASSWORD_AES))
    return ''


def encode_card_number(decode_str: str) -> str:
    if decode_str != '':
        return aes.make_str_from_dict(aes.encrypt(decode_str, settings.PASSWORD_AES))
    return ''

