import streamlit as st
import mysql.connector as mc
import pandas as pd
mydb=mc.connect(host="localhost",user="root",password="scott",database="cutoff")
mycursor=mydb.cursor()
def data_cutoff2022(your_community,your_branch,cutoff_mark):
    sql="select * from cutoff2022 where branchname=%s "
    var=(your_branch,)
    mycursor.execute(sql,var)
    data=mycursor.fetchall()
    tuple_=[]
    if your_community=="BC":
        for i in data:
            if i[5]<cutoff_mark and i[5]!=0:
                list_=[i[0],i[1],i[2],i[5]]
                tuple_.append(list_)
    if your_community=="OC":
        for i in data:
            if i[4]<cutoff_mark and i[4]!=0:
                list_=[i[0],i[1],i[2],i[4]]
                tuple_.append(list_)
    if your_community=="BCM":
        for i in data:
            if i[6]<cutoff_mark and i[6]!=0:
                list_=[i[0],i[1],i[2],i[6]]
                tuple_.append(list_)
    if your_community=="MBC":
        for i in data:
            if i[7]<cutoff_mark and i[7]!=0:
                list_=[i[0],i[1],i[2],i[7]]
                tuple_.append(list_)
    if your_community=="SC":
        for i in data:
            if i[8]<cutoff_mark and i[8]!=0:
                list_=[i[0],i[1],i[2],i[8]]
                tuple_.append(list_)
    if your_community=="SCA":
        for i in data:
            if i[9]<cutoff_mark and i[9]!=0:
                list_=[i[0],i[1],i[2],i[9]]
                tuple_.append(list_)
    if your_community=="ST":
        for i in data:
            if i[10]<cutoff_mark and i[10]!=0:
                list_=[i[0],i[1],i[2],i[10]]
                tuple_.append(list_)
    return tuple_
def data_cutoff2021(your_community,your_branch,cutoff_mark):
    sql="select * from cutoff2021 where branchname=%s "
    var=(your_branch,)
    mycursor.execute(sql,var)
    data=mycursor.fetchall()
    tuple_=[]
    if your_community=="BC":
        for i in data:
            if i[5]<cutoff_mark and i[5]!=0:
                list_=[i[0],i[1],i[2],i[5]]
                tuple_.append(list_)
    if your_community=="OC":
        for i in data:
            if i[4]<cutoff_mark and i[4]!=0:
                list_=[i[0],i[1],i[2],i[4]]
                tuple_.append(list_)
    if your_community=="BCM":
        for i in data:
            if i[6]<cutoff_mark and i[6]!=0:
                list_=[i[0],i[1],i[2],i[6]]
                tuple_.append(list_)
    if your_community=="MBC":
        for i in data:
            if i[7]<cutoff_mark and i[7]!=0:
                list_=[i[0],i[1],i[2],i[7]]
                tuple_.append(list_)
    if your_community=="SC":
        for i in data:
            if i[8]<cutoff_mark and i[8]!=0:
                list_=[i[0],i[1],i[2],i[8]]
                tuple_.append(list_)
    if your_community=="SCA":
        for i in data:
            if i[9]<cutoff_mark and i[9]!=0:
                list_=[i[0],i[1],i[2],i[9]]
                tuple_.append(list_)
    if your_community=="ST":
        for i in data:
            if i[10]<cutoff_mark and i[10]!=0:
                list_=[i[0],i[1],i[2],i[10]]
                tuple_.append(list_)
    return tuple_
def data_cutoff2020(your_community,your_branch,cutoff_mark):
    sql="select * from cutoff2020 where branchname=%s "
    var=(your_branch,)
    mycursor.execute(sql,var)
    data=mycursor.fetchall()
    tuple_=[]
    if your_community=="BC":
        for i in data:
            if i[5]<cutoff_mark and i[5]!=0:
                list_=[i[0],i[1],i[2],i[5]]
                tuple_.append(list_)
    if your_community=="OC":
        for i in data:
            if i[4]<cutoff_mark and i[4]!=0:
                list_=[i[0],i[1],i[2],i[4]]
                tuple_.append(list_)
    if your_community=="BCM":
        for i in data:
            if i[6]<cutoff_mark and i[6]!=0:
                list_=[i[0],i[1],i[2],i[6]]
                tuple_.append(list_)
    if your_community=="MBC":
        for i in data:
            if i[7]<cutoff_mark and i[7]!=0:
                list_=[i[0],i[1],i[2],i[7]]
                tuple_.append(list_)
    if your_community=="SC":
        for i in data:
            if i[8]<cutoff_mark and i[8]!=0:
                list_=[i[0],i[1],i[2],i[8]]
                tuple_.append(list_)
    if your_community=="SCA":
        for i in data:
            if i[9]<cutoff_mark and i[9]!=0:
                list_=[i[0],i[1],i[2],i[9]]
                tuple_.append(list_)
    if your_community=="ST":
        for i in data:
            if i[10]<cutoff_mark and i[10]!=0:
                list_=[i[0],i[1],i[2],i[10]]
                tuple_.append(list_)
    return tuple_
def data_cutoff2019(your_community,your_branch,cutoff_mark):
    sql="select * from cutoff2019 where branchname=%s "
    var=(your_branch,)
    mycursor.execute(sql,var)
    data=mycursor.fetchall()
    tuple_=[]
    if your_community=="BC":
        for i in data:
            if i[5]<cutoff_mark and i[5]!=0:
                list_=[i[0],i[1],i[2],i[5]]
                tuple_.append(list_)
    if your_community=="OC":
        for i in data:
            if i[4]<cutoff_mark and i[4]!=0:
                list_=[i[0],i[1],i[2],i[4]]
                tuple_.append(list_)
    if your_community=="BCM":
        for i in data:
            if i[6]<cutoff_mark and i[6]!=0:
                list_=[i[0],i[1],i[2],i[6]]
                tuple_.append(list_)
    if your_community=="MBC":
        for i in data:
            if i[7]<cutoff_mark and i[7]!=0:
                list_=[i[0],i[1],i[2],i[7]]
                tuple_.append(list_)
    if your_community=="SC":
        for i in data:
            if i[8]<cutoff_mark and i[8]!=0:
                list_=[i[0],i[1],i[2],i[8]]
                tuple_.append(list_)
    if your_community=="SCA":
        for i in data:
            if i[9]<cutoff_mark and i[9]!=0:
                list_=[i[0],i[1],i[2],i[9]]
                tuple_.append(list_)
    if your_community=="ST":
        for i in data:
            if i[10]<cutoff_mark and i[10]!=0:
                list_=[i[0],i[1],i[2],i[10]]
                tuple_.append(list_)
    return tuple_
st.set_page_config(page_title="CUTOFF",page_icon=":user",layout="wide")
st.header("Hello Everyone!!")
st.write("---")
with st.container():
    st.header("Calculate Your Cutoff")
    st.write("##")
    math_mark=st.slider("Enter your Maths mark:",0,100)
    chem_mark=st.slider("Enter your Chemistry mark:",0,100)
    phy_mark=st.slider("Enter your Physics mark:")
    cutoff_mark=(math_mark+(chem_mark+phy_mark)/2)
if cutoff_mark!=0:
    st.subheader("Your Cutoff is:")
    st.header(str(cutoff_mark))
with st.container():
    st.write("---")
    st.write("##")
    st.subheader("Get to know the COLLEGES you have chance for!!")
    branch_list=["CIVIL  ENGINEERING","COMPUTER SCIENCE ANDENGINEERING (SS)","COMPUTER SCIENCE ANDENGINEERING","ELECTRONICS ANDCOMMUNICATIONENGINEERING","ELECTRICAL ANDELECTRONICS ENGINEERING","ELECTRONICS ANDCOMMUNICATIONENGINEERING (SS)","GEO INFORMATICS","INFORMATION TECHNOLOGY(SS)","MECHANICAL ENGINEERING","MINING ENGINEERING","PRINTING AND PACKINGTECHNOLOGY","MECHANICAL ENGINEERING(TAMIL MEDIUM)","CHEMICAL  ENGINEERING","CHEMICAL  ENGINEERING (SS)","CERAMIC TECHNOLOGY (SS)","FOOD TECHNOLOGY (SS)","INDUSTRIAL BIO TECHNOLOGY","INDUSTRIAL BIO TECHNOLOGY(SS)","PETROLEUM ENGINEERINGAND TECHNOLOGY (SS)","TEXTILE TECHNOLOGY","AERONAUTICAL ENGINEERING","ARTIFICIAL INTELLIGENCE ANDDATA SCIENCE","PLASTIC TECHNOLOGY","Mechatronics Engineering","Computer Science andEngineering (Cyber Security)","FASHION TECHNOLOGY","ELECTRONICS ANDINSTRUMENTATIONENGINEERING","AUTOMOBILE ENGINEERING(SS)","BIO TECHNOLOGY (SS)","Computer Science andEngineering (ArtificialIntelligence and MachineLearning) (SS)","INSTRUMENTATION ANDCONTROL ENGINEERING (SS)","MECHANICAL ENGINEERING(SS)","MECHANICAL ENGINEERING(SANDWICH) (SS)","ELECTRICAL ANDELECTRONICS ENGINEERING(SS)","BIO MEDICAL ENGINEERING","COMPUTER SCIENCE ANDENGINEERING (TAMIL)","AGRICULTURAL ENGINEERING","COMPUTER SCIENCE ANDBUSSINESS SYSTEM","Cyber Security","Safety and Fire Engineering","METALLURGICALENGINEERING","MEDICAL ELECTRONICSENGINEERING","ROBOTICS AND AUTOMATION ","COMPUTER SCIENCE ANDDESIGN","BIO TECHNOLOGY","Artificial Intelligence andMachine Learning","COMPUTER ANDCOMMUNICATIONENGINEERING","CIVIL ENGINEERING (TAMILMEDIUM)","MECHANICAL ANDAUTOMATION ENGINEERING","MECHATRONICS (SS)","PETRO CHEMICALENGINEERING"] 
    your_branch=st.selectbox("Select your course:",branch_list,index=0)
    community_list=["BC","OC","MBC","ST","SC","BCM","SCA"]
    your_community=st.selectbox("Select your course:",community_list,index=0)
    st.write("---")
    st.write("##")
    st.write("YEAR-2022")
    data_1=data_cutoff2022(your_community,your_branch,cutoff_mark)
    df_1=pd.DataFrame(data_1,columns=['college code','college name','branch','cutoff'])
    st.dataframe(df_1)
    st.write("YEAR-2021")
    data_2=data_cutoff2021(your_community,your_branch,cutoff_mark)
    df_2=pd.DataFrame(data_2,columns=['college code','college name','branch','cutoff'])
    st.dataframe(df_2)
    st.write("YEAR-2020")
    data_3=data_cutoff2020(your_community,your_branch,cutoff_mark)
    df_3=pd.DataFrame(data_3,columns=['college code','college name','branch','cutoff'])
    st.dataframe(df_3)
    st.write("YEAR-2019")
    data_4=data_cutoff2019(your_community,your_branch,cutoff_mark)
    df_4=pd.DataFrame(data_4,columns=['college code','college name','branch','cutoff'])
    st.dataframe(df_4)
with st.container():
    st.markdown('''### DISCLAMER:
                           -All the data has been collected from vocational tnea cutoff data available at "www.tneaonline.com".
    -The cutoff are closing cutoff and the funtionality of this website is inaccurate.
    -The councelling cutoff cannot be determined because it is based on various factors.
                ''')
    st.write("---")
    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://www.formbackend.com/f/998a24bab67ece7c" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css(r"C:\Users\Uma Ramesh\Desktop\project\style\style.css")




