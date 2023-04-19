from Flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.datetime.today()
    day_of_week = today.strftime("%A")
    is_weekday = "будній" if today.weekday() < 5 else "вихідний"
    ukrainian_days = {
        "Monday": "Понеділок",
        "Tuesday": "Вівторок",
        "Wednesday": "Середа",
        "Thursday": "Четвер",
        "Friday": "П'ятниця",
        "Saturday": "Субота",
        "Sunday": "Неділя"
    }
    ukr_day_of_week = ukrainian_days[day_of_week]

    return f"Сьогодні {today.date()} ({ukr_day_of_week}) і це {is_weekday} день"

if __name__ == '__main__':
    app.run(debug=True)
