'''
    Module utils
'''

class Utils():

    def nyaa_categories(b):
        c = b.replace('/?c=', '')
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
            category_name = "{} - {}".format(categories[cat]['name'], categories[cat]['subcats'][subcat])
        except:
            pass

        return category_name

    def parse_nyaa(table_rows, limit):

        torrents = []

        for row in table_rows[:limit]:
                block = []

                for td in row.find_all('td'):
                    if td.find_all('a'):
                        for link in td.find_all('a'):
                            if link.get('href')[-9:] != '#comments':
                                block.append(link.get('href'))
                                if link.text.rstrip():
                                    block.append(link.text)

                    if td.text.rstrip():
                        block.append(td.text.rstrip())

                try:
                    torrent = {
                        'category': Utils.nyaa_categories(block[0]),
                        'url': "http://nyaa.si{}".format(block[1]),
                        'name': block[2],
                        'download_url': "http://nyaa.si{}".format(block[4]),
                        'magnet': block[5],
                        'size': block[6],
                        'date': block[7],
                        'seeders': block[8],
                        'leechers': block[9],
                        'completed_downloads': block[10],
                    }
                
                    torrents.append(torrent)
                except IndexError as ie:
                    pass
        
        return torrents

    def query_builder(q, params):
        available_params = ["category", "page", "limit", "userID", "fromID", "status", "maxage", "toDate", "fromDate",\
                            "dateType", "minSize", "maxSize", "sizeType", "sort", "order", "lang"]
        query = "?q={}".format(q.replace(" ", "+"))

        for param, value in params.items():
            if param in available_params:
                if param != "category" and param != "status" and param != "lang":
                    query += "&{}={}".format(param, value)
                else:
                    if param == "category":
                        query += "&c={}_{}".format(value[0], value[1])
                    
                    if param == "status":
                        query += "&s={}".format(value)
        
                    if param == "lang":
                        for lang in value:
                            query += "&lang={}".format(lang)
        
        return query