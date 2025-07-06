import streamlit as st
from insta_scraper import get_public_bio
import persona_analyzer

def show_persona_card(persona):
    st.markdown("### 🎯 AI-Generated TILT Persona Card")
    st.markdown(f"**Username:** @{persona['username']}")
    st.markdown(f"**Niche Category:** {persona['niche_category']}")
    st.markdown(f"**Bio:** {persona['bio'] or 'N/A'}")
    st.markdown(f"**Description:** {persona['description']}")

    st.markdown("**🔑 Keywords Detected in Bio**")
    detected = []
    for cat, kws in persona_analyzer.NICHE_CATEGORIES.items():
        for kw in kws:
            if kw in (persona['bio'] or "").lower():
                detected.append(kw)
    if detected:
        st.write(", ".join(set(detected)))
    else:
        st.write("No specific keywords detected.")

    st.markdown("**🔥 Suggested Hashtags**")
    st.write(", ".join(persona['hashtags']))

    st.markdown("**🎥 Reels Content Ideas**")
    for idea in persona['reels']:
        st.write(f"- {idea}")

    st.markdown("**📊 Estimated Follower Types**")
    st.bar_chart(persona['followers'])


def main():
    st.title("TILT — Find Your Niche")
    st.write(
        "Unlock insights about your Instagram community.\n"
        "Understand who follows you — whether you're a model, creative, musician, or multi-hyphenate."
    )

    username = st.text_input("📸 Enter a public Instagram username")

    if username:
        bio, url = get_public_bio(username)
        persona = persona_analyzer.generate_persona_card(username, bio, url)

        plan = st.radio(
            "Choose your plan:",
            ["Free Basic Analysis", "AI-Powered Detailed Analysis (Paid)"],
            index=0
        )

        if plan == "Free Basic Analysis":
            if persona['niche_category'] in ["TooMinimal"]:
                st.warning(
                    "🚧 This profile is too minimal for the free tool. "
                    "Upgrade to unlock an AI-powered deep dive with more personal insights."
                )
            else:
                show_persona_card(persona)

        elif plan == "AI-Powered Detailed Analysis (Paid)":
            st.info(
                "🔒 The AI-powered detailed version is coming soon! "
                "This will generate a custom in-depth report using advanced AI. "
                "Stay tuned and subscribe to be the first to try it!"
            )


if __name__ == "__main__":
    main()
