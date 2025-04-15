import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)



model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

