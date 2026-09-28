# -*- coding: utf-8 -*-
"""
Meta Data Viewer - Streamlit Web App
يعرض واجهة الويب التفاعلية المخصصة لفحص صفحات إعلانات ميتا وبياناتها.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتكون بعرض كامل وأنيقة
st.set_page_config(
    page_title="صفحات الإعلانات - Meta Data Viewer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إخفاء شريط ستريمليت العلوي وتوسيع الإطار ليشغل كامل الشاشة
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        width: 100% !important;
        min-height: 98vh !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# قراءة وعرض ملف index.html
html_path = Path(__file__).parent / "index.html"

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error("ملف index.html غير موجود في مسار التطبيق!")
