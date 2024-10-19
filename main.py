text_format = lambda text: text.replace("\n", "").replace("\t", "").replace("\xa0", " ")


a = "dfdf\tdfgdg\n dgdg"
print(text_format(a))
