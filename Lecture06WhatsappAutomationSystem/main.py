import time

import pyautogui
import streamlit as st 
import pandas as pd
import pywhatkit as kit


st.set_page_config("WhatsApp Automation Libarary ") 

st.title("WhatsApp Automation System ")

upload= st.file_uploader("upload and excel or csv ", type=["xlsx"])


portfolio=st.text_input("Enter Your Portfolio Link ", "https://syedmuhammadarsalanshah.com/")


customMessage= st.text_area("Enter Your Message Here ", "Follow me On Web ")


if upload is not None :
    df=pd.read_excel(upload)
    st.write("Contacts are uploaded")
    st.dataframe(df)
    if st.button("Send Message "):
        for index, row in df.iterrows():
            phoneNumber=f"+92{row["Phone"]}"
            message=f"{customMessage} \n {portfolio}"
            
            
            kit.sendwhatmsg_instantly(phoneNumber,message,wait_time=35)
            time.sleep(10)
            pyautogui.press("enter")
            print("Sent")
            time.sleep(5)
            pyautogui.press("enter")
    


