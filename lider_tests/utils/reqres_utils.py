def get_all_names(json):
    data = json["data"]
    names = [item["name"] for item in data]
    return names
