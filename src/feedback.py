# src/feedback.py
def generate_feedback(result):
    fb = []
    if result['semantic'] < 0.5:
        fb.append("Answer seems to miss core concepts—explain the main steps more clearly.")
    else:
        fb.append("Good semantic coverage of the topic.")

    # keywords
    if result['matched'] == 0:
        fb.append("Your answer missed important keywords: " + ", ".join(result['keywords']))
    elif result['matched'] < len(result['keywords']):
        missing = [k for k in result['keywords'] if k.lower() not in " ".join(result.get('keywords',[])).lower()]
        # simpler: show keywords
        fb.append(f"Consider including more of these keywords: {', '.join(result['keywords'])}")

    # grammar
    if result['grammar_errors'] is not None and result['grammar_errors'] > 2:
        fb.append(f"Grammar: {result['grammar_errors']} issues found; check sentence structure and punctuation.")

    return " ".join(fb)
