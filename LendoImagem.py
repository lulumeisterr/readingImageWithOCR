from PIL import Image
from PIL import ImageEnhance
import pytesseract as ocr
import csv


class ImageReading:

	def __init__(self,url,urlTratamento):

		self.url = url
		self.CaptureURL = urlTratamento
		self.newImage = ''

	def ReconfigurandoImagem(self):

		im = Image.open(self.url)
		nx , ny = im.size
		im = im.resize((int(nx*7),int(ny*7)), Image.BICUBIC)
		enh = ImageEnhance.Contrast(im)

		enh.enhance(1.6).show('30% more Contrast')

		imgx = im;
		imgx = imgx.convert("RGBA")

		return imgx.save(self.CaptureURL)

	def LendoImagem(self):
		self.newImage = ocr.image_to_string(Image.open(self.CaptureURL))

		with open('/home/lucasn/Desktop/ReportsError.csv', 'w') as csvfile:
   			spamwriter = csv.writer(csvfile)
    			spamwriter.writerow(self.newImage.encode('utf-8').strip())
    		csvfile.close()

		return self.newImage


Reading = ImageReading('/home/lucasn/Desktop/exame.jpg','/home/lucasn/Desktop/exame4.png')
#print(Reading.ReconfigurandoImagem())
print(Reading.LendoImagem())

#ReadingNewImage = ImageReading('/home/lucasn/Desktop/exame3.png')
#print(ReadingNewImage.LendoImagem())



















