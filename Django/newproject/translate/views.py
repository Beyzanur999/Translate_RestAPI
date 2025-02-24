from django.shortcuts import render
from googletrans import Translator

def translate_text(request):
    translated_text = ""
    
    if request.method == "POST":
        text = request.POST.get("text")
        target_language = request.POST.get("target_language")

        if text and target_language:
            translator = Translator()
            translation = translator.translate(text, dest=target_language)
            translated_text = translation.text

    return render(request, "translate/index.html", {"translated_text": translated_text})
