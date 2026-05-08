import streamlit as st
import Langchain_helper

st.title("Restaurant Name Generator")

cuisine= st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","Arabic", "American"))

def generate_restaurant_name_items(cuisine):
    return {
        'restaurant_name':'Foodies IN ',
        'menu_items': 'samosa,paneer masala,butter chicken,biryani,masala dosa,rajma chawal,chole bhature,palak paneer,dal makhani,tandoori chicken'
    }
if cuisine:
    response= Langchain_helper.generate_restaurant_name_items(cuisine)

    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**menu_items**")

    for item in menu_items:
        st.write("-",item)