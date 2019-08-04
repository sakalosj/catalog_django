from django import forms
from django.core.validators import RegexValidator
from django.forms import CharField

from album.widgets import ImageWidget, ImageWidget2


class PictureFields(forms.MultiValueField):
    # def __init__(self, *args, **kwargs):
    #     fields = (
    #         forms.CharField(max_length=128, required=False),
    #         forms.CharField(max_length=128, required=False),
    #     )
    #     super().__init__(fields, *args, **kwargs)
        # self.widget = PictureWidget
    widget = ImageWidget2

    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
                ],
            ),
            CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
            ),
        )
        super().__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return '|'.join(data_list)

