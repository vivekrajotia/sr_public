import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from get_faces_from_camera import Face_Register
from get_faces_from_camera_tkinter import main
st.write("hi")
if st.button("face_register"):
    main()
if st.button("model_train"):
    from features_extraction_to_csv import main
    main()
if st.button("detection"):
    from face_reco_from_camera import main
    # from face_reco_from_camera  import name_db
    main()
    # global name_db
    # st.write(name_db)
