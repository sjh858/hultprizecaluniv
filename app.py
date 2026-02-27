import streamlit as st
import os
from thefuzz import process  # Import fuzzy matching

# --- CONFIGURATION ---
CERT_FOLDER = "certificates"
st.set_page_config(page_title="Hult Prize CU - Certificates", page_icon="🎓")

# Branding
st.subheader("Hult Prize On-Campus 2026, University of Calcutta")
st.title("🎓 Download Your Certificate")
st.write("Enter your full name as registered to retrieve your e-certificate.")

# Get a list of all certificate names (handling .jpg based on your update)
if os.path.exists(CERT_FOLDER):
    all_files = [f for f in os.listdir(CERT_FOLDER) if f.endswith('.jpg')]
    cert_names = {f.replace('.jpg', ''): f for f in all_files}
else:
    st.error("Certificate folder not found!")
    cert_names = {}

# --- SEARCH UI ---
name_query = st.text_input("Enter your Full Name:", placeholder="e.g. John Doe")

# Add a Search Button
if st.button("Search Certificate"):
    if name_query.strip():
        # Use fuzzy logic to find the best match
        match_result = process.extractOne(name_query, cert_names.keys())
        
        if match_result:
            best_match, score = match_result
            
            # Threshold Check
            if score >= 85:
                st.success(f"Certificate found for: **{best_match}**")
                
                file_path = os.path.join(CERT_FOLDER, cert_names[best_match])
                
                # Load the image for the download button
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=f"Click here to Download",
                        data=f,
                        file_name=cert_names[best_match],
                        mime="image/jpeg" # Changed to jpeg since you are searching for .jpg
                    )
                
                # Optional: Show a preview of the image
                st.image(file_path, caption=f"Preview for {best_match}", use_container_width=True)
                
            else:
                st.warning("No close match found. Please check your spelling and try again.")
        else:
            st.error("No certificate found. Please check the spelling or contact the organizer.")
    else:
        st.error("Please enter a name before searching.")


# --- OPTIONAL: FOOTER ---
st.divider()

st.caption("Powered by Streamlit | Designed by Soham Sarkar")

