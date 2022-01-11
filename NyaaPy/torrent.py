def json_to_class(data):
    # We check if the data passed is a list or not
    if isinstance(data, list):
        object_list = []
        for item in data:
            object_list.append(Torrent(item))
            # Return a list of Torrent objects
        return object_list
    else:
        return Torrent(data)


# This deals with converting the dict to an object
class Torrent(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
