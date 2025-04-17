import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 






model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

Gender=input("Enter your Gender (Male/female/non binary): ")
Clothing_type=input("Enter your clothing type (e.g., athletic, lightweight, layered.): ")
age=input("Enter your age (e.g., 20): ")
height=input("Enter your height (In CM): ")


response = model.generate_content("Please suggest a casual summer outfit for a" +age+"-year-old" +Gender+ " who is " +height+ "cm tall and prefers "+Clothing_type+ ", trendy styles. Provide outfit details that focus on breathable fabrics and summer-appropriate colors.", )

print(response.text)