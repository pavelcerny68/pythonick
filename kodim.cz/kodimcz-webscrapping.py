#  webscrapping
from requests_html import HTML

with open("sample.html", encoding="utf-8") as soubor:
    obsah = soubor.read()

html = HTML(html=obsah)

for odstavec in html.find("p"):
    print(odstavec.text)

html.find(".sekce1")

for odkaz in html.find("a"):
    print(odkaz.attrs["href"])

html.find("h1, h2")
html.find('ol[type="a"]')
html.find(".sekce1 p")
html.find(".sekce1 > p")
html.find('ol[type="a"] li')

print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

from requests_html import HTMLSession

session = HTMLSession()
stranka = session.get("https://apps.kodim.cz/python-data/scrape")
for odstavec in stranka.html.find("p"):
    print(odstavec.text)

print(stranka.html.html)
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

from requests_html import HTMLSession

session = HTMLSession()
stranka = session.get("https://react-shopping-cart-67954.firebaseapp.com/")
stranka.html.render(sleep=5)

print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
pohyby = [
    746,
    52,
    -749,
    -63,
    71,
    958,
    157,
    -1223,
    -1509,
    -285,
    -350,
    728,
    -260,
    809,
    -164,
    243,
    -238,
    233,
    -646,
    -82,
    -275,
    179,
    417,
    149,
    301,
    957,
    -711,
    376,
    421,
    -15,
    -663,
]
import pandas
import datetime as dt

datumy = [dt.date(2019, 3, d) for d in range(1, 32)]
ucet = pandas.Series(pohyby, index=datumy)
ucet.plot()
plt.show()
ucet.cumsum().plot()
plt.show()
ucet.plot(kind="bar", color="yellow", grid=True)
plt.show()
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
muzi = pandas.Series(
    [
        179.3,
        183.7,
        181.4,
        176.0,
        183.6,
        184.7,
        163.4,
        180.3,
        167.5,
        166.8,
        173.5,
        172.5,
        173.0,
        177.6,
        176.0,
        179.5,
        182.6,
        172.0,
        183.2,
        177.0,
        176.2,
        175.7,
        174.3,
        180.3,
        184.9,
        171.1,
        182.3,
        169.7,
        181.3,
        188.8,
        176.8,
        159.0,
        180.3,
        198.5,
        185.8,
        191.0,
        170.9,
        196.0,
        183.3,
        183.0,
        189.9,
        184.8,
        184.0,
        183.1,
        184.0,
        190.7,
        191.7,
        187.8,
        177.5,
        177.5,
        189.2,
        188.4,
        195.0,
        204.2,
        180.2,
        181.3,
        178.2,
        182.6,
        172.1,
        175.7,
        180.7,
        181.2,
        165.0,
        188.6,
    ]
)
muzi.hist()
plt.show()
muzi.plot(kind="box", whis=[0, 100])
plt.show()
