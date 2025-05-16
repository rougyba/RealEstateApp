import pandas as pd
import streamlit as st
data = {
    "Title": ["5 Bedroom House w/ Pool"],
    "Location": ["Tevragh Zeina, Mauritania"],
    "Price (USD)": [250000],
    "Price (MRU)": [250000 * 38],
    "Features": ["Spacious 5-bed, 3-bath home with pool in a top Nouakchott neighborhood"],
    "Image URL": [
        "https://drive.google.com/uc?export=view&id=1-hgnmbe7b24Rz_UU5J_V5J_XdpB02mix, https://drive.google.com/uc?export=view&id=1twiJDtmP4vs2y0oOzj9YtDDQ3ZABtKp4"
    ]
}

df = pd.DataFrame(data)
df.to_csv("listings.csv", index=False)
import streamlit as st
import pandas as pd

# Load listings
df = pd.read_csv("listings.csv")

st.title("🏡 Mauritania Real Estate App")

# Show listings (only one for now)
for idx, row in df.iterrows():
    st.subheader(row["Title"])
    st.markdown(f"**Location:** {row['Location']}")
    st.markdown(f"**Price (USD):** ${row['Price (USD)']}")
    st.markdown(f"**Price (MRU):** {row['Price (MRU)']} MRU")
    st.markdown(f"**Features:** {row['Features']}")

    # Split and display multiple images
    image_links = row["Image URL"].split(",")
    for link in image_links:
        st.image(link.strip(), width=300)

    st.markdown("---")

