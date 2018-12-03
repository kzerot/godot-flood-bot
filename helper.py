import urllib.request, json 


    
class Helper():
    def __init__(self):
        self.class_list = []
        self.url = 'https://api.github.com/repos/godotengine/godot/contents/doc/classes'
        with urllib.request.urlopen(self.url) as url:
            result = json.loads(url.read().decode())
            for row in result:
                self.class_list.append({
                        "name": row["name"].replace(".xml", ""),
                        "url": row["download_url"]
                    })
            print(self.class_list)
