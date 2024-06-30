from datetime import datetime
from gcsa.google_calendar import GoogleCalendar


calendar = GoogleCalendar('apneduniya.dontdisturb@gmail.com', credentials_path='./.credentials/credentials.json')

date = datetime.today().strftime("%Y-%m-%d")
timezone = datetime.now().astimezone().tzinfo

events = list(calendar.get_events(
    time_min=datetime(2024, 6, 30, 0, 0, 0),
    time_max=datetime(2024, 12, 31, 0, 0, 0),
    timezone=timezone.__str__(),
    query="temp"
))

for event in events:
    print(event.id)
    print(event.summary, "\n")


print("\nALL EVENTS:-")
events = list(calendar.get_events(
    time_min=datetime(2021, 6, 30, 0, 0, 0),
    time_max=datetime(2024, 12, 31, 0, 0, 0),
    timezone=timezone.__str__(),
))
for event in events:
    print(event.id)
    print(event.start)
    print(event.summary, "\n")

# print(calendar.get_event("_clr78ba8650mitaa89bj2prke9r4sha0clr6arjkecn6ot9edlgg"))

