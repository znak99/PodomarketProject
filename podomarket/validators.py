import string
from django.core.exceptions import ValidationError

# value에 특수문자가 있는지 확인
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False

# value에 영문 대문자가 있는지 확인
def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False

# value에 영문 소문자가 있는지 확인
def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False

# value에 숫자가 있는지 확인
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("記号は使えません。")

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) 
        ):
            raise ValidationError("8文字以上のアルファベット大・小文字、数字")

    def get_help_text(self):
        return "8文字以上のアルファベット大・小文字、数字"