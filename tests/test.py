from NyaaPy import Pantsu

print(Pantsu.search('koe no katachi', lang=["es", "ja"], category=[1, 3]))

print(Pantsu.upload('<API_TOKEN>',
                    # '<ABS PATH TO .TORRENTFILE>',
                    # or
                    '<MAGNET_LINK>',
                    category=[2, 3], username='<ACCOUNT_USERNAME>', name='Mariya Takeuchi (竹内まりや) - VIVA MARIYA!!',
                    remake=False, description='Cool music', status=1,
                    hidden=True, website_link='https://github.com/JuanjoSalvador/NyaaPy',
                    languages=["es", "en", "jp"]))
