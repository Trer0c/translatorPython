from googletrans import Translator
translator = Translator()

input_str = "Hello world"

english = translator.translate(input_str, dest='en').text
print("English: " + english)

german = translator.translate(input_str, dest='de').text
print("German: " + german)

italian = translator.translate(input_str, dest='it').text
print("Italian: " + italian)

french = translator.translate(input_str, dest='fr').text
print("French: " + french)

swedish = translator.translate(input_str, dest='sv').text
print("Swedish: " + swedish)

portuguese = translator.translate(input_str, dest='pt').text
print("Portuguese: " + portuguese)
