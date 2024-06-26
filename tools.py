from crewai_tools import tool
import requests
import dotenv
import os


# Load the environment variables
dotenv.load_dotenv()

COMPOSIO_API_KEY = os.environ["COMPOSIO_API_KEY"] # Get the API key from composio


@tool("Create Event")
def create_event(connectedAccountId: str, start_datetime: str, end_datetime: str, title: str, description: str | None = "") -> str:
    """
        Create a new event in a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required start_datetime: The start date and time of the event in ISO 8601 format.
        :param required end_datetime: The end date and time of the event in ISO 8601 format.
        :param required title: The title of the event.
        :param optional description: The description of the event.
    """

    print("\n\nCreating event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_create_event/execute"

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": {
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "summary": title,
            "description": description
        }
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    
    if response.status_code == 200:
        return "Event created successfully"
    else:
        if response_json.response.error.code == 401:
            return "Your account's authentication credentials is expired. Please re authenticate again by using `!authenticate` command."
        return "Failed to create event"
    

@tool("Find Events")
def find_events(connectedAccountId: str, query: str | None = "", max_results: int | None = "", time_max : str | None = "", time_min : str | None = "", event_types: str | None = "", calendar_id: str | None = "") -> str:
    """
        Find events in a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param optional query: The search query for events.
        :param optional max_results: The maximum number of events to return.
        :param optional time_max: The maximum time for the event.
        :param optional time_min: The minimum time for the event.
        :param optional event_types: The type of events to search for.
        :param optional calendar_id: The ID of the calendar to search in.
    """

    print("\n\nFinding events\n\n")
    
    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_find_event/execute"

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": {
            "query": query,
            "max_results": max_results,
            "time_max": time_max,
            "time_min": time_min,
            "event_types": event_types,
            "calendar_id": calendar_id
        }
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        return "Failed to find events"
    

@tool("Delete Event")
def delete_event(connectedAccountId: str, event_id: str, calendar_id: str | None = ""):
    """
        Delete an event from a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required event_id: The ID of the event to delete.
        :param optional calendar_id: The ID of the calendar to delete the event from.
    """

    print("\n\nDeleting event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_delete_event/execute"

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": {
            "event_id": event_id,
            "calendar_id": calendar_id
        }
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return "Event deleted successfully"
    else:
        print(response.json())
        return "Failed to delete event"
    

@tool("Update Event")
def update_event(connectedAccountId: str, event_id: str, start_datetime: str | None = "", end_datetime: str | None = "", title: str | None = ""):
    """
        Update an existing event in a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required event_id: The ID of the event to update.
        :param optional start_datetime: The new start date and time of the event in ISO 8601 format.
        :param optional end_datetime: The new end date and time of the event in ISO 8601 format.
        :param optional title: The new title of the event.
    """

    print("\n\nUpdating event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_update_event/execute"

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": {
            "event_id": event_id,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "title": title
        }
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return "Event updated successfully"
    else:
        print(response.json())
        return "Failed to update event"


@tool("Remove Attendee from Event")
def remove_attendee_event(event_id: str, attendee_email: str, calendar_id: str | None = ""):
    """
        Remove an attendee from an existing event in a Google Calendar.
        :param required event_id: The ID of the event.
        :param required attendee_email: The email of the attendee to remove.
        :param optional calendar_id: The ID of the calendar to remove the attendee from.
    """

    print("\n\nRemoving attendee from event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_remove_attendee/execute"

    payload = {
        "input": {
            "event_id": event_id,
            "attendee_email": attendee_email,
            "calendar_id": calendar_id
        }
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    
