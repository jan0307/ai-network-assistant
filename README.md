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
## AWS Deployment

The AI Network Assistant was deployed to AWS using an EC2 instance running Ubuntu 24.04 LTS in the Europe (Stockholm) region.

Terraform was used to create the AWS infrastructure, including:

- EC2 t3.micro instance
- Security Group
- SSH access on port 22 restricted to my IP address
- HTTP access on port 80

The application was cloned from GitHub to the EC2 server.

The server uses:

- Nginx as the web server and reverse proxy
- Gunicorn as the WSGI application server
- Flask for the web application
- Google Gemini API for AI-generated network troubleshooting

The request flow is:

User → Internet → AWS EC2 → Nginx → Gunicorn → Flask → Gemini API

Gunicorn runs as a systemd service so the application continues running after the SSH session is closed.

## Deployment Testing

The application was tested directly on the EC2 server using curl before being tested from an external web browser.

The following parts were verified:

- Flask application started successfully
- Gunicorn served the Flask application
- Nginx forwarded HTTP traffic to Gunicorn
- The website was accessible through the EC2 public IP address
- The Gemini API returned network troubleshooting responses
- The application continued running after the SSH session was closed

## Deployment Problem and Solution

During deployment, the website initially returned an HTTP 500 Internal Server Error when an AI request was submitted.

The Gunicorn logs showed a `WORKER TIMEOUT` error. The Gemini API request sometimes required more time than Gunicorn's default timeout.

To verify the cause, the Gemini function was tested directly from Python on the EC2 server. The AI returned a valid response, confirming that the API key and Gemini integration were working.

The Gunicorn timeout was increased to 120 seconds:

`--timeout 120`

After this change, the AI responses worked correctly through the public website.

This troubleshooting process helped verify each layer separately and identify that the problem was the application server timeout rather than Flask, Nginx, or the Gemini API configuration.