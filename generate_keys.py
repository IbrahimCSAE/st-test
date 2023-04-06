# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 01:10:08 2023

@author: Marwan
"""

import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Marwan"]

usernames = ['marwan']
passwords = ["abc"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
