import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 






model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')




response = model.generate_content("Generate a winter outfit recommendation for a female user with a pear-shaped body who prefers sustainable fashion. The user is looking for lightweight fabrics that still provide warmth for cold weather. Please include details on eco-friendly materials and layering options.", )

print(response.text)