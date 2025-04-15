import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

# ✅ Configure your Gemini API key
genai.configure(api_key="AIzaSyCS0EGCycFs8HHSyZGNGW_4ucl3Yd3DHFA")

model = genai.GenerativeModel("models/gemini-1.5-pro")

# 🔹 Main chat UI
def chat_page(request):
    return render(request, 'chat.html')

# 🔹 POST endpoint for chat messages
@csrf_exempt
def gemini_chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get("message", "")
        try:
            response = model.generate_content(prompt)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"})

# 🔹 Optional: View supported models
@csrf_exempt
def list_models(request):
    try:
        models = genai.list_models()
        model_list = [
            {
                "name": model.name,
                "methods": model.supported_generation_methods
            }
            for model in models
        ]
        return JsonResponse({"models": model_list})
    except Exception as e:
        return JsonResponse({"error": f"Error: {str(e)}"})

# 🔹 Optional Chatpanel (secondary UI)
def Chatpanel(request):
    return render(request, 'Chatpanel.html')
def chat_page(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []
    return render(request, 'chat.html')

@csrf_exempt
def gemini_chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get("message", "")
        try:
            response = model.generate_content(prompt)
            reply = response.text

            history = request.session.get('chat_history', [])
            history.append({"user": prompt, "bot": reply})
            request.session['chat_history'] = history
            request.session.modified = True

            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"})
