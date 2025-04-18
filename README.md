# Fashion_Choice_maker_AI



This repository contains my AI fashion recommender



# Problem statement

the problem with current fashion recommender is that mst of them have a finite selection of random fashion options that are prompted when giving a sugestion and it usualy is nt good. The way it is done normaly is that there is a database of random diffrent outfit choices, and when prompted for a choice, it reads the keywords from the text and then gives a list of sugestions to the user. this lead to it being finite and taking a lot of resources to not make it finite. the only other soloution that i researched is that there could be physical assisastiants be there 24/7 to give fashion recmendations, but that thakes time and resources. 


# Inisights

During my research i actuly found a lot of models that are doing the same thing, where they use AI like machilne learning to make fasion choices, as the indrustery has recgnoized the problem already and is activly triying to fix it. 




# Model- selected and hypeerprameater tuning;

for my model usen in the task i used gemini 2.5 pro exp, s i tought that it would give the best resualts. for hyperprameater tuning, i addjusted the temppture to be optmal to give a detailed response as i did not eant it to devate from the example prompts. 

# Prompts i fead into the model

the prompts i fed intot h model are: 
* A male with a skinny body wearing a blue shirt to a formal meeting. The user wants a creative look, while also being polished enough to be among the people in the formal meeting. 


*a woman with a curvy body wearing a red dress for a summer wedding. The user prefers a romantic and elegant style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.

*  A male with an athletic and tall body wearing chino pants to a summer festival. The user prefers a casual and trendy style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.

* A male with an athletic and tall body wearing chino pants to a summer festival. The user prefers a casual and trendy style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.

*A woman with a skinny and short body wearing a floral dress to a summer picnic. The user prefers a casual and trendy style, with a focus on lightweight fabrics and summer colors. Please include recommendations for shoes, accessories, and any additional layers for evening wear.


# Model- simulation and resualts

the simulated input prompt is-i want a recmendation for a male with a bubly body that is wearing a yellow shit to a lecture

the response-For attending a lecture, pair the yellow shirt with comfortable, well-fitting trousers in a neutral, darker color like navy blue or charcoal grey. Opt for a straight-leg or relaxed-fit chino or corduroy pant to ensure comfort and a flattering silhouette for a bubbly body type. Choose comfortable yet smart footwear such as clean, minimalist sneakers, loafers, or desert boots in a color like brown, navy, or grey. If needed, layer with a lightweight, unstructured blazer or a simple cardigan in a complementary neutral shade (like grey or navy) for a more polished look that doesn't add bulk. Keep accessories minimal; a simple watch and a belt that matches your shoes would suffice. Ensure the yellow shirt fits well – not too tight across the midsection – for optimal comfort during the lecture.

 THe AI did exceptonaly well because it made the prompt very detailed and to the point, it followed te exampe prompts very well and gave a prargraph answer instead of a big answer. usualy,  the model would list down some technacil jargon, but after some twealing, it finaly made a good model. 
# Sources- analysis

https://ieeexplore.ieee.org/document/10275967
https://www.researchgate.net/publication/381448625_Generative_AI-based_Style_Recommendation_Using_Fashion_ItemDetection_and_Classification
https://ieeexplore.ieee.org/iel8/6287639/10380310/10565860.pdf
https://arxiv.org/html/2402.17279v3
https://www.diva-portal.org/smash/get/diva2:1603327/FULLTEXT01.pdf
https://link.springer.com/article/10.1007/s42979-023-01932-9

