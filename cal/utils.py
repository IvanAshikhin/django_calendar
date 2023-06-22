from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super().__init__()

    # Formats a day as a td
    # Filters events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        events_html = ''
        for event in events_per_day:
            events_html += f'<li>{event.title}</li>'

        if day != 0:
            return f'<td><span class="date">{day}</span><ul class="event-list">{events_html}</ul></td>'
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for day, weekday in theweek:
            week += self.formatday(day, events)
        return f'<tr>{week}</tr>'

    # Formats a month as a table
    # Filters events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
