import os
import time
import re

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

class TextGenerator:
    """A class for selecting sentences of length in a certain range from a given file."""
    def __init__(self, file_name):
        self.file_name = file_name
        self.location = 0
        self.contents = []
        self.read_contents()


    def split_into_sentences(self, text):
        text = " " + text + "  "
        text = text.replace("\n"," ")
        text = re.sub(prefixes,"\\1<prd>",text)
        text = re.sub(websites,"<prd>\\1",text)
        if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
        text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
        text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
        text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
        text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
        text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
        if "”" in text: text = text.replace(".”","”.")
        if "\"" in text: text = text.replace(".\"","\".")
        if "!" in text: text = text.replace("!\"","\"!")
        if "?" in text: text = text.replace("?\"","\"?")
        text = text.replace(".",".<stop>")
        text = text.replace("?","?<stop>")
        text = text.replace("!","!<stop>")
        text = text.replace("<prd>",".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]
        return sentences


    def read_contents(self):
        """Store certain length sentences into the contents variable."""
        with open(self.file_name, "r") as fp:
            whole_file = fp.read()
            sentences = self.split_into_sentences(whole_file)
            for sentence in sentences: 
                sentence = sentence.strip()
                sentence_split = sentence.split()
                if 10 < len(sentence_split) < 20:
                    for word in sentence_split:
                        if len(word) == 1 and word not in alphabets:
                            sentence_split.remove(word)
                    for i, word in enumerate(sentence_split):
                        if i % 3 == 0 and i > 1:
                            sentence_split[i] = word + "\n"
                    sentence = " ".join(sentence_split)
                    self.contents.append(sentence)


    def get_next_sentence(self):
        """Return the next sentence from the file."""
        if not self.contents or self.location > len(self.contents) - 1:
            raise IndexError(f"No more sentences available from {self.file_name}.")
        self.location += 1
        return self.contents[self.location]

if __name__=="__main__":
    test = TextGenerator(os.path.join("resources", "text", "africa.txt"))
    print(test.get_next_sentence())
    print(test.get_next_sentence())
    print(test.get_next_sentence())