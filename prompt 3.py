import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 






model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')




response = model.generate_content( "Recommend a formal outfit for a male user attending a business conference. The user prefers slim-fit suits and neutral colors. Please suggest a complete outfit, including accessories, that fits a professional setting.", )

print(response.text)