import streamlit as st


def add_footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #6c757d;
        text-align: center;
        padding: 10px 0;
        font-size:14px;
    }
    </style>
    <div class="footer">
        Developed by Sivakrishna, Yamini, Sravani | © 2024 Recommender System Project | Prof. Magdalini
    </div>
    """, unsafe_allow_html=True)


def navigation_page():
    # Get current selection from the URL hash
    page = st.experimental_get_query_params().get("page", ["recommendations"])[0]

    if page == "recommendations":
        st.title("Recommendations")
        st.subheader("Get Personalized Recommendations")
        # Add your recommendation logic here

    elif page == "analysis":
        st.title("Analysis")
        st.subheader("Explore Data Insights")
        # Add analysis content here (tables, charts, etc.)


def add_header():
    st.markdown("""
    <style>
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-top: 10px;
    }

    .subheader {
        font-size: 18px;
        font-weight: normal;
        color: #6c757d;
        text-align: center;
        margin-bottom: 20px;
    }

    .top-nav {
        background-color: #f8f9fa;
        padding: 10px 0;
        border-bottom: 1px solid #ddd;
    }

    .stRadio div {
        display: flex;
        justify-content: center;
        gap: 30px;
    }

    .stRadio label {
        font-weight: bold;
        color: #007bff;
    }

    </style>
    <div class="header">Social Recommender System</div>
    <div class="subheader">Explore Recommendations and Analyze User Behavior</div>
    """, unsafe_allow_html=True)


def top_navigation():
    selected_tab = st.radio(
        "",
        ["About", "Recommendations", "Analysis"],
        horizontal=True,
        key="top_navigation_radio",
    )
    return selected_tab
