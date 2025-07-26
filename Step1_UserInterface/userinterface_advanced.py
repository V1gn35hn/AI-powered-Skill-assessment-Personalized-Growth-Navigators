import streamlit as st

# --- Configure App ---
st.set_page_config(
    page_title="Intelligent Skill Assessment",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Advanced Theme-Aware Styling with Hover Effects ---
st.markdown("""
    <style>
        /* Import Google Fonts for premium typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Root variables for theme adaptability */
        :root {
            --primary-color: #4A90E2;
            --primary-hover: #3B7DD8;
            --secondary-color: #6C7B7F;
            --success-color: #00C851;
            --border-radius: 12px;
            --shadow-light: 0 2px 8px rgba(0,0,0,0.1);
            --shadow-hover: 0 4px 16px rgba(0,0,0,0.15);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Dark theme variables */
        @media (prefers-color-scheme: dark) {
            :root {
                --shadow-light: 0 2px 8px rgba(255,255,255,0.1);
                --shadow-hover: 0 4px 16px rgba(255,255,255,0.15);
            }
        }
        
        /* Global font enhancement */
        .main .block-container {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            max-width: 800px;
            padding-top: 2rem;
        }
        
        /* Enhanced title styling */
        h1 {
            font-weight: 700 !important;
            background: linear-gradient(135deg, var(--primary-color), #667eea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
            margin-bottom: 0.5rem !important;
        }
        
        /* Subtitle enhancement */
        .stCaption {
            text-align: center;
            font-style: italic;
            opacity: 0.8;
            margin-bottom: 2rem !important;
        }
        
        /* Section headers with improved spacing */
        h3 {
            font-weight: 600 !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--primary-color);
            position: relative;
        }
        
        h3::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 40px;
            height: 2px;
            background: linear-gradient(90deg, var(--primary-color), transparent);
        }
        
        /* Enhanced radio button styling with hover effects */
        div[data-testid="stRadio"] > div {
            background: rgba(74, 144, 226, 0.05);
            border-radius: var(--border-radius);
            padding: 1rem;
            margin: 0.5rem 0;
            border: 1px solid rgba(74, 144, 226, 0.1);
            transition: var(--transition);
        }
        
        div[data-testid="stRadio"] > div:hover {
            background: rgba(74, 144, 226, 0.1);
            border-color: var(--primary-color);
            box-shadow: var(--shadow-hover);
            transform: translateY(-2px);
        }
        
        /* Radio button options enhancement */
        div[data-baseweb="radio"] {
            margin: 0.75rem 0;
            padding: 0.5rem;
            border-radius: 8px;
            transition: var(--transition);
        }
        
        div[data-baseweb="radio"]:hover {
            background: rgba(74, 144, 226, 0.08);
            transform: translateX(4px);
        }
        
        /* Enhanced selectbox styling */
        div[data-testid="stSelectbox"] > div {
            background: rgba(74, 144, 226, 0.05);
            border-radius: var(--border-radius);
            padding: 1rem;
            border: 1px solid rgba(74, 144, 226, 0.1);
            transition: var(--transition);
        }
        
        div[data-testid="stSelectbox"] > div:hover {
            background: rgba(74, 144, 226, 0.1);
            border-color: var(--primary-color);
            box-shadow: var(--shadow-hover);
            transform: translateY(-2px);
        }
        
        /* Selectbox dropdown enhancement */
        .stSelectbox > div > div {
            border-radius: 8px !important;
            border: 2px solid rgba(74, 144, 226, 0.2) !important;
            transition: var(--transition) !important;
        }
        
        .stSelectbox > div > div:hover {
            border-color: var(--primary-color) !important;
            box-shadow: var(--shadow-light) !important;
        }
        
        /* Enhanced slider styling */
        div[data-testid="stSlider"] {
            background: rgba(74, 144, 226, 0.05);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(74, 144, 226, 0.1);
            transition: var(--transition);
        }
        
        div[data-testid="stSlider"]:hover {
            background: rgba(74, 144, 226, 0.1);
            border-color: var(--primary-color);
            box-shadow: var(--shadow-hover);
            transform: translateY(-2px);
        }
        
        /* Slider labels */
        .stSlider > div > div > div > div {
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--primary-color);
        }
        
        /* Premium button styling */
        .stButton {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, var(--primary-color), #667eea) !important;
            color: white !important;
            border: none !important;
            border-radius: var(--border-radius) !important;
            padding: 0.75rem 2rem !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
            box-shadow: var(--shadow-light) !important;
            transition: var(--transition) !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, var(--primary-hover), #5a67d8) !important;
            box-shadow: var(--shadow-hover) !important;
            transform: translateY(-3px) !important;
        }
        
        .stButton > button:active {
            transform: translateY(-1px) !important;
        }
        
        /* Button ripple effect */
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transition: width 0.6s, height 0.6s, top 0.6s, left 0.6s;
            transform: translate(-50%, -50%);
        }
        
        .stButton > button:active::before {
            width: 300px;
            height: 300px;
        }
        
        /* Enhanced success message */
        div[data-testid="stAlert"] {
            border-radius: var(--border-radius) !important;
            border-left: 4px solid var(--success-color) !important;
            box-shadow: var(--shadow-light) !important;
            animation: slideIn 0.5s ease-out !important;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Enhanced code block */
        div[data-testid="stCodeBlock"] {
            border-radius: var(--border-radius) !important;
            box-shadow: var(--shadow-light) !important;
            border: 1px solid rgba(74, 144, 226, 0.2) !important;
            animation: fadeIn 0.5s ease-in !important;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Divider enhancement */
        hr {
            margin: 2rem 0 !important;
            border: none !important;
            height: 2px !important;
            background: linear-gradient(90deg, transparent, var(--primary-color), transparent) !important;
            opacity: 0.3 !important;
        }
        
        /* Column hover effects */
        div[data-testid="column"] {
            transition: var(--transition);
        }
        
        div[data-testid="column"]:hover {
            transform: translateY(-2px);
        }
        
        /* Responsive enhancements */
        @media (max-width: 768px) {
            .main .block-container {
                padding-top: 1rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            
            h1 {
                font-size: 2rem !important;
            }
            
            .stButton > button {
                width: 100% !important;
            }
        }
        
        /* Focus accessibility */
        *:focus {
            outline: 2px solid var(--primary-color) !important;
            outline-offset: 2px !important;
        }
        
        /* Loading animation for interactive elements */
        .loading {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.7; }
            100% { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# --- Enhanced Title Section ---
st.title("🧠 Intelligent Skill Assessment")
st.divider()

# --- 🖥️ Enhanced Domain Selection ---
st.subheader("🖥️ Select a domain to evaluate.")

# Improved domain selection with better UX
domain_options = ["Aerodynamics", "Thermal", "ENSAG", "Crash"]
domain_descriptions = {
    "Aerodynamics": "Fluid dynamics and airflow analysis",
    "Thermal": "Heat transfer and thermal management",
    "ENSAG": "Snow & Soiling",
    "Crash": "Impact analysis and safety engineering"
}

# Create a more intuitive single selection
selected_domains = []
cols = st.columns(2)

for i, option in enumerate(domain_options):
    with cols[i % 2]:
        if st.checkbox(f"**{option}**", help=domain_descriptions[option], key=f"domain_{i}"):
            selected_domains.append(option)

# Ensure only one selection
if len(selected_domains) > 1:
    st.warning("⚠️ Please select only one domain. The last selection will be used.")
    domain = selected_domains[-1]
elif len(selected_domains) == 1:
    domain = selected_domains[0]
else:
    domain = "Aerodynamics"  # Default

st.info(f"🎯 **Selected Domain:** {domain}")
st.divider()




# --- 🧑‍🔧 Enhanced Role Selection ---
st.subheader("🛠️ Choose a role to evaluate")

role_options = ["Assembly Engineer", "Synthesis Engineer", "FOP Engineer"]
role_descriptions = {
    "Assembly Engineer": "Assembly engineers handle meshing tasks at the assembly level.",
    "Synthesis Engineer": "Builds a full-vehicle model by integrating all assemblies provided by assembly engineers.",
    "FOP Engineer": "Handles simulation setup, boundary conditions, and solver parameter configuration."
}

# Extract domain keyword from role for use in skill description
def get_domain_keyword(role):
    return role.split()[0]  # Takes the first word like "Assembly", "Synthesis", etc.

role = st.selectbox(
    label="Select the professional role to evaluate:",
    options=role_options,
    help="Choose the role that best matches your current or target position."
)

st.info(f"👤 **Selected Role:** {role}")
st.caption(role_descriptions[role])
st.divider()





# --- 📊 Enhanced Skill Level Selection ---
st.subheader("📈 What's Your Skill Level?")

# Define skill levels with placeholder for domain where applicable
skill_levels = ["L1 - Beginner", "L2 - Apprentice", "L3 - Independent", "L4 - Specialist"]

skill_levels_descriptions = {
    "L1 - Beginner": "🌱 Has no prior experience; relies heavily on guidelines and support from senior team members.",
    "L2 - Apprentice": "🌿 Has domain experience but is new to organizational guidelines; occasionally requires L3/L4 support.",
    "L3 - Independent": "🌳 Works independently and is proficient with guidelines; seeks L4 support only for critical decisions.",
    "L4 - Specialist": "🏆 Demonstrates expert-level competency across all role requirements."
}

# Let user choose a skill level
skill_level = st.radio(
    label="Choose your current skill level:",
    options=skill_levels,
    horizontal=True
)

# Display selected level and description
st.info(f"**Selected Skill Level:** {skill_level}")
st.caption(skill_levels_descriptions[skill_level])
st.divider()





# --- ⚙️ Enhanced Assessment Settings ---
st.subheader("⚙️ Customize Your Assessment")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**📊 Question Quantity**")
    question_count = st.slider(
        "Number of Questions", 
        min_value=10, 
        max_value=50, 
        value=20, 
        step=5,
        help="More questions = more comprehensive assessment"
    )
    
with col2:
    st.markdown("**🎯 Question Type Mix**")
    mcq_percent = st.slider(
        "Multiple Choice Percentage (%)", 
        min_value=0, 
        max_value=100, 
        value=60, 
        step=10,
        help="Balance between MCQ and open-ended questions"
    )

# Assessment preview
col1, col2 = st.columns(2)
with col1:
    mcq_count = int(question_count * mcq_percent / 100)
    st.metric("Multiple Choice Questions", mcq_count, "📝")
    
with col2:
    open_count = question_count - mcq_count
    st.metric("Open-ended Questions", open_count, "💭")

st.divider()

# --- 🚀 Enhanced Generate Assessment Button ---
st.markdown("### 🚀 Ready to Begin?")

if st.button("🚀 Generate Personalized Assessment", use_container_width=True):
    # Enhanced success feedback
    st.success("✅ **Assessment Successfully Generated!**")
    
    # Comprehensive assessment summary
    st.markdown("### 📋 Assessment Configuration")
    
    assessment_config = {
        "🌐 Domain": domain,
        "👤 Role": role,
        "📈 Skill Level": skill_level,
        "📊 Total Questions": question_count,
        "🎯 MCQ Questions": mcq_count,
        "💭 Open Questions": open_count,
        "⏱️ Estimated Time": f"{question_count * 2} minutes"
    }
    
    # Display in a beautiful format
    for key, value in assessment_config.items():
        st.write(f"**{key}:** {value}")
    
    # Detailed prompt generation
    st.markdown("### 🔧 Generated Assessment Prompt")
    
    prompt_text = f"""
🎯 INTELLIGENT SKILL ASSESSMENT CONFIGURATION
═══════════════════════════════════════════════

📋 ASSESSMENT PARAMETERS:
┌─ Domain Focus: {domain}
├─ Professional Role: {role}  
├─ Skill Level: {skill_level}
├─ Question Count: {question_count}
├─ MCQ Ratio: {mcq_percent}% ({mcq_count} questions)
├─ Open-ended: {100-mcq_percent}% ({open_count} questions)
└─ Estimated Duration: {question_count * 2} minutes

🎯 ASSESSMENT OBJECTIVES:
• Evaluate domain-specific technical knowledge
• Assess practical problem-solving capabilities
• Measure role-relevant competencies
• Provide skill level-appropriate challenge

🔍 QUESTION DISTRIBUTION:
• Multiple Choice: {mcq_count} questions (technical concepts, best practices)
• Open-ended: {open_count} questions (case studies, problem-solving)

⚡ GENERATED ON: {st.session_state.get('timestamp', 'Now')}
    """
    
    st.code(prompt_text, language="text")
    
    # Add download option
    st.download_button(
        label="📥 Download Assessment Configuration",
        data=prompt_text,
        file_name=f"assessment_config_{domain.lower()}_{role.replace(' ', '_').lower()}.txt",
        mime="text/plain"
    )

# --- Footer Enhancement ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; opacity: 0.7; font-size: 0.9rem; margin-top: 2rem;'>
        <p>🏆 <strong>Award-Winning Design</strong> • Built by Vignesh Narasimhan/p>
    </div>
    """, 
    unsafe_allow_html=True
)
