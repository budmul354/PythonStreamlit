import streamlit as st
import pandas as pd
import numpy as np
import re


st.title("Perlengkapan Haji")

# @st.cache_data
def load_data(nrows):
    columns_to_keep = ["Nama Produk", "Harga", "Link Komisi Ekstra"]
    data = pd.read_csv("LinkProdukSekaligus.csv", usecols=columns_to_keep)
    data.columns = ["Nama Produk","Harga","Link Toko"]
    # data['Nama Produk'] = data['Nama Produk'].apply(normalize_text)
    # print(data)
    # return data.to_markdown()
    data.index = range(1, len(data) + 1)
    return data

def normalize_text(text):
    return re.sub(r"\|"," ",text)


def main():
    data = load_data(1)
    # st.markdown(data)
    container = st.container()
    with container:
        st.dataframe(data,column_config={"Link Toko": st.column_config.LinkColumn()}, height=None)

if __name__ == '__main__':
    main()