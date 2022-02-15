"""
List of locators that are found at why page of Blue Note website.
"""

WHY_URL = 'https://bluenotetherapeutics.com/why/'
CANCER_RELATED_DISTRESS_TITLE = "//div[@class='mr5-l']//h1"


def research_links(button):
    """ 
    1- 19 
    """
    return f"(//div[@class='cms small']//a)[{button}]"
