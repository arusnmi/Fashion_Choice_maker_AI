import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 






model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')




response = model.generate_content("Provide a vacation wardrobe for a user going to a tropical beach holiday. The user enjoys casual, breathable outfits with vibrant colors. Include recommendations for sun protection and light, airy fabrics.", )

print(response.text)