import pathlib
import textwrap

import google.generativeai as genai



from IPython.display import display   
from IPython.display import Markdown 

apikey="AIzaSyBYkCnr6h6YxXT_WM3Gk4vD0vVBy-SW9jY"

genai.configure(api_key=apikey) 
model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
imput=input("Please enter the prompt for your fashion recmandation:")



prompt= """ Provide fashion recmendtions based on these exampls:

Example 1
scnerio: Please suggest a casual summer outfit for a 20-year-old male who is 180 cm tall and prefers lightweight, trendy styles. Provide outfit details that focus on breathable fabrics and summer-appropriate colors.
recmentation: For a casual summer outfit, consider a lightweight, short-sleeve linen shirt in a light color like white or pastel. Pair it with tailored shorts in a complementary color, such as khaki or light blue. Opt for breathable sneakers or loafers in a neutral shade. Accessorize with sunglasses and a stylish watch. A canvas backpack can complete the look while keeping it trendy and functional.

example 2
scnerio: Generate a winter outfit recommendation for a female user with a pear-shaped body who prefers sustainable fashion. The user is looking for lightweight fabrics that still provide warmth for cold weather. Please include details on eco-friendly materials and layering options.
recmentation: For a winter outfit, consider a sustainable wool or organic cotton turtleneck sweater as a base layer. Pair it with high-waisted, wide-leg trousers made from recycled materials to balance the pear shape. Add a long, eco-friendly puffer coat for warmth, and opt for insulated ankle boots made from vegan leather. Accessorize with a recycled wool scarf and a beanie. Layering with a lightweight, breathable thermal top underneath the sweater can provide extra warmth without bulk.

example 3
scenerio: Recommend a formal outfit for a male user attending a business conference. The user prefers slim-fit suits and neutral colors. Please suggest a complete outfit, including accessories, that fits a professional setting.
recmentation: For a business conference, opt for a slim-fit charcoal grey suit with a crisp white dress shirt. Pair it with a matching slim tie in a subtle pattern or solid color. Choose polished black leather oxford shoes and a matching belt. Accessorize with a classic silver watch and cufflinks. A sleek leather briefcase can complete the professional look while keeping it functional for the conference.

example 4
scenerio: Provide a vacation wardrobe for a user going to a tropical beach holiday. The user enjoys casual, breathable outfits with vibrant colors. Include recommendations for sun protection and light, airy fabrics.
recmentation: For a tropical beach holiday, pack lightweight, breathable cotton or linen clothing. Start with a couple of vibrant, short-sleeve button-up shirts in tropical prints. Pair them with comfortable, loose-fitting shorts in light colors. Include a wide-brimmed straw hat for sun protection and polarized sunglasses. Lightweight sandals or flip-flops are perfect for the beach. Don't forget a light, airy cover-up for when you're not in the water. A beach tote made from recycled materials can hold all your essentials while keeping the look casual and fun.

example 5
scenerio: Recommend a traditional outfit for a female user attending a cultural festival. The user prefers elegant and minimalistic styles. Please include recommendations for appropriate accessories and footwear.
recmentation: For a cultural festival, consider an elegant, minimalistic traditional outfit like a long, flowing kurta or anarkali in a solid color or subtle print. Pair it with palazzo pants or a long skirt for comfort and style. Accessorize with delicate gold or silver jewelry, such as stud earrings and a simple bracelet. Opt for comfortable yet stylish juttis or sandals that complement the outfit. A lightweight dupatta can add an extra touch of elegance while keeping the look minimalistic and sophisticated.

Example 6
Scnerio:A male with a skinny body wearing a blue shirt to a formal meeting. The user wants a creative look, while also being polished enough to be among the people in the formal meeting. 
recmentation: For a formal meeting, consider a well-fitted blue dress shirt made from breathable cotton or a cotton blend. Pair it with tailored charcoal grey trousers to create a sophisticated look. Opt for polished black leather loafers or oxfords to elevate the outfit. Accessorize with a slim black leather belt and a classic wristwatch. A lightweight blazer in a complementary color can add an extra layer of sophistication while keeping the overall look polished and professional.

Example 7
Scenerio: a woman with a curvy body wearing a red dress for a summer wedding. The user prefers a romantic and elegant style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.
recmentation: For a summer wedding, you can pair a red dress with nude or metallic heels. Add a light shawl or wrap in a neutral color to keep warm in the evening. Accessorize with gold or silver jewelry, and consider a clutch bag that complements the dress. A floral headband or hairpiece can add a touch of whimsy to your look.

Example 8
scenerio: A male with an athletic and tall body wearing chino pants to a summer festival. The user prefers a casual and trendy style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.
recmentation: For a summer festival, consider pairing lightweight chino pants in a light color with a short-sleeve, patterned button-up shirt. Opt for breathable sneakers or casual loafers to keep the look trendy and comfortable. Accessorize with a stylish watch and sunglasses. A lightweight denim jacket can be added for cooler evenings, while a canvas backpack can hold essentials while keeping the outfit casual and functional.

Example 9
scenerio: a male with a muscular body wearing a black t-shirt to a casual outing. The user prefers a sporty and trendy style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.
recmentation: For a casual outing, consider pairing a fitted black t-shirt with lightweight, breathable joggers or shorts in a complementary color. Opt for trendy sneakers or slip-on shoes for comfort and style. Accessorize with a sporty watch and sunglasses. A lightweight bomber jacket can be added for cooler evenings, while a crossbody bag can keep your essentials handy without compromising the sporty look.

Example 10
scenerio: A woman with a skinny and short body wearing a floral dress to a summer picnic. The user prefers a casual and trendy style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.
recmentation: For a summer picnic, consider a lightweight, floral sundress that flatters your figure. Pair it with comfortable espadrilles or sandals in a neutral color. Accessorize with a wide-brimmed straw hat and sunglasses for sun protection. A light denim jacket can be added for cooler evenings, while a crossbody bag can keep your essentials handy without compromising the casual look.
example 11
scenerio:"""


response =  model.generate_content(prompt+imput, generation_config=genai.types.GenerationConfig(temperature=0.7))
print (response.text )