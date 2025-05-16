{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "90902bef-ae08-42f8-9cbc-2922dccb435c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7ffa8261-bbd6-4acd-9c2b-497735f2305b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "data = {\n",
    "    \"title\": [\"5 Bedroom House w/ Pool\"],\n",
    "    \"location\": [\"Tevragh Zeina, Mauritania\"],\n",
    "    \"price_usd\": [250000],\n",
    "    \"price_mru\": [250000 * 38],  # USD to MRU conversion\n",
    "    \"description\": [\"Spacious 5-bed, 3-bath home with pool in a top Nouakchott neighborhood\"],\n",
    "    \"images\": [\"https://drive.google.com/file/d/1-hgnmbe7b24Rz_UU5J_V5J_XdpB02mix/view?usp=share_link,https://drive.google.com/file/d/1twiJDtmP4vs2y0oOzj9YtDDQ3ZABtKp4/view?usp=share_link\"]  # Replace with real URLs\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "df.to_csv(\"listings.csv\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b92dee6a-d62d-45e0-9ced-716db5e1a835",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv(\"listings.csv\")\n",
    "\n",
    "st.title(\"🏡 Mauritania Real Estate App\")\n",
    "\n",
    "# Filter by location\n",
    "locations = df[\"location\"].unique()\n",
    "selected_location = st.selectbox(\"Filter by location\", options=[\"All\"] + list(locations))\n",
    "\n",
    "# Apply filter\n",
    "if selected_location != \"All\":\n",
    "    df = df[df[\"location\"] == selected_location]\n",
    "\n",
    "# Show listings\n",
    "for idx, row in df.iterrows():\n",
    "    st.subheader(row[\"title\"])\n",
    "    st.markdown(f\"**Location:** {row['location']}\")\n",
    "    st.markdown(f\"**Price (USD):** ${row['price_usd']}\")\n",
    "    st.markdown(f\"**Price (MRU):** {row['price_mru']} MRU\")\n",
    "    st.markdown(f\"**Description:** {row['description']}\")\n",
    "\n",
    "    image_links = str(row[\"images\"]).split(\",\")\n",
    "    for link in image_links:\n",
    "        st.image(link.strip(), width=300)\n",
    "\n",
    "    st.markdown(\"---\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a34e1059-cc55-4919-a9b6-7f3e17ba2c8d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6597dc5d-745e-46fb-a06c-1301a05cf0d9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f8c68a8-10ac-43dc-bbb6-6c2bc1da0706",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73e2676a-6018-4f5a-bec1-c61c9aa6c718",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
