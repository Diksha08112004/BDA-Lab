from bs4 import BeautifulSoup

html = """
<html><body>
<a href="http://example.com">Example</a>
<a href="http://test.com">Test</a>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))