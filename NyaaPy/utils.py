'''
    Module utils
'''

import re
from lxml import etree
from pprint import pprint


def nyaa_categories(b):
    c = b.replace('?c=', '')
    cats = c.split('_')

    cat = cats[0]
    subcat = cats[1]

    categories = {
        "1": {
            "name": "Anime",
            "subcats": {
                "1": "Anime Music Video",
                "2": "English-translated",
                "3": "Non-English-translated",
                "4": "Raw"
            }
        },
        "2": {
            "name": "Audio",
            "subcats": {
                "1": "Lossless",
                "2": "Lossy"
            }
        },
        "3": {
            "name": "Literature",
            "subcats": {
                "1": "English-translated",
                "2": "Non-English-translated",
                "3": "Raw"
            }
        },
        "4": {
            "name": "Live Action",
            "subcats": {
                "1": "English-translated",
                "2": "Idol/Promotional Video",
                "3": "Non-English-translated",
                "4": "Raw"
            }
        },
        "5": {
            "name": "Pictures",
            "subcats": {
                "1": "Graphics",
                "2": "Photos"
            }
        },
        "6": {
            "name": "Software",
            "subcats": {
                "1": "Applications",
                "2": "Games"
            }
        }
    }

    try:
        category_name = "{} - {}".format(
            categories[cat]['name'], categories[cat]['subcats'][subcat])
    except Exception:
        pass

    return category_name


def parse_nyaa(request_text, limit):
    parser = etree.HTMLParser()
    tree = etree.fromstring(request_text, parser)

    torrents = []

    # Going through table rows
    for tr in tree.xpath("//tbody//tr")[:limit]:
        block = []

        for td in tr.xpath("./td"):
            for link in td.xpath("./a"):

                href = link.attrib.get("href").split('/')[-1]

                # Only caring about non-comment pages.
                if href[-9:] != "#comments":
                    block.append(href)

                    if link.text and link.text.strip():
                        block.append(link.text.strip())

            if td.text and td.text.strip():
                block.append(td.text.strip())

        # Add type of torrent based on tr class.
        if 'danger' in tr.attrib.get("class"):
            block.append("remake")
        elif 'success' in tr.attrib.get("class"):
            block.append("trusted")
        else:
            block.append("default")

        # Create torrent object
        try:
            torrent = {
                'id': block[1],
                'category': nyaa_categories(block[0]),
                'url': "https://nyaa.si/view/{}".format(block[1]),
                'name': block[2],
                'download_url': "https://nyaa.si/download/{}".format(block[3]),
                'magnet': block[4],
                'size': block[5],
                'date': block[6],
                'seeders': block[7],
                'leechers': block[8],
                'completed_downloads': block[9],
                'type': block[10]
            }
            torrents.append(torrent)
        except IndexError:
            pass
    return torrents


def parse_single(request_text):
    parser = etree.HTMLParser()
    tree = etree.fromstring(request_text, parser)

    torrent = {}
    data = []
    torrent_files = []

    # Find basic uploader info & torrent stats
    for row in tree.xpath("//div[@class='row']"):
        for div_text in row.xpath("./div[@class='col-md-5']//text()"):
            d = div_text.strip()
            if d:
                data.append(d)

    # Find files, we need only text of the li element(s).
    # Sorry about Pycodestyle aka PEP8 (E501) error
    for el in tree.xpath("//div[contains(@class, 'torrent-file-list')]//li/text()"):
        if el.rstrip():
            torrent_files.append(el)

    torrent['title'] = \
        tree.xpath("//h3[@class='panel-title']/text()")[0].strip()
    torrent['category'] = data[0]
    torrent['uploader'] = data[4]
    torrent['uploader_profile'] = "http://nyaa.si/user/{}".format(data[4])
    torrent['website'] = data[6]
    torrent['size'] = data[8]
    torrent['date'] = data[3]
    torrent['seeders'] = data[5]
    torrent['leechers'] = data[7]
    torrent['completed'] = data[9]
    torrent['hash'] = data[10]
    torrent['files'] = torrent_files

    torrent['description'] = ""
    for s in tree.xpath("//div[@id='torrent-description']"):
        torrent['description'] += s.text

    return torrent


def parse_sukebei(table_rows, limit):
    if limit == 0:
        limit = len(table_rows)

    torrents = []

    for row in table_rows[:limit]:
        block = []

        for td in row.find_all('td'):
            for link in td.find_all('a'):
                if link.get('href')[-9:] != '#comments':
                    block.append(link.get('href'))
                    block.append(link.text.rstrip())

            if td.text.rstrip():
                block.append(td.text.rstrip())

            try:
                torrent = {
                    'id': block[1].replace("/view/", ""),
                    'category': sukebei_categories(block[0]),
                    'url': "http://sukebei.nyaa.si{}".format(block[1]),
                    'name': block[2],
                    'download_url': "http://sukebei.nyaa.si{}".format(
                        block[4]),
                    'magnet': block[5],
                    'size': block[6],
                    'date': block[7],
                    'seeders': block[8],
                    'leechers': block[9],
                    'completed_downloads': block[10],
                }
            except IndexError as ie:
                pass

            torrents.append(torrent)

    return torrents


def sukebei_categories(b):
    c = b.replace('/?c=', '')
    cats = c.split('_')

    cat = cats[0]
    subcat = cats[1]

    categories = {
        "1": {
            "name": "Art",
            "subcats": {
                "1": "Anime",
                "2": "Doujinshi",
                "3": "Games",
                "4": "Manga",
                "5": "Pictures",
            }
        },
        "2": {
            "name": "Real Life",
            "subcats": {
                "1": "Photobooks & Pictures",
                "2": "Videos"
            }
        }
    }

    try:
        category_name = "{} - {}".format(
            categories[cat]['name'], categories[cat]['subcats'][subcat])
    except Exception:
        pass

    return category_name


# Pantsu Utils
def query_builder(q, params):
    available_params = ["category", "page", "limit", "userID", "fromID",
                        "status", "maxage", "toDate", "fromDate",
                        "dateType", "minSize", "maxSize", "sizeType",
                        "sort", "order", "lang"]
    query = "?q={}".format(q.replace(" ", "+"))

    for param, value in params.items():
        if param in available_params:
            if (param != "category" and param != "status" and
                    param != "lang"):
                query += "&{}={}".format(param, value)
            elif param == "category":
                query += "&c={}_{}".format(value[0], value[1])

            elif param == "status":
                query += "&s={}".format(value)

            elif param == "lang":
                for lang in value:
                    query += "&lang={}".format(lang)

    return query
