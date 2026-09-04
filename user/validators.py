from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^09\d{9}$',
    message='شماره تماس باید با فرمت صحیح وارد شود'
)