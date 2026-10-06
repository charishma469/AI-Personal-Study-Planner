import streamlit as st
from planner import create_plan, create_daily_schedule


st.set_page_config(
    page_title="AI Personal Study Planner",
    page_icon="📚"
)


st.title("📚 AI Personal Study Planner")

st.write(
    "Create a personalized study plan based on your subject, "
    "number of days, and study hours."
)


name = st.text_input("👤 Enter your name")


subject = st.selectbox(
    "📖 Select Subject",
    [
        "Python",
        "Java",
        "Data Structures",
        "Machine Learning"
    ]
)


days = st.number_input(
    "📅 How many days do you want to study?",
    min_value=1,
    max_value=30,
    value=7,
    step=1
)


study_hours = st.number_input(
    "⏰ How many hours can you study per day?",
    min_value=1,
    max_value=12,
    value=2,
    step=1
)


if st.button("🚀 Generate Study Plan"):

    if name.strip() == "":
        st.warning("⚠️ Please enter your name.")

    else:

        plan = create_plan(
            subject,
            days,
            study_hours
        )

        st.success(
            f"🎉 Hello {name}! Your {subject} study plan is ready."
        )


        st.subheader("📅 Your Study Plan")


        for day, details in plan.items():

            st.write(f"### {day}")

            st.write(
                f"📖 **Topic:** {details['topic']}"
            )

            st.write(
                f"⏰ **Study Time:** {details['hours']} hour(s)"
            )

            st.divider()


        st.subheader("🕐 Daily Study Schedule")


        schedule = create_daily_schedule(
            subject,
            study_hours
        )


        for item in schedule:

            st.write(
                f"**{item['time']}** — "
                f"{item['activity']} "
                f"({item['duration']})"
            )