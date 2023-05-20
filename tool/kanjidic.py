import os
import string
import json
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET

jplt_4_kanjidic2 = {}
jplt_3_kanjidic2 = {}
jplt_2_kanjidic2 = {}
jplt_1_kanjidic2 = {}
kanjidic2_json = {}

def get_kanjidic2_data():
    # Load the XML file
    tree = ET.parse('tool/kanjidic2.xml')

    # Iterate over all the characters in the XML file
    katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
    hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
    kat2hir = str.maketrans(katakana_chart, hiragana_chart)

    for character in tree.iter("character"):
        entry = {
            "kanji": None,
            "jlpt": None,
            "meanings": [],
            "onyomi": [],
            "kunyomi": []
        }

        literal = character.find("literal").text
        kanjidic2_json[literal] = entry

        misc = character.find("misc")
        entry["kanji"] = literal
        if misc is not None:
            jlpt = misc.find("jlpt")
            if jlpt is not None:
                entry["jlpt"] = int(jlpt.text)

        reading_meaning = character.find("reading_meaning")
        if reading_meaning is not None:
            rmgroups = reading_meaning.findall("rmgroup")
            for rmgroup in rmgroups:

                meanings = rmgroup.findall("meaning")
                for meaning in meanings:
                    m_lang = meaning.get("m_lang")
                    if m_lang == "fr":
                        entry["meanings"].append(string.capwords(meaning.text))

                readings = rmgroup.findall("reading")
                for reading in readings:
                    r_type = reading.get("r_type")
                    if r_type == "ja_on":
                        entry["onyomi"].append(reading.text.translate(kat2hir))
                    elif r_type == "ja_kun":
                        entry["kunyomi"].append(reading.text)

    return kanjidic2_json


def save_json_files():
    json_kanji = get_kanjidic2_data()

    # Create a new dictionary with only the kanji for each JLPT level
    for key, entry in json_kanji.items():

        if entry.get("jlpt") == 1:
            jplt_1_kanjidic2[key] = entry

        elif entry.get("jlpt") == 2:
            jplt_2_kanjidic2[key] = entry

        elif entry.get("jlpt") == 3:
            jplt_3_kanjidic2[key] = entry

        elif entry.get("jlpt") == 4:
            jplt_4_kanjidic2[key] = entry

        # Save the kanjidic2_json object as a new JSON file
    with open("json/kanjidic.json", "wt", encoding="utf-8") as fp:
        json.dump(json_kanji, fp, ensure_ascii=False, indent=4)

        # Save the jlpt_1_characters object as a new JSON file
    with open("json/jplt_1.json", "wt", encoding="utf-8") as file:
        json.dump(jplt_1_kanjidic2, file, ensure_ascii=False, indent=4)

        # Save the jlpt_2_characters object as a new JSON file
    with open("json/jplt_2.json", "wt", encoding="utf-8") as file:
        json.dump(jplt_2_kanjidic2, file, ensure_ascii=False, indent=4)

        # Save the jlpt_3_characters object as a new JSON file
    with open("json/jplt_3.json", "wt", encoding="utf-8") as file:
        json.dump(jplt_3_kanjidic2, file, ensure_ascii=False, indent=4)

        # Save the jlpt_4_characters object as a new JSON file
    with open("json/jplt_4.json", "wt", encoding="utf-8") as file:
        json.dump(jplt_4_kanjidic2, file, ensure_ascii=False, indent=4)
