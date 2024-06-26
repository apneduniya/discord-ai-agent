from crewai_tools import tool
import requests
import dotenv
import os


# Load the environment variables
dotenv.load_dotenv()

# Get the API key from composio
COMPOSIO_API_KEY = os.environ["COMPOSIO_API_KEY"]


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

    if response_json["executed"]:
        return "Created the event successfully!"

    elif not response_json["executed"]:
        if int(response_json["response"]["error"]["code"]) == 401:
            return "Your account's authentication credentials is expired. Please re authenticate again by using `!authenticate` command."

        return "Something went wrong in creating the event."

    else:
        return "Failed to create event"


@tool("Find Events")
def find_events(connectedAccountId: str, query: str | None = None, max_results: int | None = None, time_max: str | None = None, time_min: str | None = None, event_types: str | None = None, calendar_id: str | None = None) -> str:
    """
        Find events in a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param optional query: Search terms to find events that match these terms in the event's summary, description, location, attendee's displayName, attendee's email, organizer's displayName, organizer's email, etc if needed.
        :param optional max_results: The maximum number of events to return.
        :param optional time_max: The maximum time for the event.
        :param optional time_min: Lower bound (exclusive) for an event's end time to filter by. Must be an RFC3339 timestamp with mandatory time zone offset.
        The start of the interval for the query formatted as per RFC3339.
        :param optional event_types: Event types to return. Acceptable values are 'default', 'focusTime', 'outOfOffice', 'workingLocation'.
        :param optional calendar_id: The ID of the calendar to search in.
    """

    print("\n\nFinding events\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_find_event/execute"

    # Build the input dictionary dynamically
    input_data = {}
    if query is not None:
        input_data["query"] = query
    if max_results is not None:
        input_data["max_results"] = max_results
    if time_max is not None:
        input_data["time_max"] = time_max
    if time_min is not None:
        input_data["time_min"] = time_min
    if event_types is not None:
        input_data["event_types"] = event_types
    if calendar_id is not None:
        input_data["calendar_id"] = calendar_id

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": input_data
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(payload, "\n\n")
    print(response.json())
    response_json = response.json()

    if response_json["executed"]:
        events = response_json["response"]["event_data"]
        if events:
            event_list = [event["summary"] for event in events]
            return f"Found events: {', '.join(event_list)}"
        else:
            return "No events found"
    else:
        if int(response_json["response"]["error"]["code"]) == 401:
            return "Your account's authentication credentials is expired. Please re authenticate again by using `!authenticate` command."

        return "Something went wrong in finding the event."


@tool("Delete Event")
def delete_event(connectedAccountId: str, event_id: str, calendar_id: str | None = None):
    """
        Delete an event from a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required event_id: The ID of the event to delete.
        :param optional calendar_id: The ID of the calendar to delete the event from.
    """

    print("\n\nDeleting event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_delete_event/execute"

    # Build the payload
    input_data = {
        "event_id": event_id
    }
    if calendar_id is not None:
        input_data["calendar_id"] = calendar_id

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": input_data
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    if response_json["executed"]:
        return "Event deleted successfully"
    else:
        if int(response_json["response"]["error"]["code"]) == 401:
            return "Your account's authentication credentials is expired. Please re authenticate again by using `!authenticate` command."

        return "Something went wrong in deleting the event."


@tool("Update Event")
def update_event(connectedAccountId: str, event_id: str, start_datetime: str | None = None, end_datetime: str | None = None, title: str | None = None, description: str | None = None):
    """
        Update an existing event in a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required event_id: The ID of the event to update.
        :param optional start_datetime: The new start date and time of the event in ISO 8601 format.
        :param optional end_datetime: The new end date and time of the event in ISO 8601 format.
        :param optional title: The new title of the event.
        :param optional description: The new description of the event.
    """

    print("\n\nUpdating event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_update_event/execute"

    # Build the payload
    input_data = {
        "event_id": event_id
    }
    if start_datetime is not None:
        input_data["start_datetime"] = start_datetime
    if end_datetime is not None:
        input_data["end_datetime"] = end_datetime
    if title is not None:
        input_data["title"] = title
    if description is not None:
        input_data["description"] = description

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": input_data
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    if response_json["executed"]:
        return "Event updated successfully"
    else:
        if int(response_json["response"]["error"]["code"]) == 401:
            return "Your account's authentication credentials is expired. Please re authenticate again by using `!authenticate` command."

        return "Something went wrong in updating the event."


@tool("Remove Attendee from Event")
def remove_attendee_event(connectedAccountId: str, event_id: str, attendee_email: str, calendar_id: str | None = None):
    """
        Remove an attendee from an existing event in a Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required event_id: The ID of the event.
        :param required attendee_email: The email of the attendee to remove.
        :param optional calendar_id: The ID of the calendar to remove the attendee from.
    """

    print("\n\nRemoving attendee from event\n\n")

    url = "https://backend.composio.dev/api/v1/actions/googlecalendar_remove_attendee/execute"

    # Build the payload
    input_data = {
        "event_id": event_id,
        "attendee_email": attendee_email
    }

    if calendar_id is not None:
        input_data["calendar_id"] = calendar_id

    payload = {
        "connectedAccountId": connectedAccountId,
        "appName": "googlecalendar",
        "input": input_data
    }

    headers = {
        "X-API-Key": COMPOSIO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()

    if response_json["executed"]:
        return "Attendee removed successfully"
    else:
        if int(response_json["response"]["error"]["code"]) == 401:
            return "Your account's authentication credentials is expired. Please re authenticate again by using `!authenticate` command."

        return "Something went wrong in removing the attendee from the event."
    
