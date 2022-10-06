import ast
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Set

__author__ = "Anonymous"
__license__ = "MIT License"
__version__ = "1.0."
__email__ = "Anonymous"
antonym_dict = {}

"""
Extract antonyms from the German Wiktionary dumpfiles, available here: https://dumps.wikimedia.org/
Applied to the unzipped dumpfile.
Select only antonyms ("Gegenwörter") in the German language ("Sprache Deutsch").
Plural words are added in their singular and plural form.
Every word is set to lowercase and stored in a Python dictionary with key: word, value: its antonyms.
Also, every antonym relation is made bidirectional.
"""


def wiktionary_parser():
    link_to_wiktionary_dump = "./dewiktionary-20211120-pages-articles-multistream.xml"
    tree = ET.parse(link_to_wiktionary_dump)
    root = tree.getroot()
    page_list = []

    for child in root:
        if child.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":
            page_list.append(child)
    for page in page_list:
        title = page[0].text
        revision = page[3]
        wikitext = ""
        for child in revision:
            if child.tag == "{http://www.mediawiki.org/xml/export-0.10/}text":
                wikitext = child.text

            # check if there are multiple languages, not only German("Deutsch")
            if wikitext and "{{Sprache|Deutsch}}" in wikitext:
                wikitext = re.sub("\n", " ", wikitext)
                if wikitext.count("{{Sprache|") > 1:  # multiple languages
                    try:
                        wikitext = re.search("{{Sprache\|Deutsch}}\) ==(.*?){{Sprache\|", wikitext).group(1)
                    except AttributeError:
                        continue

                # check if the page contains antonyms, get only content until next heading starting with {{
                if "{{Gegenwörter}}" in wikitext:
                    wikitext = re.search("{{Gegenwörter}}(.*?){{", wikitext).group(1)

                    # split string at punctuation mark: ,;:./ to later retrieve content between [[antonym]]
                    wordlist = re.split(r"\,|\;|:|\.|/", wikitext)
                    resultset = set()

                    for word in wordlist:
                        try:
                            # antonyms can be multiwords [[herab]] [[schauen]] that are joined "herab schauen"
                            matches = re.findall(r"\[\[(.*?)\]\]", word)
                            word = " ".join(matches)
                            word = word.strip().lower()
                        except AttributeError:  # Problems with entries: [[#Substantiv, m|See]] because of the comma
                            continue
                        if word == "":
                            continue

                        # try to find singular/plural words: [[Wolke(n)]]
                        match = re.match(r"^(.*?)(\((\S+)\))?$", word)
                        # the first group always exists
                        resultset.add(match.group(1))
                        # the second group only exists if there is combined singular/plural in the word
                        if match.group(2) is not None:
                            resultset.add(f"{match.group(1)}{match.group(3)}")

                    if resultset:
                        if title.lower() in antonym_dict:
                            antonym_dict[title.lower()].update(resultset)
                        else:
                            antonym_dict[title.lower()] = resultset

    with open("./AntonymDictOneDirection.txt", mode="w",
              encoding="utf-8") as f:
        print(antonym_dict, file=f)


"""
Extend the antonym dictionary and create a bidirectional relation between antonyms:
E.g., if father is an antonym of mother, mother is set as an antonym of father, too.
"""
def antonym_dict_extender():
    with open("./AntonymDictOneDirection.txt", mode="r", encoding="utf-8") as f:
        antonym_file = f.read()
    antonym_dict_single = ast.literal_eval(antonym_file)

    antonym_data: Dict[str, List[str]] = antonym_dict_single
    output: Dict[str, Set[str]] = dict()

    for k, vs in antonym_data.items():
        # add the existing links to output
        current_output_values = output.setdefault(k, set())
        current_output_values.update(vs)
        # create new keys
        for v in vs:
            current_output_values = output.setdefault(v, set())
            current_output_values.add(k)

    with open("./AntonymDict.txt", mode="w",
              encoding="utf-8") as f:
        print(output, file=f)


def main():
    wiktionary_parser()
    antonym_dict_extender()


if __name__ == '__main__':
    main()
