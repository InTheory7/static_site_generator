def extract_title(markdown):
    # Remove whitespace at the start of the markdown:
    markdown = markdown.strip()
    # Split the markdown at newlines:
    lines = markdown.split("\n")
    # If the document starts with '# ', return the first line after this:
    if lines[0].startswith("# "):
        return lines[0][2:].strip()
    # Otherwise, raise an exception:
    else:
        raise Exception("Markdown file does not have a level 1 heading for the page title.")