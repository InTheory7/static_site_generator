def markdown_to_blocks(markdown):
    # Make sure the input is a string:
    if not isinstance(markdown, str):
        raise Exception("Input must be a string")
    # Split the markdown input at double newlines:
    blocks = markdown.split("\n\n")
    # Remove whitespace from each block (without a for loop):
    new_blocks = list(map(lambda block: block.strip(), blocks))
    # Remove empty strings from the list (without a for loop):
    return list(filter(lambda block: block != ("" or "\n"), new_blocks))

from itertools import groupby

def block_to_block_type(block):
    # Make sure the input is a string:
    if not isinstance(block, str):
        raise Exception("Input must be a string")
    # Make sure the string isn't empty:
    if block.strip() == "":
        return "normal"
    
    # Check if the block is a heading:
    groups = []
    for _, group in groupby(block):
        groups.append(list(group))
    if (block[0] == "#") and (
            (len(groups[0]) >= 1) and (len(groups[0]) <= 6)
        ):
        return "heading"

    # Check if the block is code:
    if len(block) >= 6:
        if block[:3] == "```" and block[-3:] == "```":
            return "code"

    # Split the block at newlines:
    lines = block.split("\n")
    # Remove whitespace from each line (without a for loop):
    new_lines = list(map(lambda line: line.strip(), lines))
    print(new_lines)

    # Check if the block is a quote, unordered, or ordered list
    quote_true = True
    unordered_true = True
    ordered_true = True
    order_count = 0
    for line in new_lines:
        # Ignore empty strings in the list:
        if len(line) == 0:
            continue
        # Quote check:
        if line[0] != ">":
            quote_true = False
        # Unordered check:
        if len(line) > 2:
            bullet_point = False
            dash_point = False
            if line[:2] == "* ":
                bullet_point = True
            elif line[:2] == "- ":
                dash_point = True
            if (not bullet_point) and (not dash_point):
                unordered_true = False
        else:
            unordered_true = False
        # Ordered check:
        order_count += 1
        if len(line) > (int(order_count/10) + 1 + 2):
            if line[:(int(order_count/10) + 1 + 2)] != f"{order_count}. ":
                ordered_true = False
        else:
            ordered_true = False

    if quote_true:
        return "quote"
    if unordered_true:
        return "unordered_list"
    if ordered_true:
        return "ordered_list"
    
    # Otherwise it's a paragraph
    return "normal"