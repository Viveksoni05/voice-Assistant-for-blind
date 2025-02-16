import re


def extract_yt_term(command):
    # Define the regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern, command ,re.IGNORECASE)
    return match.group(1) if match else None


def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string

def extract_lang(query):
    match = re.search(r"(\w+) .* translate into ([\w\s]+)", query)

    if match:
        text = match.group(1)
        lang = match.group(2)
        return lang
    else:
        return None

def extract_text(query):
    match = re.search(r"([\w\s]+?)(?=\s+translate into)\s+translate into\s+([\w\s]+)", query)

    if match:
        text = match.group(1)
        lang = match.group(2)
        return text
    else:
        return None