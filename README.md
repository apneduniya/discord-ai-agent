# Discord AI Agent

🤖 Meet our new AI made using [**composio**](https://www.composio.dev/) & [**crew AI**](https://docs.crewai.com/)! 🎉 This bot connects with your **Google Calendar**, making it a breeze to manage all your calendar activities right from _discord_. 💬🔗

<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## 📙 Features
You can scheduled events just by normal chatting with our bot and you can:

- **Create** events even by _adding someone via email, create google meeting room_ and all the neccessary features.
- **Find** upcoming events.
- **Update** & **Delete** existing events.
- **Create Quick** events.
- **Remove attendee** from an event

<br />

## 🤔 How I used composio?
**Composio** was very _crucial and reliable tool_ for making my project. It helped me to make my agentic tools for the agent **much more faster** and **in an easy way** acting like a **pipeline** between _agent_ and _google calendar_. It would really took me many more days if done without this 🔥.

<br />

## 🫳 Prerequisites
You should have

- Python 3.8 or higher
- GEMINI API KEY
- COMPOSIO API KEY
- Discord Bot Token
- And an [integration id](https://docs.composio.dev/api-reference/integrations/create-a-new-integration) from composio.

<br />

## 👣 Steps to Run
**Navigate to the Project Directory:**
Change to the directory where the `setup.sh`, `main.py`, `requirements.txt`, and `README.md` files are located. For example:
```shell
cd path/to/project/directory
```

### 1. Run the Setup File
Make the setup.sh Script Executable (if necessary):
On Linux or macOS, you might need to make the setup.sh script executable:
```shell
chmod +x setup.sh
```
Execute the setup.sh script to set up the environment, install dependencies, login to composio and 
add necessary tools:
```shell
./setup.sh
```
Now, Fill in the `.env` file with your secrets.

### 2. Run the python script
```shell
python3 main.py
```

<br />

## 🏛️ Project structure

```bash
utils
├── calendar.py
└── manage_events.py
.env.example
.gitignore
LICENSE
README.md
main.py
requirements.txt
setup.sh
tools.py
```

<br />

## 🤗 Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

<br />

## 🧾 License
This project is licensed under the [MIT License](LICENSE).

