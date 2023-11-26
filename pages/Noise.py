import streamlit as st
import streamlit.components.v1 as components

st.title("GreenSight Data Visualization - Noise")
st.write("This data was synthesized with our proprietary algorithm for measuring ecological advantages, called Noise.")
with st.expander("What is Noise?"):
    st.write("Noise is a composite metric that takes into account the following factors:")
    st.write("""- Population density
- Availability of hospitals
- Availability of waste management
- Availability of educational institutions
- Geological features
    """)
    st.write("It can easily be extended to include other significant factors.")

noise_html = open("embed/noise.html").read()
components.html(noise_html, height=800)