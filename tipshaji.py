import streamlit as st
import pandas as pd
import numpy as np
import re


st.title("Perlengkapan Haji")

# @st.cache_data
def load_data(nrows):
    columns_to_keep = ["Nama Produk", "Harga", "Link Komisi Ekstra"]
    data = pd.read_csv("LinkProdukSekaligus.csv", usecols=columns_to_keep)
    # data.rename(columns={"Link Komisi Ekstra":"Link Toko"})
    data.columns = ["Nama Produk","Harga","Link Toko"]
    data.replace(r"\|", " ", regex=True)
    data['Nama Produk'] = data['Nama Produk'].apply(normalize_text)
    print(data)
    return data.to_markdown()

def normalize_text(text):
    return re.sub(r"\|"," ",text)


def main():
    data = load_data(1)
    st.markdown(data)

if __name__ == '__main__':
    main()