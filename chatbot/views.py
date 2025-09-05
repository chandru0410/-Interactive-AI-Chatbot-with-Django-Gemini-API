import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Configure Gemini with your API key
genai.configure(api_key=settings.GEMINI_API_KEY)  # Ensure this key is defined in your settings

# Initialize the Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@csrf_exempt  # Only for development/testing — remove in production!
def chatbot_view(request):
    bot_response = ""

    if request.method == "POST":
        user_message = request.POST.get("message")

        if user_message:
            try:
                response = model.generate_content(user_message)
                bot_response = response.text

            except Exception as e:
                bot_response = f"Error: {str(e)}"

    return render(request, 'chatbot/chat.html', {"bot_response": bot_response})
