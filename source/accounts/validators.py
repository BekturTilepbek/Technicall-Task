from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_password(value):
    errors = []

    if len(value) < 8:
        errors.append('Password must be at least 8 characters long.')

    if not any(char.isalpha() for char in value):
        errors.append('Password must contain at least one letter.')

    if not any(char.isdigit() for char in value):
        errors.append('Password must contain at least one number.')

    special_chars = ["@", "$", "!", "%", "*", "?", "&"]
    if not any(char in value for char in special_chars):
        errors.append('Password must contain at least one special character (@, $, !, %, *, ?, &).')

    forbidden_words = ['password', '123456', 'qwerty']
    if any(word in value.lower() for word in forbidden_words):
        errors.append('Password is too weak. Avoid using common passwords.')

    if errors:
        raise ValidationError(errors)

    return value


def validate_username(value):
    errors = []

    if not any(char.isalpha() for char in value):
        errors.append('Username must contain at least one letter.')

    if not any(char.isdigit() for char in value):
        errors.append('Username must contain at least one number.')

    if len(value) < 4:
        errors.append('Username must be at least 4 characters long.')

    if User.objects.filter(username=value).exists():
        errors.append('Username is already taken.')

    if errors:
        raise ValidationError(errors)

    return value
