texto = ["Alicante", "Arándano", "Barcelona", "Banano", "Cartagena", "Cereza", "Doha", "Durazno", "Edimburgo", "Endrina", "Florencia", "Frambuesa", "Granada", "Guanábana", "Helsinki", "Higo", "Ibagué", "Ica"]

for palabra in texto:
    letras_iniciales = palabra[:3] 
    longitud = len(palabra)
    
    if longitud > 6:
        print(f"Su palabra es: {palabra}")
        print(f"Sus tres primeras letras son: {letras_iniciales}")
        print(f"Longitud: {longitud}\n")
    else:
        print(f"Palabra corta: {palabra}\n")