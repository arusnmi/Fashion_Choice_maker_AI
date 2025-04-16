import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 






model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

Gender=input("Enter your Gender (Male/female/non binary): ")
body_type=input("Enter your body type (e.g., athletic, curvy, etc.): ")
outfit_type=input("Enter the type of outfit you want (e.g., casual, formal, etc.): ")
occasion=input("Enter the occasion (e.g., wedding, party, etc.): ")
Clothing=input("Enter the type of cloths that you want to style, eg(chino pants, shirt): ")

response = model.generate_content("What would go with a "+Clothing+" for a "+occasion+" that  is "+outfit_type+" on a "+Gender+" "+body_type+" body type?")

print(response.text)