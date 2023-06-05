import easyocr
reader = easyocr.Reader(['en'], gpu=False)  # this needs to run only once to load the model into memory
result = reader.readtext('0Jl54.png', detail=0)
print(result)