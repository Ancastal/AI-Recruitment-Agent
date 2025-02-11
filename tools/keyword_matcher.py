import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    """Tokenize, remove stopwords, and lemmatize the text."""
    doc = nlp(text.lower())  # Convert to lowercase
    clean_tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(clean_tokens).lower()

def match_keywords(resume_text: str, keywords: list[str]) -> tuple[list[str], str]:
    """Match keywords in the resume to the job description.
    
    Returns:
        tuple containing (matched_keywords, decision)
    """
    # Preprocess both the resume and keywords
    processed_resume = preprocess_text(resume_text)
    processed_keywords = [preprocess_text(keyword) for keyword in keywords]
    
    # Find matching keywords
    keywords_found = [
        original_keyword 
        for original_keyword, processed_keyword in zip(keywords, processed_keywords)
        if processed_keyword in processed_resume
    ]
    
    print(f"Keywords found: {keywords_found}")
    # Make hiring decision
    decision = (
        "The candidate has passed the initial screening."
        if keywords_found
        else "The candidate has failed the initial screening. TERMINATE"
    )
    
    return keywords_found, decision

if __name__ == "__main__":
    resume = "I have 10 years of experience in software development"
    keywords = ["software", "development"]
    matched_keywords, decision = match_keywords(resume, keywords)
    print(f"Matched keywords: {matched_keywords}")
    print(f"Decision: {decision}")
