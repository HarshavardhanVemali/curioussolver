from django.db import models

from phonenumbers import (
    PhoneNumber,
    parse,
    is_valid_number,
    format_number,
    PhoneNumberFormat,
)
from phonenumbers.phonenumberutil import NumberParseException

class PhoneNumberField(models.CharField):
    """
    Custom model field for storing and validating phone numbers.
    """

    def __init__(self, *args, region=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.region = region

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['region'] = self.region
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            return parse(value, self.region)
        except NumberParseException:
            return value

    def get_prep_value(self, value):
        if isinstance(value, PhoneNumber):
            return format_number(value, PhoneNumberFormat.E164)
        elif value is None:
            return value
        else:
            try:
                parsed_number = parse(value, self.region)
                if is_valid_number(parsed_number):
                    return format_number(parsed_number, PhoneNumberFormat.E164)
                else:
                    raise ValueError("Invalid phone number")
            except NumberParseException:
                raise ValueError("Invalid phone number")

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return str(value) if value else ''

class Register(models.Model):
    name=models.CharField(max_length=100,null=True)
    phone_number=PhoneNumberField(max_length=15, region='IN', null=True,unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
