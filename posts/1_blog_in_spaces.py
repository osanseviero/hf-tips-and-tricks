import streamlit as st

from stmol import showmol
import py3Dmol

title = "T&T1 - Create interactive blog posts with Streamlit and Spaces"
description = "Learn about how to host interactive blogs using Streamlit, GitHub and Spaces."
date = "2022-01-20"
thumbnail = "assets/1_thumbnail.png"

def run_article():
    st.markdown("""
    # 🤗 Tips & Tricks Edition 1 
    # Create interactive blog posts with Streamlit and Spaces

    Welcome to the first post of the 🤗 Tips and Tricks blog! Each post can be read in <5 minutes and shares features you might not know about that will allow you to leverage the Hub platform and Open Source ecosystem to its full extent. 

    In today's post, you'll learn how this blog was actually done! This is actually very easy and the initial setup takes less than 10 minutes!

    **How much will it cost me? 🤑 **

    Nothing! We'll be using Open Source and free tools to achieve it.

    I'm a strong believer that there are different tools for different jobs, so today you'll use:

    * **Streamlit**: A very cool Open Source library that allows to build apps in Python in a very straightforward way.
    * **GitHub**: The main platform in which we're going to be hosting the code. 
    * **Hugging Face Hub**: The platform in which the demo will be hosted using [Spaces](http://hf.co/spaces/launch). Spaces is a platform through which you can freely share ML demos using Streamlit, Gradio or even static sites (HTML & JavaScript if you're into that stuff).

    **This is cool! Will I get subscriptions, likes, RSS, comments, ...**

    No 😢 this is not a fully-fledged blog platform. It's just a cool proof of concept that can be interesting for having interactive articles.

    **Sure sure...but how does it work?**

    So you will have a Streamlit-based application in which you'll have your articles. The code will be in GitHub, and through GitHub Action workflows, the blog will be automatically sync'ed to a Hugging Face Space. All the way automated!

    **Sounds fun, let's do it!**

    Cool! 🔥 So Nate has built a [nice template](https://github.com/nateraw/host-a-blog-on-huggingface-spaces) we can already use out of the box. Isn't that cool? Let's begin by clicking that **Fork** button in GitHub. Let's quickly explore what we have here

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
        
        First, create a [new Space](https://huggingface.co/new-space) at Hugging Face. You will need to specify the Streamlit SDK. Since it's still being written, you can make it private so others don't see it. The Space can have any name you want.
        
        The second step is to create a [write token](https://huggingface.co/settings/token). This will allow GitHub to push whenever there are changes to the Space.

        Make sure to copy the token and...

        **I won't expose my token! They will hack me! 🚨🚨🚨**

        No worries, we'll be adding a **secret** in GitHub, which allows to add environment variables that can be accessed but not viewed by anyone. You can go to your **GitHub repo**, go to Settings -> SECRETS, and click ** New secret**. The name can be `HF_TOKEN` and the value is the one you got from the Hub.

        🦙
    """)

    with col2:
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/1_streamlit_space.png", width=300)
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/1_token.png", width=300)

    

    st.markdown("""
    **Ok this is actually not that hard**

    I know!

    Now, if you go to your GitHub repo, to **workflows/sync-to-hub**, you'll see the last line makes a reference to the original Space repository and your token variable. Let's switch the path to your own Space.

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

    **Isn't this just the same as having my content in GitHub Pages?**

    The cool thing of doing the blog post with Streamlit is that your blog posts can be interactive.

    **I don't get it**

    Check this example to interact with a protein visualization! This is directly in the blog article and leverages [great work](https://towardsdatascience.com/molecular-visualization-in-streamlit-using-rdkit-and-py3dmol-part-2-657d28152753) done by the open source community.
    """)

    prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
    prot_list=prot_str.split(',')
    bcolor = st.color_picker('Pick A Color', '#6D73A6')
    protein=st.selectbox('select protein',prot_list)
    xyzview = py3Dmol.view(query='pdb:'+protein)
    xyzview.setStyle({"stick":{'color':'spectrum'}})
    xyzview.setBackgroundColor(bcolor)
    showmol(xyzview, height = 500,width=800)

    st.markdown("""
    **🤯 cool**

    Yes! Now imagine all the cool, ML interactive blogs you could have. You could nicely mix ML demos with great explanations in a very interactive way. Next time you release a model, you could embed it directly in the announcement article and readers would be able to try it out directly in their browsers!

    I hope this was useful! Until the next time!

    **A Hacker Llama 🦙**

    [osanseviero](https://twitter.com/osanseviero)
    """)