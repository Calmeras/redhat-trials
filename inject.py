from PIL import Image

img = Image.open("photo1.png").convert("RGB")
    
with open("payload.bin", "rb") as f:
    payload = f.read()
    
pixels = img.load()
width, height = img.size
idx = 0
    
for y in range(height):
    for x in range(width):
        if idx < len(payload):
            r, g, b = pixels[x, y]
                # On remplace la valeur Rouge par l'octet du virus
            pixels[x, y] = (payload[idx], g, b)
            idx += 1
    
img.save("photofinal.png")
print("Termine! le fichier photofinal.png est pret")
