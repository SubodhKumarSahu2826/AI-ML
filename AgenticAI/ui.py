import streamlit as st
from youtube_analyzer import build_youtube_agent

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="🎥 AI YouTube Video Analyzer",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

/* Hero Title */
.hero-title{
    text-align:center;
    font-size:42px;
    font-weight:800;
    color:white;
    margin-bottom:5px;
}

.hero-subtitle{
    text-align:center;
    color:#B0B0B0;
    font-size:18px;
    margin-bottom:30px;
}

/* Card */
.stApp {
    background: linear-gradient(135deg,#0F172A,#111827,#1E293B);
}

/* Analysis Box */
.result-box{
    background:#111827;
    border-radius:15px;
    padding:25px;
    border:1px solid #374151;
    box-shadow:0px 5px 20px rgba(0,0,0,.35);
}

/* Footer */
.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    font-size:14px;
}

/* Button */
div.stButton > button:first-child{
    width:100%;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
    background:linear-gradient(90deg,#ff416c,#ff4b2b);
    color:white;
    border:none;
}

div.stButton > button:first-child:hover{
    background:linear-gradient(90deg,#ff4b2b,#ff416c);
    color:white;
}

/* Input */
.stTextInput>div>div>input{
    border-radius:10px;
    padding:12px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.title("📌 Instructions")

    st.info("""
1. Paste any YouTube video URL.

2. Click **Analyze Video**.

3. Wait a few seconds.

4. Read the AI-generated report.
""")

    st.markdown("---")

    st.success("Powered by AI Agent")

# ---------------- HEADER ---------------- #
st.markdown(
    """
<div class='hero-title'>
🎥 AI YouTube Video Analyzer
</div>

<div class='hero-subtitle'>
Analyze any YouTube video using AI and generate an intelligent report in seconds.
</div>
""",
    unsafe_allow_html=True,
)

# ---------------- LOAD AGENT ---------------- #
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# ---------------- INPUT ---------------- #
video_url = st.text_input(
    "🔗 Enter YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=..."
)

button = st.button("🚀 Analyze Video")

# ---------------- PROCESS ---------------- #
if video_url and button:

    progress = st.progress(0)

    with st.spinner("🤖 AI is watching the video..."):

        for i in range(100):
            progress.progress(i + 1)

        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    progress.empty()

    st.success("✅ Analysis Completed Successfully!")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="result-box">
        <h3>📊 Analysis Report</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(response.content)

elif button:
    st.warning("Please enter a valid YouTube URL.")

# ---------------- FOOTER ---------------- #
st.markdown(
    """
<div class='footer'>
Made with ❤️ using Streamlit • LangChain • AI Agents
</div>
""",
    unsafe_allow_html=True,
)