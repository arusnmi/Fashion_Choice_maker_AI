import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 






model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')




response = model.generate_content("Recommend a traditional outfit for a female user attending a cultural festival. The user prefers elegant and minimalistic styles. Please include recommendations for appropriate accessories and footwear.", )

print(response.text)