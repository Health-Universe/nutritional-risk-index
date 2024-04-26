import streamlit as st

def calculate_nri(albumin, actual_weight, usual_weight):
    if usual_weight > 0:  # To avoid division by zero
        nri = 1.519 * albumin + 41.7 * (actual_weight / usual_weight)
        return nri
    else:
        return "Usual weight must be greater than zero"

st.title('Nutritional Risk Index (NRI) Calculator')

st.write("""
This app calculates the Nutritional Risk Index (NRI), which is used to assess the nutritional status of patients.
Enter the required values below to compute the NRI.
""")

with st.form("nri_form"):
    serum_albumin = st.number_input('Enter Serum Albumin in g/dL:', min_value=0.0, format="%.2f")
    actual_weight = st.number_input('Enter Actual Weight in kg:', min_value=0.0, format="%.2f")
    usual_weight = st.number_input('Enter Usual Weight in kg:', min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Calculate NRI")
    if submitted:
        nri_result = calculate_nri(serum_albumin, actual_weight, usual_weight)
        if isinstance(nri_result, str):
            st.error(nri_result)
        else:
            st.success(f'The Nutritional Risk Index (NRI) is: {nri_result:.2f}')

