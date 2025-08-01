import os
os.environ['QT_QPA_PLATFORM'] = 'xcb'

import sounds
import cv2
import mediapipe as mp
import pygame

mp_manos = mp.solutions.hands
mp_dibujo = mp.solutions.drawing_utils
mp_estilos_dibujo = mp.solutions.drawing_styles

pygame.init()  #Ruta a tu carpeta de sonidos
sonidos = [
    pygame.mixer.Sound('sounds/#do.WAV'),   # 0 - Mano 1, Dedo 1 (Índice)
    pygame.mixer.Sound('sounds/re.WAV'),    # 1 - Mano 1, Dedo 2 (Medio)
    pygame.mixer.Sound('sounds/#fa.WAV'),   # 2 - Mano 1, Dedo 3 (Anular)
    pygame.mixer.Sound('sounds/#sol.WAV'),  # 4 - Mano 2, Dedo 1 (Índice)
    pygame.mixer.Sound('sounds/la.WAV'),    # 5 - Mano 2, Dedo 2 (Medio)
    pygame.mixer.Sound('sounds/si.WAV'),    # 6 - Mano 2, Dedo 3 (Anular)
]

# La función ahora recibe la lista de landmarks y los ÍNDICES de la punta y la base del dedo.
def is_finger_down(lista_landmarks, tip_index, mcp_index):
    # En OpenCV, el eje Y aumenta hacia abajo, por lo que si la punta tiene un valor Y mayor, está "doblado" o "abajo".
    return lista_landmarks[tip_index].y > lista_landmarks[mcp_index].y

manos = mp_manos.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5)

finger_state = [False] * 6

MAX_INDICES_A_PROBAR = 10
cap = None

for i in range(MAX_INDICES_A_PROBAR):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Cámara encontrada en el índice {i}.")
        break
    cap.release()

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

print()
print("Presiona 'ESC' para salir.")
print()
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignorando fotograma vacío de la cámara.")
        continue

    # Voltear la imagen horizontalmente para una vista tipo espejo
    frame = cv2.flip(frame, 1)
    frame.flags.writeable = False
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = manos.process(frame_rgb)
    frame.flags.writeable = True

    if resultados.multi_hand_landmarks:
        for m, mano_landmarks in enumerate(resultados.multi_hand_landmarks):
            # Usamos las constantes de MediaPipe en lugar de números para más claridad.
            finger_tips_indices = [mp_manos.HandLandmark.INDEX_FINGER_TIP, mp_manos.HandLandmark.MIDDLE_FINGER_TIP, mp_manos.HandLandmark.RING_FINGER_TIP]
            finger_mcp_indices = [mp_manos.HandLandmark.INDEX_FINGER_MCP, mp_manos.HandLandmark.MIDDLE_FINGER_MCP, mp_manos.HandLandmark.RING_FINGER_MCP]

            for i in range(3): #3 dedos de enmedio
                # Mano 0 (m=0): i=0,1,2 -> finger_index = 0,1,2
                # Mano 1 (m=1): i=0,1,2 -> finger_index = 4,5,6
                finger_index = i + (m * 3)
                

                if is_finger_down(mano_landmarks.landmark, finger_tips_indices[i], finger_mcp_indices[i]):
                    if not finger_state[finger_index]:
                        print(f"Nota musical {finger_index}") 
                        sonidos[finger_index].play() 
                        finger_state[finger_index] = True 
                else:
                    # Si el dedo está ARRIBA, reseteamos su estado.
                    finger_state[finger_index] = False

            mp_dibujo.draw_landmarks(
                frame,
                mano_landmarks,
                mp_manos.HAND_CONNECTIONS,
                mp_estilos_dibujo.get_default_hand_landmarks_style(),
                mp_estilos_dibujo.get_default_hand_connections_style())

    # Mostrar el fotograma resultante
    cv2.imshow('Muestra mensaje - MediaPipe', frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberar recursos
manos.close()
cap.release()
cv2.destroyAllWindows()
pygame.quit()
