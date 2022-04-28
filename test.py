import cv2
import streamlit as st
import os

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


class Face_Register:
    def __init__():
        path_photos_from_camera = "data/data_faces_from_camera/"
    def GUI_clear_data():
        path_photos_from_camera = "data/data_faces_from_camera/"
        folders_rd = os.listdir(path_photos_from_camera)
        for i in range(len(folders_rd)):
            shutil.rmtree(path_photos_from_camera + folders_rd[i])
        if os.path.isfile("data/features_all.csv"):
            os.remove("data/features_all.csv")
        label_cnt_face_in_database['text'] = "0"
        existing_faces_cnt = 0
        log_all["text"] = "Face images and `features_all.csv` removed!"


while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    




else:
    st.write('Stopped')
if st.button("Clear Data123"):
    Face_Register.GUI_clear_data()
