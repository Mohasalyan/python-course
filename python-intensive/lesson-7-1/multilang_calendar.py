import calendar
import locale
from functools import wraps

def short_form(func):
    """Decorator to return abbreviated day names."""
    @wraps(func)
    def wrapper():
        return [day[:3] for day in func()]
    return wrapper

def translate(language):
    """Decorator to translate day names into a given language."""
    def decorator(func):
        @wraps(func)
        def wrapper():
            try:
                locale.setlocale(locale.LC_TIME, language)
                return [calendar.day_name[i] for i in range(7)]
            except locale.Error:
                return [f"Translation not available for {language}"]
        return wrapper
    return decorator

def get_data():
    """Returns full names of the days of the week."""
    return [calendar.day_name[i] for i in range(7)]

@short_form
def get_short_days():
    return get_data()

@translate("fr_FR")  # Example: French translation
def get_french_days():
    return get_data()

if __name__ == "__main__":
    print("Full days:", get_data())
    print("Short days:", get_short_days())
    print("French days:", get_french_days())
