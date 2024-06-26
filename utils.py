import os
import dotenv
from datetime import datetime
from crewai import Agent, Task
# from composio_crewai import App, ComposioToolSet
from langchain_google_genai import ChatGoogleGenerativeAI


# Load the environment variables
dotenv.load_dotenv()
google_api_key = os.environ["GOOGLE_API_KEY"] # Google API Key

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1, google_api_key=google_api_key)

# composio_toolset = ComposioToolSet()
# tools = composio_toolset.get_tools(apps=[App.GOOGLECALENDAR])

date = datetime.today().strftime("%Y-%m-%d")
timezone = datetime.now().astimezone().tzinfo


def manage_events(connectedAccountId: str, prompt: str) -> str:
    """
        Run the crew to manage events in Google Calendar.
        :param required connectedAccountId: The ID of the connected account.
        :param required prompt: The prompt for the crew to follow.
    """

    response = ""

    calendar_agent = Agent(
        role="Google Calendar Agent",
        goal="""You take action on Google Calendar using Google Calendar APIs""",
        backstory="""You are an AI agent responsible for taking actions on Google Calendar on users' behalf.
        You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set.""",
        verbose=True,
        llm=llm,
    )

    def log_response(response):
        response += f"\n{response}"

    task = Task(
        description=f"""Manage events in Google Calendar based on: \n {prompt} \n 
        Schedule it for given date. Today's date is {date} and make the timezone be {timezone}.
        The connected account ID (connectedAccountId) is {connectedAccountId}.
        """,
        agent=calendar_agent,
        expected_output="Successfully scheduled the events",
        on_result=log_response,
    )

    task.execute()
    if response:
        return response
    else:
        print(response)
        return "Failed to schedule the events"