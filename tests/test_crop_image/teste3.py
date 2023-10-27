from PIL import Image

image_pillow = Image.open('imagem.jpeg')

x = 100
y = 154
width = 1400
height = 592

cropped_image_pillow = image_pillow.crop((x, y, x + width, y + height))

cropped_image_pillow.save('recorte_imagem.jpeg')

print("Imagem recortada e salva com sucesso!")
