import streamlit as st
import streamlit.components.v1 as components

title = "T&T2 - Craft demos of private models"
description = "Build public, shareable models of private models."
date = "2022-01-27"
thumbnail = "assets/2_thumbnail.png"



def run_article():
    st.markdown("""
        # 🤗 Tips & Tricks Edition 2
        # Using private models in your public ML demos

        Welcome to a new post of 🤗 Tips and Tricks! Each post can be read in <5 minutes and shares features you might not know about that will allow you
        to leverage the Hub platform to its full extent. 

        In today's post, you'll learn how you can create public demos of your private models. This can be useful if you're not ready to share the model
        or are worried of ethical concerns, but would still like to share the work with the community to try it out.

        **Is this expensive?**

        It will cost...nothing! You can host private models on Hugging Face right now in a couple of clicks! Note: This works not just for transformers,
        but for any ML library!

        **Which is the model?**

        The super secret model we won't want to share publicly but still showcase is a super powerful Scikit-learn model for...wine quality classification!
        For the purposes of this demo, assume there exists a private model repository with `id=osanseviero/wine-quality`. 
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🍷Cheers. And what is the demo?**

        Let's build it right now! You first need to create a [new Space](https://huggingface.co/new-space). I like to use the Gradio SDK, but you are 
        also encouraged to try Streamlit and static Spaces.

        The second step is to create a [read token](https://huggingface.co/settings/token). A read token allows reading repositories, which is useful when 
        you don't need to modify them. This token will allow the Space to access the model from the private model repository.

        The third step is to create a secret in the Space, which you can do in the settings tab.

        **What's a secret?**

        If you hardcode your token, other people will be able to access your repository, which is what you're trying to avoid. Remember that the Space is 
        public so the code of the Space is also public! By using secrets + tokens, you are having a way in which the Space can read a private model repo 
        without exposing the raw model nor the token. Secrets can be very useful as well if you are making calls to APIs and don't want to expose it.

        So you can add a token, with any name you want, and paste the value you should have coppied from your settings. 
        """)

    with col2:
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/2_gradio_space.png", width=300)
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/2_token.png", width=300)
        st.image("https://github.com/osanseviero/hf-tips-and-tricks/raw/main/assets/2_secret.png", width=300)


    st.markdown("""
        **🤯 That's neat! What happens next?**

        The secret is made available available to the gradio Space as a. environment variable. Let's write the code for the Gradio demo.

        The first step is adding the `requirements.txt` files with used dependencies.

        ```
        scikit-learn
        joblib
        ```

        As always in Spaces, you create a file called `app.py`. Let's go through each section of the file

        1. Imports...nothing special

        ```python
        import joblib
        import os

        import gradio as gr

        from huggingface_hub import hf_hub_download
        ```

        2. Downloading model from private repo

        You can use `hf_hub_download` from the `huggingface_hub` library to download (and cache) a file from a model repository. Using the
        `use_auth_token` param, you can access the secret `TOKEN`, which has the read token you created before. I want to download the file
        `sklearn_model.joblib`, which is how `sklearn` encourages to save the models.


        ```python
        file_path = hf_hub_download("osanseviero/wine-quality", "sklearn_model.joblib",
                                use_auth_token=os.environ['TOKEN'])
        ```

        3. Loading model

        The path right now points to the cached local joblib model. You can easily load it now:
        
        ```python
        model = joblib.load(file_path)
        ```
        
        4. Inference function

        One of the most important concepts in Gradio is the inference function. The inference function receives an input and has an output. It can 
        receive multiple types of inputs (images, videos, audios, text, etc) and multiple outputs. This is a simple sklearn inference

        ```python
        def predict(data):
            return model.predict(data.to_numpy())
        ```

        5. Build and launch the interface

        Building Gradio interfaces is very simple. You need to specify the prediction function, the type of input and output. You can add more things such
        as the title and descriptions. In this case, the input is a dataframe since that's the kind of data managed by this model. 

        ```
        iface = gr.Interface(
            predict,
            title="Wine Quality predictor with SKLearn",
            inputs=gr.inputs.Dataframe(
                headers=headers,
                default=default,
            ),
            outputs="numpy",
        )
        iface.launch()
        ```

        We're done!!!!

        You can find the Space at [https://huggingface.co/spaces/osanseviero/wine_quality](https://huggingface.co/spaces/osanseviero/wine_quality)
        and try it yourself! It's not great, but the main idea of the article was to showcase a workflow of public demo with private model. This can also
        work for datasets! With Gradio, you can create datasets with flagged content from users!

        **Wait wait wait! I don't want to click more links!**

        Ahm...ok. The link above is cool because you can share it with anyone, but you can also show Spaces-hosted Gradio demos with a couple of
        HTML lines in your own website. Here you can see the Gradio Space.
    """)

    embed_gradio = components.html(
        """
        <head>
            <link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
            </head>
            <body>
            <div id="target"></div>
            <script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
            <script>
            launchGradioFromSpaces("osanseviero/wine_quality", "#target")
            </script>
            </body>
        """,
        height=600,
    )
    
    st.markdown("""
        **🤯 Is that...a Gradio Space embedded within a Streamlit Space about creating Spaces?**

        Yes, that's right! I hope this was useful! Until the next time!

        **A Hacker Llama 🦙**

        [osanseviero](https://twitter.com/osanseviero)
    """)

    