import streamlit as st 
import re 

st.markdown("""
<style>
.stApp {
    background-image: url(https://i.pinimg.com/736x/32/05/63/320563f808d3aa67e8fab5afa718efa6.jpg);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    
}
</style>
""", unsafe_allow_html=True)




st.title("Password Strength Checker")
def check_password_strength(password):
    score= 0

    weak_password =["password123" , "abc123", "passsword12345" ,"password1" , "password321","1234","1234567899"]
    if password in weak_password:
        st.error("This password is commonly used it's a weak password. Please choose a stronger password.")
        return 0
    if len(password)>=8:
        score+=1
    else:
        st.warning("Must contain at least 8 chacracters long.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score+=1
    else:
        st.warning("Must contain both uppercase and lowercase letters.")

    if re.search(r"\d",password):
        score+=1
    else:
        st.warning("Must contain at least one digit.")

    if re.search(r"[!@#$%^&*(),.?:{}|<>]",password):
        score+=1
    else:
        st.warning("Must contain at least one special character.")
    return score
    




password = st.text_input("Enter your password: ",type="password")


if password.strip():
    score = check_password_strength(password)
    


    if score == 4:
        st.success("Password is strong.")
    elif score == 3:
        st.success("Password is good.")
    elif score == 2:
        st.warning("Password is medium.")
    else:
        st.warning("Password is weak.")

    if score ==4 :
        st.success("Succesfully created password!")
    else:
        st.warning("Please enter a password.")

