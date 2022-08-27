# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plxscripting.easy import *

@st.cache
def check_connection(ip,localhostport_input,password):
    s,g = new_server(ip, localhostport_input, password=password)
    return(s.active)

    

def main_page():
    st.title("PLAXIS 3D Embedded beam generator app")

    st.markdown("**Creator**: Francisco Santos Marques (FM) CEng MICE ")
    st.markdown("*Current Version - 1.0*")
    st.markdown("**Revision tracker**")
    st.markdown("*Version 1.0 (27/08/2022) -  Initial  release of the tool*")
    st.markdown("")
    st.markdown("### Tool Instruction - ⚠️ Read first before moving to the App page ⚠️")
    st.sidebar.markdown("# Page 1 - Tool Instruction  ")
    st.markdown("#### Step 1")
    st.markdown("Make sure that  PLAXIS Input  Remote Scripting server is running (Expert --> Configure Remote Scripting server)") 
    st.markdown("**Take note of the password and port used to initialize the server**")
    st.write("*Detailed info about PLAXIS Remote Scripting server is in this [link](https://communities.bentley.com/products/geotech-analysis/w/plaxis-soilvision-wiki/46005/using-plaxis-remote-scripting-with-the-python-wrapper)*")
    
    st.markdown("#### Step 2 (Most critical step ⚠️)")
    st.markdown("The app is running on a cloud service, which means that the machine running PLAXIS needs to connect the app over the internet. Therefore you need:")
    st.markdown("""          
                - To know beforehand the **Public IP address** of the machine with PLAXIS --> check this [link](https://whatismyipaddress.com)
                - Set up appropriate **port forwarding rules in your router**. This is to allow the app to access the machine via the port assigned in the Remote Scripting server. More information in this [link](https://www.lifewire.com/how-to-port-forward-4163829)
                """)
    st.markdown("#### Step 3")
    st.markdown("Copy-paste the **Public IP**, **PLAXIS Remote Scripting Server password** information to the respective box on the left-hand side of the page.")
    st.markdown("Make sure also you assigned the correct **port** information")
    st.markdown(" ")
    st.markdown("If all goes well, a message showing a 🟢 will indicate that the app is communicating with PLAXIS. Also, Pile layout information importations options will appear below")
    st.markdown("If 🔴 is shown instead, please check steps 1 to 3 again")
    
    st.markdown("#### Step 4")
    st.markdown("Import the Pile layout information into the app")
    st.markdown("The app expects each embedded beam element information to be in a CSV file with the following format shown below:")
    list_fg=["Pile Name",
                  "x (m)",
                  
                  "y (m)",
                  "Top (m)",
                  "Toe(m)",
                  "Material"]
    
    df1 = pd.DataFrame(columns=list_fg)
    st.dataframe(df1)
    st.markdown("*Note: Columns names are case sensivite*")
    st.markdown("""          
                - Pile name - Name of the Pile
                - x (m) - x coordinate of the embedded beam element in PLAXIS (in project length unit)
                - y (m) - y coordinate of the embedded beam element in PLAXIS (in project length unit)
                - Top (m) - z coordinate of the top of embedded beam element in PLAXIS (in project length unit)
                - Toe (m) - z coordinate of the toe of embedded beam element in PLAXIS (in project length unit)
                - Material - Name of the embedded beam materialset to be assigned (**Note: Avoid using spaces in the name or/and using only numbers to name the material set**)
                """)
                
    st.markdown("#### Step 5")
    st.markdown("Press the 'Click here to generate the embedded beam elements in PLAXIS!' button and enjoy the ride! ")
    
    
  
   
    
    
def page2():
    st.title("PLAXIS 3D Embedded beam generator app")
    st.markdown("**Creator**: Francisco Santos Marques (FM) CEng MICE ")
    st.markdown("*Current Version - 1.0*")
    st.markdown("**Revision tracker**")
    st.markdown("*Version 1.0 (27/08/2022) -  Initial  release of the tool*")
    st.markdown("")

   
    st.sidebar.markdown("# Page 2 - App")
    

     
 

    st.sidebar.markdown("## PLAXIS Remote Script details")

    ip=st.sidebar.text_input("Public IP address of the machine with PLAXIS", key="ip_address")
    password=st.sidebar.text_input("PLAXIS Remote Scripting Server Password", key="password",type="password")
    localhostport_input=st.sidebar.number_input("Port assigned in PLAXIS Input",value=10000,)

        
    # localhostport_output=st.sidebar.number_input("Port assigned in PLAXIS Output",value=10001,)
    if len(password) !=0  and len(ip) !=0:
        # if st.sidebar.button('Establish connection between app and PLAXIS Remote Scripting'):    
        # try:
        # if s.active==True:
        #     # g.line(0,0,0,2,4,6)
        #     status=1
        
        s,g,status=check_connection(ip,localhostport_input,password)    
             
        if status==True:
            st.sidebar.write(" PLX Remote Scrip. Connection status : 🟢")
            st.sidebar.markdown("## Basic input information")
            uploaded_file = st.sidebar.file_uploader("Import Pile schedule data as xlsx file")
            if uploaded_file is not None:
                st.markdown("## Imported Pile schedule")
                st.markdown("##### Make sure that the format of the information is according the instructions defined in page 1!")
                df = pd.read_csv(uploaded_file ,header=0)
                list_check=[
                  "Pile Name",
                  "x (m)",
                  "y (m)",
                  "Top (m)",
                  "Toe(m)",
                  "Material"]
                  
                if df.columns.tolist()==list_check:    
                    st.dataframe(df)
        
                    if len(password) !=0 and uploaded_file is not None and len(ip) !=0:
                       if st.sidebar.button('Click here to generate the embedded beam elements in PLAXIS!'):
                           count=0
                           for i in range(0,len(df)):
                            count=count+1
                            name=df.loc[i,"Pile Name"]
                            print(name)
                            x_pile=df.loc[i,"x (m)"]
                            y_pile=df.loc[i,"y (m)"]
                            top_pile=df.loc[i,"Top (m)"]
                            toe_pile=df.loc[i,"Toe(m)"]
                            material=df.loc[i,"Material"]
                            try:
                                materialplx=getattr(g,material)
                            except:
                                # materialplx=getattr(g,material)
                                # st.write(materialplx)
                                st.write("{} NOT MODELLED Cannot find Embedded beam materialset {} -- Check Material sets in PLAXIS ".format(name,material))
                                continue
                            
                            g.embeddedbeam (x_pile,y_pile,top_pile,x_pile,y_pile,toe_pile)
                            g.Lines[-1].EmbeddedBeam.Material=materialplx
                else:
                    st.markdown("### ❌❌❌Import columns format is not correct!!") 
                    st.markdown("### ⚠️⚠️⚠️Check if the imported csv is formated according to the guidance in the instruction page")
       
        
        

            
        else:
            st.sidebar.write(" PLX Remote Scrip. Connection status : 🔴") 

        
            
  

    