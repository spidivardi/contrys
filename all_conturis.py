__author__ = 'david vardi'
from csv import DictReader
from math import radians, cos, sin, asin, sqrt
from collections import defaultdict

style = '''<style>
body {background-color: #d0e4fe;}
h1 {color: #00008B;
    text-align: center;
    font-size: 30px;}
dt {color: #B22222;
    font-size: 25px;}
dd{font-style: italic;
    font-size: 20px;}
m{font-size: 20px;}
ol.f {list-style-type: decimal;}
l {
    float: left;
    width: 12em;
    text-decoration: none;
    color: white;
    background-color: #7FFF00;
    padding: 0.2em 0.8em;
    border-right: 1px solid white;
}

l:hover {
    background-color: #00FFFF;
}
</style>\n'''
indexstyle = '''<style>
body {background-color: #FAFAD2;}
h1   {text-align: center;
      font-size: 30px;
      color: #00008B;}
</style>\n'''
index3style = '''<style>
body {background-color: #FAFAD2;}
h1   {text-align: center;
      font-size: 30px;
      color: #0:
ol.f {list-style-type: decimal;}
      </style>\n'''


def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def continent_long_mame(con):
    continents = {'AS': 'Asia', 'AF': 'Africa', 'AN': 'Antarctica', 'EU': 'Europe', 'NA': 'North_America',
                  'OC': 'Oceania', 'SA': 'South_and_Central_America'}
    return continents[con]


def distance_from(contury_list, lon, lat):
    distance_list = []
    for i in contury_list:
        distance_list.append(('<li><a href ="{}.html">{}</a></li>'.format(i.shortName, i.name, ),
                              int(haversine(i.lon, i.lat, lon,
                                            lat), )))
    l = sorted(distance_list, key=lambda b: b[1])
    s = ''
    for i in l[1:16]:
        s += i[0]
        s += 'The distance is: {:,d}'.format(i[1])
    return s


class Contury:
    def __init__(self, lon, lat, capital, short_name, land, name, continent, population, languages):
        self.lat = lat
        self.lon = lon
        self.capital = capital
        self.shortName = short_name
        self.land = land
        self.name = name
        self.continent = continent
        self.population = population
        self.languages = languages

    def __str__(self):
        return 'State of {} located in {}'.format(self.name, self.continent)


def crate_html_file_index1(contury_list):
    israel_lat, israel_lon = 31.5, 34.75
    html_str = '{}<h1>index by distance from israel</h1><ul>\n\t'.format(indexstyle)
    for i in contury_list:
        html_str += '\n\t<li>{}: {:,d}</li>\n<a href ="{}.html">{}</a>'.format(i.name, int(
            haversine(i.lon, i.lat, israel_lon, israel_lat)), i.shortName, i.name)
    html_str += '\n</ul>'
    with open('/home/student/Desktop/home work/new html/index.html', 'w')as file:
        file.write(html_str)


def crate_html_file_index2(contury_list):
    html_str = '<h1>index by population</h1>'
    conturis = []
    for i in contury_list:
        conturis.append(
            ('<li>The population of <a href ="{}.html">{}</a> is:</li>'.format(i.shortName, i.name), i.population))
    l = sorted(conturis, key=lambda x: x[1], reverse=True)
    for i in l:
        html_str += i[0]
        html_str += '<dd>{:,d}</dd>'.format(i[1])
    with open('/home/student/Desktop/home work/new html/index1.html', 'w')as file:
        file.write(html_str)


def crate_html_file_index3(contury_list):
    a = defaultdict(list)
    html_str = '<h1>index by continent</h1>'
    for i in contury_list:
        a[i.continent].append('<li>{} <a href={}.html>{}</a></li>'.format(i.name, i.shortName, i.name))
    for k, v in a.items():
        html_str += '<li><a href=continent_{}.html>{}</a></li>'.format(k, k)
        with open('/home/student/Desktop/home work/new html/continent_' + k + '.html', 'w')as file:
            file.write('\n\n'.join(c for c in v))
    with open('/home/student/Desktop/home work/new html/index3.html', 'w')as file:
        file.write(html_str)


def menu(contury_list):
    l = []
    for i in contury_list:
        l.append(i.continent)
    st = ''
    for i in set(l):
        st += '<li><a href="continent_{}.html">{}</a></li>'.format(i, i)
    s = '''<style>body {
    padding: 0;
    margin: 0;
    font-family: Arial;
    font-size: 17px;
}
#nav {
    background-color: #222;
}
#nav_wrapper {
    width: 1000px;
    margin: 0 auto;
    text-align: left;
}
#nav ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
    position: relative;
    min-width: 200px;
}
#nav ul li {
    display: inline-block;
}
#nav ul li:hover {
    background-color: #333;
}
#nav ul li a, visited {
    color: #CCC;
    display: block;
    padding: 15px;
    text-decoration: none;
}
#nav ul li:hover ul {
    display: block;
}
#nav ul ul {
    display: none;
    position: absolute;
    background-color: #333;
    border: 5px solid #222;
    border-top: 0;
    margin-left: -5px;
}
#nav ul ul li {
    display: block;
}
#nav ul ul li a:hover {
    color: #699;
}</style>'''

    html_str = ''' <body background="map.jpg">
{} <div id="nav">
    <div id="nav_wrapper">
        <ul>
            <li><a href="index.html">index</a>
            </li>
            <li> <a href="index1.html">index by population</a>
            </li>
            <li> <a href="index3.html">index by continent</a>
                <ul>
                    {}
                </ul>
            </li>
        </ul>
    </div>
    <!-- Nav wrapper end -->
</div>
<!-- Nav end -->'''.format(s,st)

    with open('/home/student/Desktop/home work/new html/new.html', 'w')as file:
        file.write(html_str)


def crate_html_file(contury_list):
    for i in contury_list:
        html_str = ('''
            <html>\n
            {}
            <head>\n
            \t<title>{}</title>\n
            </head>\n
            <body>\n
            <body background="1.jpg">
            <h1>{}</h1>\n
            <dl>\n\n
            \t<dt>The Capital is:</dt>\n
            \t<dd>{}</dd>\n\n
            \t<dt>The population number is:</dt>\n
            \t<dd>{:,d}</dd>\n\n
            \t<dt>Land Area</dt>\n
            \t<dd>{} km<sup>2</sup></dd>\n\n
            \t<dt>The country is located in the continent:</dt>\n
            \t<dd>{}</dd>\n
            \t<dt>The language is:</dt>\n
            \t<dd>{}</dd>\n
            <li><m>15 countries are coming:</m><dd><ol class="f">{}</ol></dd></li>\n
            <l><a href ="index.html">Back to index</a></l>
            <l><a href ="index1.html">Back to index by population</a></l>
            <l><a href ="index3.html">Back to index by continent</a></l>
            </dl>\n
            </body>\n
            </html>''').format(style, i.name, i.name, i.capital, i.population, i.land, i.continent, i.languages,
                               distance_from(contury_list, i.lon, i.lat))
        with open('/home/student/Desktop/home work/new html/' + i.shortName + '.html', 'w')as file:
            file.write(html_str)


def play():
    contury_list = []
    with open('/home/student/Desktop/home work/html/countries.csv') as f:
        reader = DictReader(f)
        for d in reader:
            lon = float(d.get('lon'))
            lat = float(d.get('lat'))
            capital = d.get('capital')
            short_name = d.get('short_name')
            land = int(d.get('land')) if d.get('land') else d.get('land')
            name = d.get('name')
            continent = continent_long_mame(d.get('continent'))
            population = int(d.get('population'))
            languages = d.get('languages')
            contury_list.append(Contury(lon, lat, capital, short_name, land, name, continent, population, languages))
    crate_html_file_index1(contury_list)
    crate_html_file_index2(contury_list)
    crate_html_file_index3(contury_list)
    crate_html_file(contury_list)
    menu(contury_list)


play()
