import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAi8NHvMBWuc-k-DIdvo_0wwyUpqtTtoZQ")

models = genai.list_models()
for model in models:
    print(model.name)
