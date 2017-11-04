![NyaaPy](https://github.com/JuanjoSalvador/NyaaPy/blob/master/nyaapy-logo.png?raw=true)

![](https://img.shields.io/badge/Python-3.5-green.svg)
![](https://img.shields.io/badge/Nyaa.si-supported-green.svg)
![](https://img.shields.io/badge/NyaaPantsu-supported-green.svg)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/JuanjoSalvador/NyaaPy/master/LICENSE.txt)
![](https://img.shields.io/badge/Version-0.5.0-blue.svg)


Unofficial Python module for Nyaa.si (WebScraping) and Nyaa.pantsu.cat (API wrapper)

Supports Python 3+

Full docs available on [repo Wiki](https://github.com/JuanjoSalvador/NyaaPy/wiki)

* [Installation](#installation)
* [Example](#example)
* [License](#license)

## Installation

Install it using pip.

    pip install nyaapy

## Nyaa.si Example

```python
    from NyaaPy import Nyaa

    nyaa_query = Nyaa.search(keyword='koe no katachi 1080', category=1, subcategory=0, filters=0, page=0)

    nyaa_news = Nyaa.news(5)

    if len(nyaa_query) > 0:
        for result in nyaa_query:
            print(result['name'])
    else:
        print('Nothing here!')

    for new in nyaa_news:
        print(new['name'])
```

## Methods

### search()

Returns a list of dicts with the search results.

Parameters:

* **keyword**: String. Keyword for the search query. Mandatory.
* **category**: Integer. Optional.
* **subcategory**: Integer. Optional.
* **filters**: Integer. Optional.
* **page**: Integer. Optional.

`page` must be between 0 and 1000.

#### Dict returned for Nyaa.si

```python
    'category': "Anime - English-translated",
    'url': "https://nyaa.si/view/968600",
    'name': "[HorribleSubs] Shoukoku no Altair - 14 [720p].mkv",
    'download_url': "https://nyaa.si/download/968600.torrent",
    'magnet': <magnet torrent URI>
    'size': "317.2 MiB",
    'date': "2017-10-13 20:16",
    'seeders': "538",
    'leechers': "286",
    'completed_downloads': "852"
```

### news()

Parameters:

* **number_of_results**: Integer

`number_of_results` must be between 1 and 75.


## Categories and subcategories

List of available categories and subcategories:

0. All categories and subcategories

1. Anime.

    1.1 - Anime Music Video

    1.2 - English-translated

    1.3 - Non-English-translated

    1.4 - Raw

2. Audio.

    2.1 - Lossless

    2.2 - Lossy

3. Literature.

    3.1 - English-translated

    3.2 - Non-English-translated

    3.3 - Raw

4. Live Action.

    4.1 - English-translated

    4.2 - Idol/Promotional Video

    4.3 - Non-English-translated

    4.4 - Raw

5. Pictures.

    5.1 - Graphics

    5.2 - Photos

6. Software.

    6.1 - Applications

    6.2 - Games

### Contributions and development

At this moment there isn't an official Nyaa.si API, so we only can make requests using the search URI.

#### Instructions to contribute

1. Clone or fork the repo.

    ```
    $ git clone https://github.com/JuanjoSalvador/nyaapy.git
    ```

2. Set the virtual environment.

    ```
    $ virtualenv nyaa
    $ source nyaa/bin/activate
    ```

3. If you are ussing a clonned repo, please create a new branch named `patch-<username>-<version>`. Example: `patch-juanjosalvador-0.2`

## License

MIT license.
