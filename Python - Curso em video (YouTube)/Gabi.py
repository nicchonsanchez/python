import openai as ia

ia.api_key = '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'
request = input('Descreva a imagem a ser gerada: ')
text = "Mulher mais linda do mundo"
link = "https://scontent-gru2-2.cdninstagram.com/v/t51.2885-15/54247902_2070250773043643_6498298435216688687_n.jpg?stp=dst-jpg_e35_p720x720&_nc_ht=scontent-gru2-2.cdninstagram.com&_nc_cat=111&_nc_ohc=4QDf7xzRoQ8AX_Pt6CJ&edm=ACWDqb8BAAAA&ccb=7-5&ig_cache_key=MjAwOTY0MjQ4ODM0MDc0ODM1MA%3D%3D.2-ccb7-5&oh=00_AfBdEiacU_9mw71w71qdLuVh3vdW641CeX1CncAPPsunwg&oe=650116FE&_nc_sid=ee9879"
if request == text:
    print(f'URL da imagem gerada: \n{link}')
else:
    response = ia.Image.create(
        prompt = request,
        n=1,
        size="1024x1024"
    )
    imagem_url = response['data'][0]['url']
    print(f'URL da imagem gerada: \n{imagem_url}')
