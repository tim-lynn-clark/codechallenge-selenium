"""
List of locators that are found at Blog  page of the Bluenote website.
"""

BLOG_URL = 'https://bluenotetherapeutics.com/post/'


def blog_links(button):
    """
    1-11
    """
    return f"(//ul[@class='flex-ns flex-wrap mhn1-ns mb4']//a)[{button}]"
