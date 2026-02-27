import streamlit as st
import os

# --- CONFIGURATION ---
CERT_FOLDER = "certificates"  # Your folder name with JPGs
CSV_PATH = "recipients.csv"    # Your list of names

st.set_page_config(page_title="Certificate Portal", page_icon="🎓")

st.title("Hult Pize On-Campus 2026, University of Calcutta")
st.title("🎓 Download Your Certificate")
st.write("Enter your full name as registered to retrieve your e-certificate as a member of the organising committee.")

# --- SEARCH LOGIC ---
name_query = st.text_input("Enter your Full Name:", placeholder="e.g. John Doe")

if name_query:
    # Clean the input
    search_name = name_query.strip().lower()
    
    # Check if the file exists (matching filename to search query)
    # Assumes files are named 'Soham Sarkar.jpg'
    file_path = os.path.join(CERT_FOLDER, f"{name_query.strip()}.jpg")
    
    if os.path.exists(file_path):
        st.success(f"Certificate found for {name_query.strip()}!")
        
        with open(file_path, "rb") as f:
            st.download_button(
                label="Download file",
                data=f,
                file_name=f"{name_query.strip()}.jpg",
                mime="application/jpg"
            )
    else:
        st.error("No certificate found. Please check the spelling or contact the organizer.")

# --- OPTIONAL: FOOTER ---
st.divider()
st.caption("Powered by Streamlit | Designed by Soham Sarkar")