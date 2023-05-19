from django.core.exceptions import ValidationError


def validate_years_of_experience(years_of_experience):
    if years_of_experience < 0:
        raise ValidationError("Years of experience can't be less than 0")
    elif years_of_experience > 100:
        raise ValidationError(
            "You can't be this old :) " "Years of experience can't be more than 100"
        )

    return years_of_experience
