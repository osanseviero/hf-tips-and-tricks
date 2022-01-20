from email.mime import image
import streamlit as st

title = "T&T1 - Create interactive blog posts with Streamlit and Spaces"
description = "Learn about how to host interactive blogs using Streamlit, GitHub and Spaces."
date = "2022-01-20"
thumbnail = "assets/1_huggingface_logo.png"

def run_article():
    st.markdown("""
    # 🤗 Tips & Tricks Edition 1 
    # Create interactive blog posts with Streamlit and Spaces

    Welcome to the first post of the 🤗 Tips and Tricks blog! In this blog, I'll be sharing features you might not know about to leverage the Hub platform and Open Source ecosystem at its full extent. 

    In today's post, you'll learn how this blog was actually done! This is actually very easy and the setup takes less than 10 minutes!

    ## Workflow

    I'm a strong believer that there are different tools for different jobs. The tools we'll use today are:

    * **Streamlit**: A very cool Open Source library that allows to build apps in Python in a very straightforward way.
    * **GitHub**: The main platform in which we're going to be doing the coding. 
    * **Hugging Face Hub**: The platform in which the demo will be hosted using [Spaces](http://hf.co/spaces/launch), a platform through which you can freely share ML demos using Streamlit, Gradio or even static sites (HTML & JavaScript if you're into that stuff).

    Note: this is not a fully-fledged blog platform. There won't be subscribe options, for example, but it's a cool proof of concept that can be interesting for certain interactive articles.

    **Sure sure...but how does it work?**

    So you will have a Streamlit-based application in which you'll have your articles. The code will be in GitHub, and through GitHub Action workflows, the blog will be automatically sync'ed to a Hugging Face Space.

    **Sounds fun, let's do it!**

    Cool! So Nate has built a [nice template](https://github.com/nateraw/host-a-blog-on-huggingface-spaces) we can already use out of the box. Isn't that cool? Let's begin by clicking that **Fork** button in GitHub. Nice, so you're getting ready. Let's quickly explore what we have here

    - **.github/workflows/**: There is a GitHub Actions workflow that will automatically sync to the Hugging Face Hub each time you push into the repo.
    - **images/**: Well...it contains images.
    * **posts/**: You can write your articles here directly with Markdown!.
    * **app.py**: This is the main application file that has the structure of the blog.
    * **packages.txt** and **requirements.txt** allow you to specify any dependencies you'll want to have installed in the blog. If you want to show some cool visualization using library X, you can add X here!

    **Can we get this started?**

    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        Yes, let's do it. 
        
        First, create a [new Space](https://huggingface.co/new-space) at Hugging Face. You will need to specify the Streamlit SDK. Since it's still being setup, you can make it private so others don't see it. The Space can have any name you want.
        
        The second step is to create a [write token](https://huggingface.co/settings/token). This will allow GitHub to push whenever there are changes to the Space.

        Make sure to copy the token and...

        **I won't expose my token! They will hack me!**

        No worries, we'll be adding a **secret** in GitHub, which allows to add environment variables that can be accessed but not viewed by anyone. You can go to your **GitHub repo**, go to Settings -> SECRETS, and click ** New secret**. The name can be `HF_TOKEN` and the value is the one you got from the Hub.
    """)

    with col2:
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/1_streamlit_space.png", width=300)
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/1_token.png", width=300)

    

    st.markdown("""
    Now, if you go to **workflows/sync-to-hub**, you'll see the last line makes a reference to the original repo Space and your token. Let's switch the path to your own Space.

    So I changed

    ```
    run: git push https://nateraw:$HF_TOKEN@huggingface.co/spaces/nateraw/host-a-blog-on-huggingface-spaces main --force
    ```

    to

    ```
    run: git push https://osanseviero:$HF_TOKEN@huggingface.co/spaces/osanseviero/tips-and-tricks main --force
    ```

    As you can see, I never exposed my token!

    **Cool**

    What is even cooler is that now each time you do any change in the GitHub repository, it will be automatically deployed in HF Spaces and re-deployed!

    **What's next?**

    Well, you just finished the setup! There are a couple of places where you will want to change stuff and then write your first article. Once you're ready, you should make your Spaces repo public, share it in social media and get likes from the community!

    I hope this was useful! Until the next time!

    A Hacker Llama 🦙 
    """)
