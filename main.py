import streamlit as st
from datetime import datetime, timedelta
import time
from PIL import Image

# Constants
WORK_MIN = 1  # Duration for work in minutes for demonstration
SHORT_BREAK_MIN = 1  # Duration for short break in minutes
LONG_BREAK_MIN = 1  # Duration for long break in minutes
WORK_SESSIONS_BEFORE_LONG_BREAK = 4  # Number of work sessions before a long break

# Initialize session state variables if they don't already exist
if "current_time" not in st.session_state:
    st.session_state.current_time = datetime.now()
if "timer_end" not in st.session_state:
    st.session_state.timer_end = datetime.now()
if "work_sessions_completed" not in st.session_state:
    st.session_state.work_sessions_completed = 0
if "timer_active" not in st.session_state:
    st.session_state.timer_active = False


# Functions
def start_timer(duration_minutes):
    st.session_state.current_time = datetime.now()
    st.session_state.timer_end = st.session_state.current_time + timedelta(
        minutes=duration_minutes
    )
    st.session_state.timer_active = True
    if duration_minutes == WORK_MIN:
        st.session_state.work_sessions_completed += 1


def reset_timer():
    st.session_state.timer_active = False
    st.session_state.work_sessions_completed = 0
    st.session_state.timer_end = datetime.now()  # Reset the timer_end variable


def display_time_remaining():
    now = datetime.now()
    if st.session_state.timer_active and now < st.session_state.timer_end:
        delta = st.session_state.timer_end - now
        minutes, seconds = divmod(delta.seconds, 60)
        st.header(f"{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        st.rerun()  # Replace st.experimental_rerun() with st.rerun()
    elif st.session_state.timer_active:
        st.session_state.timer_active = False
        st.balloons()  # Visual feedback
        st.audio("beep.wav")  # Replace with your own audio file path or URL
        st.rerun()  # Replace st.experimental_rerun() with st.rerun()


def display_checkmarks():
    checkmarks = "✔️" * (
        st.session_state.work_sessions_completed // WORK_SESSIONS_BEFORE_LONG_BREAK
    )
    st.sidebar.markdown(f"### Completed Cycles: {checkmarks}")


# Sidebar
st.sidebar.title("Pomodoro Timer Settings")
work_duration = st.sidebar.number_input(
    "Work Duration (min)", min_value=1, value=WORK_MIN, step=1
)
short_break_duration = st.sidebar.number_input(
    "Short Break Duration (min)", min_value=1, value=SHORT_BREAK_MIN, step=1
)
long_break_duration = st.sidebar.number_input(
    "Long Break Duration (min)", min_value=1, value=LONG_BREAK_MIN, step=1
)

# Main Page
st.title("Pomodoro Timer")
pom_img = Image.open("tomato.png")
timer_container = st.container()
with timer_container:
    st.image(pom_img)
    display_time_remaining()
display_checkmarks()

# Timer Controls
if not st.session_state.timer_active:
    if st.button("Start Work Timer"):
        start_timer(work_duration)
    if (
        st.session_state.work_sessions_completed > 0
        and st.session_state.work_sessions_completed % WORK_SESSIONS_BEFORE_LONG_BREAK
        == 0
    ):
        if st.button("Start Long Break Timer"):
            start_timer(long_break_duration)
    else:
        if st.button("Start Short Break Timer"):
            start_timer(short_break_duration)
if st.button("Reset Timer"):
    reset_timer()

# Keep the timer running in the background
while st.session_state.timer_active:
    display_time_remaining()  # Only call the function once per iteration
    st.rerun()  # Replace st.experimental_rerun() with st.rerun()

# Explanation and User Guide
st.markdown(
    """
This Pomodoro Timer helps you manage your work and break periods effectively. 
- Click **Start Work Timer** to begin a work session.
- After completing a session, choose to start a short break or a long break after four work sessions.
- **Reset Timer** clears the current progress and starts over.
- **Completed Cycles** show how many sets of 4 work sessions you've completed.
"""
)
