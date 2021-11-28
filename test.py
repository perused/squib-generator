from PIL import Image, ImageColor
squib = Image.new(mode="RGB", size=(420, 420), color=(255, 255, 255))
squib.paste(im=Image.open("archive/white.png"), box=(0, 0, 420, 420))
squib.paste(im=Image.open("squibs/straight_squib/body.png"), box=(0, 0, 420, 420))
squib.save("archive/test.png")