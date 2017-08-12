# NyaaPy

Unofficial Python module to search into Nyaa.si and nyaa.pantsu.cat.

Based on [Kylart's Nyaapi](https://github.com/Kylart/Nyaapi).


### Installation and ussage

Install it using pip.

    pip install nyaapy


### Contributions and development

At this moment there isn't an official Nyaa.si API, so we only can make requests using the search URI.

#### Instructions to contribute

1. Clone or fork the repo.

    ```
    $ git clone https://github.com/JuanjoSalvador/nyaapy.github
    ```

2. Set the virtual environment.

    ```
    $ virtualenv nyaa
    $ source nyaa/bin/activate
    ```

3. If you are ussing a clonned repo, please create a new branch named `patch-<username>-<version>`. Example: `patch-juanjosalvador-0.2`

4. Always use the code into `src` folder, never the package.

### Example code

    from NyaaPy.nyaa import Nyaa
    from NyaaPy.nyaa import NyaaPantsu

    # Nyaa.si results
    nyaa_query = Nyaa.search('new game')
    for result in nyaa_query:
        print(result['title'])

    # Nyaa.pantsu.cat results
    pantsu_query = NyaaPantsu.search('new game')

    for result in pantsu_query:
        print(result['title'])

### License

MIT license.
