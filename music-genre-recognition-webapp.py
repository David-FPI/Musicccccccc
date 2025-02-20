import numpy as np
import streamlit as st
import base64
import pytube
import os
import subprocess 
import librosa
import tempfile 
from pydub import AudioSegment
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import tensorflow as tf
from statistics import mode
from tensorflow import keras
from keras import regularizers
from keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import Model, Sequential, load_model
from tensorflow.keras.layers import (Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, 
                                     Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D,
                                     Dropout)
st.title("🎈 Ben ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
