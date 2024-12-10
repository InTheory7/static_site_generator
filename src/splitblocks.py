def markdown_to_blocks(markdown):
    # Make sure the input is a string:
    if not isinstance(markdown, str):
        raise Exception("Input must be a string")
    # Split the markdown input at newlines:
    blocks = markdown.split("\n")
    # Remove whitespace from each block (without a for loop):
    new_blocks = list(map(lambda block: block.strip(), blocks))
    # Remove empty strings from the list (without a for loop):
    return list(filter(lambda block: block != "", new_blocks))