import streamlit as st
import random

st.set_page_config(page_title="AI Business Internship Simulator")
st.title("🤖 AI-Powered Virtual Business Internship")

# Step 1: Onboarding
companies = ["Acme Corp", "TechNova", "GreenFuture", "RetailX", "FinEdge"]
roles = ["Marketing Intern", "Finance Intern", "Strategy Intern", "Operations Intern"]

if "assigned_company" not in st.session_state:
    st.session_state.assigned_company = random.choice(companies)
    st.session_state.assigned_role = random.choice(roles)

st.subheader(f"🏢 Welcome to {st.session_state.assigned_company}!")
st.write(f"You've been hired as a **{st.session_state.assigned_role}**. Get ready to solve real-world business challenges!")

# Step 2: Challenge generation
challenges = {
    "Marketing Intern": {
        "question": "Your company wants to increase product sales by 20%. Which strategy should you choose?",
        "options": {
            "A": "Invest in social media ads targeting Gen Z",
            "B": "Launch a referral program with discounts",
            "C": "Expand partnerships with influencers"
        },
        "best": "A"
    },
    "Finance Intern": {
        "question": "The company is running low on cash. What do you recommend?",
        "options": {
            "A": "Raise venture capital funding",
            "B": "Cut operational expenses significantly",
            "C": "Launch a new product line to increase revenue"
        },
        "best": "B"
    },
    "Strategy Intern": {
        "question": "A competitor has launched a similar product at a lower price. What's your move?",
        "options": {
            "A": "Reduce prices to match",
            "B": "Emphasize your product's unique value",
            "C": "Offer bundled deals"
        },
        "best": "B"
    },
    "Operations Intern": {
        "question": "Supply chain delays are impacting deliveries. What do you do?",
        "options": {
            "A": "Increase local suppliers",
            "B": "Offer discounts for delays",
            "C": "Stockpile inventory"
        },
        "best": "A"
    }
}

role = st.session_state.assigned_role
challenge = challenges[role]

st.subheader("📌 Business Challenge")
st.write(challenge["question"])

# Step 3: User decision
choice = st.radio("Select your decision:", list(challenge["options"].keys()), format_func=lambda x: f"{x}) {challenge['options'][x]}")

# Step 4: Submit & Feedback
if st.button("Submit Decision"):
    if choice == challenge["best"]:
        feedback = "✅ Great choice! This strategy aligns with best practices."
        score = 95
    else:
        feedback = f"⚠️ Consider a better strategy next time. The best choice was {challenge['best']}) {challenge['options'][challenge['best']]}"
        score = 70

    st.success("**Internship Report**")
    st.write(f"**Your Role:** {role}")
    st.write(f"**Your Decision:** {choice}) {challenge['options'][choice]}")
    st.write(f"**AI Feedback:** {feedback}")
    st.metric(label="Performance Score", value=f"{score}/100")
