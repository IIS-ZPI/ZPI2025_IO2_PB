from datetime import datetime


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True

    except:
        return False