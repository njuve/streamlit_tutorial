import streamlit as st

def write():
    st.title("Multiple pages with streamlit")
    st.subheader("index page")
    st.markdown(
        """
        We create a app with a index page and other pages (`page1`, `page2`).
        The index page `app.py`:
        ```py
            import streamlit as st
            import page1
            import page2

            PAGES = {
                'page1': page1,
                'page2': page2
            }

            st.sidebar.title("Navigation")
            selection = st.sidebar.selectbox('pages', list(PAGES.keys()))

            PAGES[selection].write()
        ```
        Namely,
        - import each page file `page1.py` and `page2.py`
        - `page1` and `page2` has a method `write()`

        Then we have to explain a structure of `page1` and `page2` and a method `write()`.
        """
    )
    st.subheader("Page structures and a write method")
    st.markdown(
        """
        Page files structure is as follows:
        ```py
            import streamlit as st

            def write():
                st.title('Page1')
                ...
        ```
        """
    )