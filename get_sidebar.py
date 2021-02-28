import os

TITLE = "* {}"
SUBTITLE = "    * [{}]({})"
IGNORE_DIRS = [
    ".git",
    "static",
    ".github"
]


class GenerateSidebar():
    f = open("_sidebar.md", "w")

    def write(self, content):
        self.f.write(content + "\n")

    def get_sidebar(self):
        tree = os.walk("./", topdown=True)
        self.write("* [Headline](README.md)")
        for root, dirs, files in tree:
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            if root == "./":
                continue
            title = root.split("./")[-1]
            self.write(TITLE.format(title))
            for file in files:
                self.write(SUBTITLE.format(file[:-3], f"{title}/{file}"))
        self.f.close()


if __name__ == '__main__':
    hi = GenerateSidebar()
    hi.get_sidebar()
