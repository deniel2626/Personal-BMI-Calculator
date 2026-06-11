import streamlit as st
# PAGE CONFIG
st.set_page_config(
    page_title="Deniel's BMI Calculator",
    layout="wide"
)
# LIGHT / DARK MODE

title_col, toggle_col = st.columns([6, 1])

with title_col:
    st.markdown(
        "<h1 style='text-align:center;'>Personal BMI Calculator</h1>",
        unsafe_allow_html=True
    )

with toggle_col:
    dark_mode = st.toggle("🌙")

if dark_mode:

    st.markdown("""
    <style>

    .stApp {
        background-color: #0F172A;
    }

    h1, h2, h3, p, label {
        color: white !important;
    }

    /* Inputs */
    input, textarea {
        color: white !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: #1E293B;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #334155;
    }

    /* Button */
    .stButton > button {
        background-color: #2563EB;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        border: none;
    }

    /* Expanders */
    [data-testid="stExpander"] {
        background-color: #1E293B;
        border-radius: 10px;
        border: 1px solid #334155;
    }

    [data-testid="stExpander"] summary {
        color: white !important;
        font-weight: 600;
    }

    [data-testid="stExpander"] summary:hover {
        color: #FFFFFF !important;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp {
        background-color: #B0E0E6;
    }

    h1, h2, h3, p, label {
        color: #0F172A !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #D6EAF0;
    }

    /* Button */
    .stButton > button {
        background-color: #2563EB;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        border: none;
    }

    .stButton button p {
        color: white !important;
    }

    /* Expanders */
    [data-testid="stExpander"] {
        background-color: white;
        border-radius: 10px;
        border: 1px solid #D6EAF0;
    }

    [data-testid="stExpander"] summary {
        color: #0F172A !important;
        font-weight: 600;
    }

    [data-testid="stExpander"] summary:hover {
        color: #2563EB !important;
    }

    </style>
    """, unsafe_allow_html=True)
# Layout
col1, spacer, col2 = st.columns([.5, 0.1, .5])
# ==========================
# INPUT SECTION
# ==========================

with col1:

    st.header("Personal Information")

    name = st.text_input("What is your name?")
    age = st.number_input("What is your age?", min_value=0, step=1)
    address = st.text_input("Where do you live?")
    gender = st.selectbox(
        "What is your gender?",
        ["Male", "Female", "Other"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.header("Body Measurements")

    weight = st.number_input(
        "What is your weight (kg)?",
        min_value=0.0
    )

    height = st.number_input(
        "What is your height (cm)?",
        min_value=0.0
    )

    st.markdown("<br>", unsafe_allow_html=True)

    calculate = st.button(
        "Calculate BMI",
        use_container_width=True
    )

# ==========================
# RESULT SECTION
# ==========================

with col2:

    st.header("Results:")

    if calculate:

        if height == 0:
            st.error("Height cannot be zero.")
            st.stop()

        bmi = weight / ((height / 100) ** 2)

        # User Summary
        st.info(
            "👤 " + name +
            " | " + gender +
            " | " + address
        )

        if age >= 18:
            st.success("You are an Adult")
        else:
            st.info("You are a Minor")

        st.metric("BMI", round(bmi, 1))

        # ==========================
        # UNDERWEIGHT
        # ==========================

        if bmi < 18.5:

            target_weight = 18.5 * ((height / 100) ** 2)
            weight_to_gain = target_weight - weight

            colA, colB, colC = st.columns(3)

            colA.metric(
                "Current Weight",
                round(weight, 1)
            )

            colB.metric(
                "Target Weight",
                round(target_weight, 1)
            )

            colC.metric(
                "Weight To Gain",
                round(weight_to_gain, 1)
            )

            st.warning("Underweight")

            st.markdown("---")

            with st.expander("📋 Suggested Plan"):

                st.write("• Increase daily calorie intake")
                st.write("• Eat 4 to 6 meals per day")
                st.write("• Increase protein intake")
                st.write("• Do strength training")
                st.write("• Get 7 to 9 hours of sleep")

            with st.expander("🍽 Recommended Foods"):

                st.write("• Eggs")
                st.write("• Chicken Breast")
                st.write("• Rice")
                st.write("• Oatmeal")
                st.write("• Milk")
                st.write("• Peanut Butter")
                st.write("• Bananas")

            with st.expander("🏋 Recommended Exercises"):

                st.write("• Push-ups: 3 sets of 10 reps")
                st.write("• Squats: 3 sets of 15 reps")
                st.write("• Pull-ups: 3 sets of 3 reps")
                st.write("• Weight Training: 3 times per week")

        # ==========================
        # NORMAL
        # ==========================

        elif bmi < 25:

            st.success("✅ Normal Weight - Keep it up!")

        # ==========================
        # OVERWEIGHT
        # ==========================

        elif bmi < 30:

            target_weight = 25 * ((height / 100) ** 2)
            weight_to_reduce = weight - target_weight

            calories_to_burn = weight_to_reduce * 7700
            steps_needed = weight_to_reduce * 170000

            colA, colB, colC = st.columns(3)

            colA.metric(
                "Current Weight",
                round(weight, 1)
            )

            colB.metric(
                "Target Weight",
                round(target_weight, 1)
            )

            colC.metric(
                "Weight To Lose",
                round(weight_to_reduce, 1)
            )

            st.warning("Overweight")

            colD, colE = st.columns(2)

            colD.metric(
                "Calories To Burn",
                f"{round(calories_to_burn):,}"
            )

            colE.metric(
                "Estimated Steps",
                f"{round(steps_needed):,}"
            )

            st.markdown("---")

            with st.expander("📋 Suggested Plan"):

                st.write("• Walk 10,000 steps per day")
                st.write("• Avoid sugary drinks")
                st.write("• Eat more vegetables and protein")
                st.write("• Aim to lose 0.5 kg per week")

        # ==========================
        # OBESE
        # ==========================

        else:

            st.error("🚨 Obese")

            st.write(
                "Consider consulting a healthcare professional and creating a structured nutrition and exercise plan."
            )