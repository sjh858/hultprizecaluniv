import streamlit as st
import os
from thefuzz import process  # Import fuzzy matching

# --- CONFIGURATION ---
CERT_FOLDER = "certificates"
st.set_page_config(page_title="Certificate Portal", page_icon="🎓")

st.title("Hult Pize On-Campus 2026, University of Calcutta")
st.title("🎓 Download Your Certificate")
st.write("Enter your full name as registered to retrieve your e-certificate as a member of the organising committee.")

# Get a list of all certificate names (without .jpg)
if os.path.exists(CERT_FOLDER):
    all_files = [f for f in os.listdir(CERT_FOLDER) if f.endswith('.jpg')]
    # Dictionary mapping {Clean Name: Original Filename}
    cert_names = {f.replace('.jpg', ''): f for f in all_files}
else:
    st.error("Certificate folder not found!")
    cert_names = {}

# --- SEARCH LOGIC ---
name_query = st.text_input("Enter your Full Name:", placeholder="e.g. John Doe")

if name_query:
    # 1. Use fuzzy logic to find the best match
    # process.extractOne returns (match, score)
    match_result = process.extractOne(name_query, cert_names.keys())
    
    if match_result:
        best_match, score = match_result
        
        # 2. Set a threshold (usually 80-90 is safe)
        if score >= 85:
            st.info(f"Showing result for: **{best_match}** (Match score: {score}%)")
            
            file_path = os.path.join(CERT_FOLDER, cert_names[best_match])
            
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"Download {best_match}'s Certificate",
                    data=f,
                    file_name=cert_names[best_match],
                    mime="application/pdf"
                )
        else:
            st.warning("No close match found. Please try typing your name again.")
    else:
        st.error("No certificate found. Please check the spelling or contact the organizer.")
# --- OPTIONAL: FOOTER ---
st.divider()

st.caption("Powered by Streamlit | Designed by Soham Sarkar")
