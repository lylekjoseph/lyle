from requests_html import HTML, HTMLSession

session = HTMLSession()
r= session.get('http://python-requests.org/')
r.html.render()

name = r.html.find('ProductSearch-HolidaySearch-MuiBox-root.ProductSearch-HolidaySearch-fctg-product-search520.ProductSearch-HolidaySearch-MuiGrid-root.ProductSearch-HolidaySearch-fctg-product-search504.ProductSearch-HolidaySearch-MuiGrid-item.ProductSearch-HolidaySearch-MuiGrid-grid-xs-6')
