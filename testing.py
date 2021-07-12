'''
from bs4 import BeautifulSoup

page = """
<body class="container1280">
<table>
    <tr>
        <td class="image">
           <a href="/target/tt0111161/" title="Target Text 1">
            <img alt="target img" height="74" src="img src url" title="image title" width="54"/>
           </a>
        </td>
        
        <td class="title">
           <span class="wlb_wrapper" data-caller-name="search" data-size="small" data-tconst="tt0111161">
           </span>

           <a href="/target/tt0111161/">
            Other Text
           </a>

           <span class="year_type">
            (2013)
           </span>
        </td>
    </tr>
</table>
</body>
"""
soup = BeautifulSoup(page)
tbl = soup.find('table')
rows = tbl.findAll('tr')
for row in rows:
    cols = row.find_all('td')
    for col in cols:
        if col.has_attr('class') and col['class'][0] == 'image':
            hrefs = col.find_all('a')
            for href in hrefs:
                print(href.get('title'))

        elif col.has_attr('class') and col['class'][0] == 'title':
            spans = col.find_all('span')
            for span in spans:
                if span.has_attr('class') and span['class'][0] == 'wlb_wrapper':
                    print(span.get('data-tconst'))

exit()
'''


import requests
from bs4 import BeautifulSoup
from IPython.core.display import HTML
from requests.sessions import session
                         

myhtml = """
<body>
    <div class="abc">
        <div class="cbd", id="123">
        HIT
        </div>
        <div class="pnc_wrapper" id="456"></div>
    </div>
    <div class="efgh"></div>
    <div class="okjh"></div>

</body>
"""
content = BeautifulSoup(myhtml, "html.parser")
rows = content.findAll('div')
for row in rows:
    subrows = row.findAll('div')
    if len(subrows) > 0:
        for item in subrows:
            print(item.get('id'))
print("done")










