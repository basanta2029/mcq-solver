from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_secrets import API_KEY
# Create your views here.

import openai

openai.api_key=API_KEY


@api_view(['GET'])
def home(request):
    p = '''How many millimeters make ten kilometers?
    A) 1010	B) 109
    C) 108	D) 107'''

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = "Also Explain why {}".format(p),
        temperature=0.7,
        max_tokens=200,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0,
        )
    choices=response["choices"]
    resp=choices[0]["text"]
    print(resp)
    return Response(response)