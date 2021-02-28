import sys
from get_sidebar import GenerateSidebar

CONTENT = """
<div class="video-container">
    <iframe 
        src="https://www.youtube.com/embed/{}?fs=0"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>

---

```
```
"""

class Generate(GenerateSidebar):
    def __init__(self, filename, video_id):
        self.filename = filename.capitalize()
        self.video_id = video_id
        self.f = open(self.filename + ".md", "w")

    def write(self, content):
        self.f.write(content + "\n")

    def main(self):
        self.write(f"# {self.filename}")
        self.write(CONTENT.format(self.video_id))
        self.f.close()
        self.get_sidebar()

if __name__ == "__main__":
    try:
        post = Generate(sys.argv[1], sys.argv[2])
        post.main()
    except:
        print("Please input corret format.\nExample: python3 post.py <fileName> <videoId>")
        sys.exit()
