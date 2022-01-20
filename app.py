import streamlit as st
import re
from pathlib import Path
import importlib

import yaml

REGEX_YAML_BLOCK = re.compile(r"---[\n\r]+([\S\s]*?)[\n\r]+---[\n\r](.*)", re.DOTALL)


def render_preview(image, title, description):
    with st.container():
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image(image)

        with text_col:
            st.subheader(title)
            st.write(description)
            clicked = st.button("Read more...", key=title)
        return clicked


def render_page(post_path: Path):
    mod = importlib.import_module(str(post_path))
    mod.run_article()
    

def get_page_data(post_path: Path):
    mod = importlib.import_module(str(post_path))
    return {
        "title": mod.title,
        "description": mod.description,
        "date": mod.date,
        "thumbnail": mod.thumbnail,
    }


def main():
    st.set_page_config(layout="wide")
    posts = ['posts.1_blog_in_spaces']
    page_to_show = posts[0]
    with st.sidebar:
    
        st.markdown('''
            <div align="center">
                <h1>🤗 Tips & Tricks</h1>
                <p>Learn power user tips of things you can do at Hugging Face. Learn about latest features and more!</p>

            [![Github Badge](https://img.shields.io/github/stars/osanseviero/hf-tips-and-tricks?style=social)](https://github.com/osanseviero/hf-tips-and-tricks)
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('---')

        for post in posts:
            data = get_page_data(Path(post))
            clicked = render_preview(data.get("thumbnail"), data.get("title"), data.get("description"))
            if clicked:
                page_to_show = post

    if page_to_show:
        render_page(Path(page_to_show))

main()
