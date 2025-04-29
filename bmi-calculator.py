import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg:")
height = st.number_input("Enter your height in cm:")

if st.button("Calculate BMI"):
    if height == 0:
        st.error("Height cannot be zero!")
    else:
        height_in_meters = height / 100
        final_height = height_in_meters ** 2
        bmi = weight / final_height

        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
