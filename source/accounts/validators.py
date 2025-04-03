from django.core.exceptions import ValidationError

class DigitValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру.", code="password_no_digit")


class UppercaseValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError("Пароль должен содержать хотя бы одну заглавную букву.", code="password_no_upper")
