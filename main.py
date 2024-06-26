import os
import dotenv
from datetime import datetime
from crewai import Agent, Task
from composio_crewai import App, ComposioToolSet
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the environment variables
dotenv.load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1, google_api_key=GOOGLE_API_KEY)

composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(apps=[App.GOOGLECALENDAR])

date = datetime.today().strftime("%Y-%m-%d")
timezone = datetime.now().astimezone().tzinfo

todo = """
On 27th June
    9AM - 12PM -> Learn something,
    1PM - 3PM -> Code,
    5PM - 7PM -> Meeting,
    8PM - 10PM -> Game
"""

def run_crew():
    calendar_agent = Agent(
        role="Google Calendar Agent",
        goal="""You take action on Google Calendar using Google Calendar APIs""",
        backstory="""You are an AI agent responsible for taking actions on Google Calendar on users' behalf.
        You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set.""",
        verbose=True,
        tools=tools,
        llm=llm,
    )

    def log_response(response):
        with open('calendar_response.log', 'a') as f:
            f.write(str(response) + '\n')

    task = Task(
        description=f"Book slots according to \n {todo}. Label them with the work provided to be done in that time period. Schedule it for given date. Today's date is {date} and make the timezone be {timezone}.",
        agent=calendar_agent,
        expected_output="Successfully create all events",
        on_result=log_response,
    )

    task.execute()
    return "Crew run initiated", 200

run_crew()