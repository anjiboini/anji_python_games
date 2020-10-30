import mechanize

# noinspection PyProtectedMember
from bs4 import beautifulsoup





mc = mechanize.Browser()

url ='https://www.findandtrace.com/trace-mobile-number-location'

mc.open(url)
mc.select_form('trace')
mc['mobilenumber'] = '9866618573'

res = mc.submit().read()
#print(res)

soup =beautifulsoup(res,'html.parser')
print(soup.prettify)