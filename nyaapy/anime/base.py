from abc import abstractmethod

from nyaapy.torrent import Torrent

class BaseTorrentSite:

    def _json_to_class(data):
        # We check if the data passed is a list or not
        if isinstance(data, list):
            object_list = []
            for item in data:
                object_list.append(Torrent(item))
                # Return a list of Torrent objects
            return object_list
        else:
            return Torrent(data)
    
    @classmethod
    def _parse_request(cls, base_url: str, keyword: str, kwargs):
        user = kwargs.get("user", None)
        category = kwargs.get("category", 0)
        subcategory = kwargs.get("subcategory", 0)
        filters = kwargs.get("filters", 0)
        page = kwargs.get("page", 0)
        sorting = kwargs.get(
            "sort", "id"
        )  # Sorting by id = sorting by date, this is the default.
        order = kwargs.get("order", "desc")

        user_uri = f"user/{user}" if user else ""

        if page > 0:
            search_uri = f"{base_url}/{user_uri}?f={filters}&c={category}_{subcategory}&q={keyword}&p={page}&s={sorting}&o={order}"
        else:
            search_uri = f"{base_url}/{user_uri}?f={filters}&c={category}_{subcategory}&q={keyword}&s={sorting}&o={order}"

        if not user:
            search_uri += "&page=rss"
            
        return user, search_uri

    @abstractmethod
    def last_uploads(cls, number_of_results: int):
        pass

    @abstractmethod
    def parse_request(cls, keyword, kwargs):
        pass

    @abstractmethod
    def search(cls, keyword: str, **kwargs):
        pass

    @abstractmethod
    def get(cls, view_id: int):
        pass

    @abstractmethod
    def get_from_user(cls, username):
        pass
