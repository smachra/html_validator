#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    equal = True 
    Ltags = []
    for tag in _extract_tags(html):
        if '/' not in tag: # if it is not an end tag then add to list of tags
            Ltags.append(tag)
        else: 
            if Ltags  == []: # if list of tags is empty then there is no balance so false
                equalnum = False 
            else:
                top = Ltags.pop()  # this line pops off last value and returns last value of a line
                if top[2:] not in tag[1:]:  #Because an index is given, top pops out that index  
                    equalnum = False
                #If elements going from index 2 onwards of the list tags is not in the list of tag 
                #from index 1 onwards then the tags do not balance themselves out
                #
    if equalnum and Ltags == []:
        return True 
    else:
        return False 

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    while len(html) != 0:
        left = html.find('<') # finds "" in line of code
        right = html.find('>')
        if left == -1 or right == -1:
            break
        tags.append(html[left:(right + 1)]) 
        html = html[(right + 1):]
    return tags 
