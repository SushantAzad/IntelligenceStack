import streamlit as st
import os
from litellm import completion
from dotenv import load_dotenv
from IPython.display import Markdown, display

load_dotenv(override=True)

gemini_api_key = os.getenv("GOOGLE_API_KEY")
from scraper import fetch_website_contents

# Your existing variables
# gemini_api_key = "..."
system_prompt = f"""You are an expert marketing strategist, brand designer, copywriter, and brochure creation specialist.

Your task is to transform a website summary into a polished, professional, visually structured brochure suitable for business presentation, client acquisition, investor communication, or marketing distribution.

Requirements:

1. Analyze the provided website summary and identify:
   - Company name
   - Industry
   - Products and services
   - Unique value proposition
   - Key benefits
   - Target audience
   - Competitive differentiators
   - Brand positioning

2. Create brochure content that is:
   - Professional and persuasive
   - Clear and concise
   - Marketing focused
   - Factually grounded in the provided summary
   - Free from unsupported claims

3. Structure the brochure using the following sections whenever information is available:

   - Cover Page
     - Company Name
     - Tagline
     - Hero Statement

   - About Us

   - Our Services / Products

   - Key Features

   - Why Choose Us

   - Benefits for Customers

   - Industries Served

   - Customer Value Proposition

   - Call to Action

   - Contact Information (only if provided)

4. Improve readability by:
   - Using compelling headlines
   - Using concise paragraphs
   - Including bullet points where appropriate
   - Maintaining a premium business tone

5. If information is missing:
   - Do not invent facts
   - Use neutral placeholders such as:
     [Contact Information Not Provided]

6. Output Format:

   # Brochure Title

   ## Cover Section

   ## About Us

   ## Services

   ## Features

   ## Why Choose Us

   ## Benefits

   ## Call to Action

7. Additionally provide:
   - Suggested brochure design theme
   - Suggested color palette
   - Suggested imagery style
   - Recommended brochure layout (bi fold, tri fold, A4, etc.)

Return only the completed brochure content and design recommendations."""


def gen_user_prompt(website):
    user_prompt = f"""Create a professional brochure using the website summary provided at the end of this prompt.

    Requirements:

    - Create brochure ready marketing content.
    - Maintain a professional and modern tone.
    - Highlight the company's core value proposition.
    - Emphasize customer benefits and business impact.
    - Use compelling headlines and concise content.
    - Do not include information that is not present in the summary.
    - If any information is missing, omit the section instead of making assumptions.

    Output Structure:

    # Brochure Title

    ## Cover Section
    - Headline
    - Tagline
    - Hero Description

    ## About Us

    ## Products and Services

    ## Key Features

    ## Benefits

    ## Why Choose Us

    ## Call To Action

    ## Design Recommendations
    - Theme
    - Color Palette
    - Imagery Style
    - Typography Style
    - Layout Recommendation

    Website Summary:"""
    content = fetch_website_contents(website)
    user_prompt += "/n".join(content)
    return user_prompt


st.set_page_config(page_title="Brochure Generator", page_icon="📄", layout="centered")

st.title("Brochure Generator")

website_link = st.text_input("Enter the company URL", placeholder="https://example.com")

st.markdown("### Examples")

col1, col2 = st.columns(2)

with col1:
    if st.button("sushantazad.vercel.app"):
        website_link = "https://sushantazad.vercel.app/"

with col2:
    if st.button("galaxyweblinks.com"):
        website_link = "https://www.galaxyweblinks.com/"


def stream_brochure(url):
    response = completion(
        model="gemini/gemini-2.5-flash",
        api_key=gemini_api_key,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": gen_user_prompt(url)},
        ],
        stream=True,
    )

    full_response = ""

    for chunk in response:
        delta = chunk.choices[0].delta.content

        if delta:
            full_response += delta
            yield full_response


if st.button("Generate Brochure"):

    if not website_link:
        st.warning("Please enter a company URL.")
        st.stop()

    st.markdown("---")
    st.subheader("Generated Brochure")

    output_placeholder = st.empty()

    for partial_response in stream_brochure(website_link):
        output_placeholder.markdown(partial_response)
