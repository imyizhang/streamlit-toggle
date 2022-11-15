# -*- coding: utf-8 -*-

import streamlit as st
from streamlit_space import space
from streamlit_toggle import theme

BADGE = '''[![Open in Streamlit][share_badge]][share_link] [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/imyizhang/streamlit-toggle/main/streamlit_app.py

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/imyizhang/streamlit-toggle

[pypi_badge]: https://badgen.net/pypi/v/streamlit-toggle?icon=pypi&color=black&label
[pypi_link]: https://www.pypi.org/project/streamlit-toggle
'''

QUICKSTART = '''import streamlit as st
from streamlit_toggle import toggle

st.title('Streamlit Toggle')
toggle()
'''


def app():
    # config
    st.set_page_config(
        page_title='Streamlit Toggle',
        page_icon='🔛',
        layout='centered',
        initial_sidebar_state='auto',
    )
    # sidebar
    st.sidebar.title('Theme')
    theme(st.sidebar, widget='checkbox', label='Dark', value=False)
    space(st.sidebar)
    st.sidebar.title('Spacing')
    lines = st.sidebar.slider('lines', 0, 10, 5, 1)
    space(st.sidebar)
    st.sidebar.caption(f'Streamlit {st.__version__}')
    # page
    st.title('Streamlit Toggle')
    st.markdown(BADGE)
    space()
    st.write('Add toggle switches to your Streamlit app.')
    space(lines=lines)
    st.header('Installation')
    st.code('pip install streamlit-toggle', language='bash')
    space(lines=lines)
    st.header('Quickstart')
    st.code(QUICKSTART, language='python')
    space(lines=lines)
    st.header('License')
    st.write(
        'Streamlit Toggle has an MIT license, as found in the [LICENSE](https://github.com/imyizhang/streamlit-toggle/blob/main/LICENSE) file.'
    )


if __name__ == '__main__':
    app()
