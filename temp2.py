import datetime

from googleapiclient.discovery import build
import google.oauth2.credentials
import google_auth_oauthlib.flow


flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    './.credentials/credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar'])

flow.redirect_uri = 'https://www.example.com/oauth2callback'


def find_event_id_to_title(calendar_id):
  """Finds the event ID to title in Google Calendar.

  Args:
    calendar_id: The ID of the calendar to search.

  Returns:
    A dictionary of event IDs to titles.
  """

  service = build('calendar', 'v3', credentials=google.oauth2.credentials.Credentials.from_authorized_user_file('./.credentials/credentials.json'))

  # Get a list of all events in the calendar.
  events = service.events().list(calendarId=calendar_id).execute()

  # Create a dictionary of event IDs to titles.
  event_id_to_title = {}
  for event in events['items']:
    event_id = event['id']
    event_title = event['summary']
    event_id_to_title[event_id] = event_title

  return event_id_to_title


if __name__ == '__main__':
  # Get the ID of the calendar to search.
  calendar_id = 'primary'

  # Find the event ID to title in the calendar.
  event_id_to_title = find_event_id_to_title(calendar_id)

  # Print the event ID and the event title to the console.
  for event_id, event_title in event_id_to_title.items():
    print(f'{event_id}: {event_title}')