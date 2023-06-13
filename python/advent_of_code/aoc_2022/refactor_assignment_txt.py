import collections

class RefactorTextDocument:
    Text = ""

    def __init__(self, path):
        self.path = path
        self.text = ""

    def resize_document(self):
        f = open(self.path, "r")
        text = f.read()
        f.close()

        paragraphs = text.split("\n\n")
        new_paragraphs = collections.deque()

        for p in paragraphs:
            lines = p.split("\n")
            new_lines = collections.deque()
            for l in lines:
                words = l.split(" ")
                new_line = ""
                while words:
                    if len(new_line) > 0:
                        if len(new_line + " " + words[0]) < 55:
                            new_line += " "
                        else:
                            new_lines.append(new_line)
                            new_line = ""
                    new_line += words.pop(0)
                if len(new_line) > 0:
                    new_lines.append(new_line)
            new_paragraphs.append("\n".join(new_lines))


        self.text = "\n\n".join(new_paragraphs)
        return self

    def write(self):
        f = open(path, "w")
        f.write(self.text)
        f.close()
        return self

path = "04_camp_cleanup/p1/assignment.txt"
r = RefactorTextDocument(path)
# print(r.resize_document().text)
r.resize_document().write()
