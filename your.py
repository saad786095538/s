import streamlit as st
import re

st.set_page_config(page_title="password strength meter",page_icon="🔒")
st.title("🔐password strength meter")

password=st.text_input("enter your password",type="password")

feedback=[]

score=0
if password:

    if len(password)>=8:
     score+=1
    else:
        feedback.append("❌password should be at least 8 characters long")
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
     score+=1
    else:
     feedback.append("❌password should contain both uper and lower case characters")
    if re.search(r'\d',password):
      score+=1
    else:
         feedback.append("❌password should contain at least one digit")
    if re.search(r'[!@#%?&*]',password):
        score+=1
    else:
        feedback.append("❌password should be at least one special character")
    if score==4:
        feedback.append("✅your password is strong🎉")
    elif score==3:
        feedback.append("🟡your password is meidiumm strenghth")
    else:
        feedback.append("🔴your password is weak")
    if feedback:
        st.markdown("##improve suggestions")
        for tip in feedback:
            st.write(tip)
else:
   st.info("please enter your password to get started")
   
