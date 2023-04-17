import streamlit as st
import os
import pandas as pd

df = pd.read_csv('try.csv')

edited_df = st.experimental_data_editor(df)

output_path = "try.csv"
edited_df.to_csv(output_path, mode='a', index=False,
                 header=not os.path.exists(output_path))
