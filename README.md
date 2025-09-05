# -Interactive-AI-Chatbot-with-Django-Gemini-API
An interactive AI-powered chatbot built with Django and integrated with the Google Gemini API.
This project demonstrates how to create a conversational chatbot interface using Django as the backend framework and Gemini API as the AI model.

🚀 Features

Django-based web application with modular app structure

Integration with Google Gemini API for AI-driven responses

Simple and interactive chat UI

Scalable architecture for further enhancements

Easy to configure and deploy

📂 Project Structure
Interactive-AI-Chatbot-with-Django-Gemini-API/
│
├── core/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── chatbot/            # Main chatbot app
│   ├── views.py        # Chatbot logic
│   ├── urls.py         # Chat routes
│   ├── models.py       # (Optional) Store chat history
│   └── templates/      # Frontend HTML templates
│
├── manage.py
└── README.md

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/chandru0410-Jayachandran_k/Interactive-AI-Chatbot-with-Django-Gemini-API.git
cd Interactive-AI-Chatbot-with-Django-Gemini-API

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the root directory and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

5. Run Database Migrations
python manage.py migrate

6. Start the Development Server
python manage.py runserver


Now open your browser and go to:
👉 http://127.0.0.1:8000/chatbot/
