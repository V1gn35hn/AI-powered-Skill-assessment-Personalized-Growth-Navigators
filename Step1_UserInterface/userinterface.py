import streamlit as st

st.set_page_config(page_title="Intelligent Skill Assessment System", layout="centered")

st.title("🎯 Intelligent Skill Assessment System")

# Section 1: Role
role = st.selectbox("🔧 Select Role", ["Assembly Engineer", "Synthesis Engineer", "FOP Engineer"])

# Section 2: Skill Level
skill_level = st.radio(
    "📈 Select Skill Level",
    ["L1 - Beginner", "L2 - Apprentice", "L3 - Independent", "L4 - Specialist"]
)

# Section 3: Number of Questions
question_count = st.radio("❓ Number of Questions", [10, 20, 30])

# Section 4: Percentage of MCQs
mcq_percent = st.slider("📊 Percentage of MCQs", 0, 100, step=10)

# Generate Button
if st.button("🎯 Generate Assessment"):
    st.success("✅ Prompt Generated!")
    st.code(f'''Prompt Query:
Role: {role}
Skill Level: {skill_level}
Number of Questions: {question_count}
MCQ Percentage: {mcq_percent}%
''', language="text")

# Summary
st.markdown("### 🧾 Summary")
st.write(f"👤 **Role**: {role}")
st.write(f"📈 **Skill Level**: {skill_level}")
st.write(f"❓ **Questions**: {question_count}")
st.write(f"📊 **MCQs**: {mcq_percent}%")
