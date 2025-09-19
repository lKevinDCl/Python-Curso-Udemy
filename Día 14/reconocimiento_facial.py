import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

# Pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control,cv2.COLOR_BGRA2BGR)
FOTO_PRUEBA = cv2.cvtColor(foto_prueba,cv2.COLOR_BGRA2BGR)

# localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# localizar cara control
lugar_cara_B = fr.face_locations(foto_control)[0]
cara_codificada_B = fr.face_encodings(foto_control)[0]

# mostrar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0,255,0),
              2)

# mostrar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0,255,0),
              2)

# realizar comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B, 0.3)

# medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,225,0),
            2)


# mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)


# mantener programa abierto
cv2.waitKey(0)