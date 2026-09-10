# AI Network Assistant

AI Network Assistant is a web application that helps users troubleshoot common network problems using Generative AI.
## Features

- AI-powered network troubleshooting
- Simple web interface
- Provides step-by-step troubleshooting suggestions
- Handles common network problems such as DNS, IP addresses, connectivity, and router issues
## Technologies Used

- Python
- Flask
- Google Gemini API
- HTML
- CSS
- Git and GitHub
## Installation

Clone the repository:

```bash
git clone https://github.com/jan0307/ai-network-assistant.git
```

Go into the project directory:

```bash
cd ai-network-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```
## API Key Configuration

Create a `.env` file in the project directory and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is ignored by Git and should not be uploaded to GitHub.
## Running the Application

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Start the Flask application:

```powershell
flask --app app run
```

Open the following address in your web browser:

```text
http://127.0.0.1:5000
```
## Architecture

The application uses the following flow:

User → Web Browser → Flask Application → Gemini API → Flask Application → Web Browser
## Testing

The application was manually tested with several common network problems:

- DNS problem: The computer can ping 8.8.8.8 but not google.com.
- DHCP/APIPA problem: The computer receives a 169.254 IP address.
- Local network problem: The computer cannot ping the router.
- Internet connectivity problem: The computer has no internet connection.

All four tests produced relevant troubleshooting suggestions from the AI.
