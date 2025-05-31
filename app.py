import streamlit as st
import pandas as pd

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
        html, body {
            background-color: white !important;
            margin: 0;
            font-family: Arial, sans-serif;
            color: black;
        }
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: left;
            padding: 40px 50px;
            background-color: 
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 80%;
            top: 10;
            z-index: 100;
        }
        .top-nav .left {
            font-size: 30px;
            font-weight: bold;
        }
        .top-nav .right {
            display: flex;
            gap: 50px;
            align-items: right;
        }
        .top-banner {
            background-image: url('https://i.imgur.com/YD56mZv.png');
            background-size: cover;
            background-position: left;
            height: 900px;
            width: 100vw;
            display: flex;
            align-items: flex-end;
            justify-content: center;
           .top-banner {
    background-image: url('https://i.imgur.com/YD56mZv.png');
    background-size: cover;
    background-position: center;
    height: 600px;
    width: 100vw;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    position: relative;
    margin-top: 60px;
    padding-bottom: 200px; /* Moved search bar up */
}


.search-box-container {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 20px 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    width: 60%;
    display: flex;
    justify-content: center;
}

        .listings-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            padding: 80px 40px 40px;
            background-color: white;
        }
        .listing-card {
            width: 48%;
            margin-bottom: 50px;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            color: black;
        }
        .listing-card img {
            width: 100%;
            border-radius: 10px;
        }
        .listing-card h2 {
            margin-top: 15px;
            margin-bottom: 10px;
            font-size: 26px;
        }
        .listing-card p {
            font-size: 18px;
            margin-bottom: 10px;
        }

        @media (max-width: 768px) {
            .listings-container {
                flex-direction: column;
                align-items: center;
            }
            .listing-card {
                width: 100% !important;
            }
            .search-box-container {
                width: 90% !important;
            }
            .top-nav {
                flex-direction: column;
                gap: 10px;
            }
            .top-banner {
                height: 400px;
                padding-bottom: 20px;
            }
        }
    </style>
   <div class="top-nav">
        <div class="left">
            <select style="padding: 5px 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px;">
                <option>Buy</option>
                <option>Rent</option>
                <option>Sell</option>
            </select>
        </div>
        <div class="right">
            <div style="font-size: 16px; cursor: pointer;">Sign In</div>
        </div>
    </div>

    """,
    unsafe_allow_html=True
)

# ---------- Top Banner with Search Input ----------
st.markdown('<div class="top-banner">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="search-box-container">
        <div style="position: relative;">
            <input type="text" placeholder="Search by city, neighborhood or home type..." style="width: 100%; padding: 15px 50px 15px 20px; font-size: 20px; border-radius: 8px; border: 1px solid #ccc;">
            <span style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); font-size: 22px;">🔍</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Sample Listings Data ----------
data = {
    "Title": [
        "5 Bedroom House with Pool",
        "6 Bedroom Villa with Pool"
    ],
    "Location": [
        "Tevragh Zeina, Mauritania",
        "Cite Plage, Nouakchott"
    ],
    "Price (USD)": [250000, 350000],
    "Price (MRU)": [250000 * 38, 350000 * 38],
    "Features": [
        "Spacious 5-bedroom, 3-bath home with private pool and modern finishes in the prestigious Tevragh Zeina neighborhood. Great for families and entertaining.",
        "Elegant 6-bedroom, 3-bath villa with a private pool, 300m² living space, and premium amenities. Steps from the beach in scenic Cite Plage."
    ],
    "Image URL": [
        "https://i.imgur.com/5kFFD1B.jpeg",
        "https://i.imgur.com/DeXEqUn.jpeg"
    ],
    "WhatsApp": [
        "https://wa.me/22220000001",
        "https://wa.me/22220000002"
    ]
}

# ---------- Display Listings ----------
df = pd.DataFrame(data)
st.markdown('<div class="listings-container">', unsafe_allow_html=True)

for _, row in df.iterrows():
    st.markdown(f'''
        <div class="listing-card">
            <img src="{row['Image URL']}"/>
            <h2>{row['Title']}</h2>
            <p><strong>Location:</strong> {row['Location']}</p>
            <p><strong>Price:</strong> ${row['Price (USD)']:,} USD / {row['Price (MRU)']:,} MRU</p>
            <p>{row['Features']}</p>
            <a href="{row['WhatsApp']}" target="_blank">
                <button style='background-color:#25D366;color:white;padding:10px 15px;border:none;border-radius:5px;font-size:16px;'>
                    📱 Contact on WhatsApp
                </button>
            </a>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)