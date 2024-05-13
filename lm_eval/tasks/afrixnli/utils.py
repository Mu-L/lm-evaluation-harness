import yaml
import argparse


class FunctionTag:
    def __init__(self, value):
        self.value = value


LANGUAGES = {
    "amh": {
        "QUESTION_WORD": "ትክክል",
        "ENTAILMENT_LABEL": "አዎ",
        "NEUTRAL_LABEL": "እንዲሁም",
        "CONTRADICTION_LABEL": "አይ"
    },
    "eng": {
        "QUESTION_WORD": "Right",
        "ENTAILMENT_LABEL": "Yes",
        "NEUTRAL_LABEL": "Also",
        "CONTRADICTION_LABEL": "No"
    },
    "ewe": {
        "QUESTION_WORD": "Esɔ gbe",
        "ENTAILMENT_LABEL": "Ɛ̃",
        "NEUTRAL_LABEL": "Hã",
        "CONTRADICTION_LABEL": "Ao"
    },
    "fra": {
        "QUESTION_WORD": "correct",
        "ENTAILMENT_LABEL": "Oui",
        "NEUTRAL_LABEL": "Aussi",
        "CONTRADICTION_LABEL": "Non"
    },
    "hau": {
        "QUESTION_WORD": "Daidai",
        "ENTAILMENT_LABEL": "Ee",
        "NEUTRAL_LABEL": "Haka kuma",
        "CONTRADICTION_LABEL": "A'a"
    },
    "ibo": {
        "QUESTION_WORD": "Ziri ezi",
        "ENTAILMENT_LABEL": "Éè",
        "NEUTRAL_LABEL": "Ọzọkwa",
        "CONTRADICTION_LABEL": "Mba"
    },
    "kin": {
        "QUESTION_WORD": "Nibyo",
        "ENTAILMENT_LABEL": "Yego",
        "NEUTRAL_LABEL": "Na none",
        "CONTRADICTION_LABEL": "Oya"
    },
    "lin": {
        "QUESTION_WORD": "Malamu",
        "ENTAILMENT_LABEL": "Iyo",
        "NEUTRAL_LABEL": "Lisusu",
        "CONTRADICTION_LABEL": "Te"
    },
    "lug": {
        "QUESTION_WORD": "Kituufu",
        "ENTAILMENT_LABEL": "Yee",
        "NEUTRAL_LABEL": "N’ekirala",
        "CONTRADICTION_LABEL": "Nedda"
    },
    "orm": {
        "QUESTION_WORD": "Sirrii",
        "ENTAILMENT_LABEL": "Eeyyee",
        "NEUTRAL_LABEL": "Akkasumas",
        "CONTRADICTION_LABEL": "Lakki"
    },
    "sna": {
        "QUESTION_WORD": "Chokwadi",
        "ENTAILMENT_LABEL": "Hongu",
        "NEUTRAL_LABEL": "Uye",
        "CONTRADICTION_LABEL": "Kwete"
    },
    "sot": {
        "QUESTION_WORD": "Nepile",
        "ENTAILMENT_LABEL": "E",
        "NEUTRAL_LABEL": "Hape",
        "CONTRADICTION_LABEL": "Tjhe"
    },
    "swa": {
        "QUESTION_WORD": "Sahihi",
        "ENTAILMENT_LABEL": "Ndiyo",
        "NEUTRAL_LABEL": "Pia",
        "CONTRADICTION_LABEL": "Hapana"
    },
    "twi": {
        "QUESTION_WORD": "Nifa",
        "ENTAILMENT_LABEL": "Aane",
        "NEUTRAL_LABEL": "Anaasɛ",
        "CONTRADICTION_LABEL": "Daabi"
    },
    "wol": {
        "QUESTION_WORD": "Dëgg",
        "ENTAILMENT_LABEL": "Waaw",
        "NEUTRAL_LABEL": "Itam",
        "CONTRADICTION_LABEL": "Déet"
    },
    "xho": {
        "QUESTION_WORD": "Ichanekile",
        "ENTAILMENT_LABEL": "Ewe",
        "NEUTRAL_LABEL": "Kananjalo",
        "CONTRADICTION_LABEL": "Hayi"
    },
    "yor": {
        "QUESTION_WORD": "Òótọ́",
        "ENTAILMENT_LABEL": "Bẹ́ẹ̀ni",
        "NEUTRAL_LABEL": "Àti pé",
        "CONTRADICTION_LABEL": "Rárá"
    },
    "zul": {
        "QUESTION_WORD": "Kulungile",
        "ENTAILMENT_LABEL": "Yebo",
        "NEUTRAL_LABEL": "Futhi",
        "CONTRADICTION_LABEL": "Cha"
    }
}


def gen_lang_yamls(output_dir: str, overwrite: bool, mode: str) -> None:
    """
    Generate a yaml file for each language.

    :param output_dir: The directory to output the files to.
    :param overwrite: Whether to overwrite files if they already exist.
    """
    err = []
    languages = ['eng', 'amh', 'ibo', 'fra', 'sna', 'wol', 'ewe', 'lin', 'lug', 'xho', 'kin', 'twi', 'zul', 'orm',
                 'yor', 'hau', 'sot', 'swa']
    for lang in languages:
        try:
            if mode == "en_direct":
                file_name = f"afrixnli_en_direct_{lang}.yaml"
                task_name = f"afrixnli_en_direct_{lang}"
                yaml_template = "afrixnli_en_direct_yaml"
                with open(
                        f"{output_dir}/{file_name}", "w" if overwrite else "x", encoding="utf8"
                ) as f:
                    f.write("# Generated by utils.py\n")
                    yaml.dump(
                        {
                            "include": yaml_template,
                            "task": task_name,
                            "dataset_name": lang
                        },
                        f,
                        allow_unicode=True,
                    )
            elif mode == "native-direct":
                QUESTION_WORD = LANGUAGES[lang]["QUESTION_WORD"]
                ENTAILMENT_LABEL = LANGUAGES[lang]["ENTAILMENT_LABEL"]
                NEUTRAL_LABEL = LANGUAGES[lang]["NEUTRAL_LABEL"]
                CONTRADICTION_LABEL = LANGUAGES[lang]["CONTRADICTION_LABEL"]

                file_name = f"afrixnli_native_direct_{lang}.yaml"
                task_name = f"afrixnli_native_direct_{lang}"
                yaml_template = "afrixnli_native_direct_yaml"
                with open(
                        f"{output_dir}/{file_name}", "w" if overwrite else "x", encoding="utf8"
                ) as f:
                    f.write("# Generated by utils.py\n")
                    yaml.dump(
                        {
                            "include": yaml_template,
                            "task": task_name,
                            "dataset_name": lang,
                            "doc_to_choice": f"{{{{["
                                           f"""premise+\", {QUESTION_WORD}? {ENTAILMENT_LABEL}, \"+hypothesis,"""
                                           f"""premise+\", {QUESTION_WORD}? {NEUTRAL_LABEL}, \"+hypothesis,"""
                                           f"""premise+\", {QUESTION_WORD}? {CONTRADICTION_LABEL}, \"+hypothesis"""
                                           f"]}}}}",
                        },
                        f,
                        allow_unicode=True,
                    )
        except FileExistsError:
            err.append(file_name)

    if len(err) > 0:
        raise FileExistsError(
            "Files were not created because they already exist (use --overwrite flag):"
            f" {', '.join(err)}"
        )


def main() -> None:
    """Parse CLI args and generate language-specific yaml files."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--overwrite",
        default=True,
        action="store_true",
        help="Overwrite files if they already exist",
    )
    parser.add_argument(
        "--output-dir", default="./native-direct", help="Directory to write yaml files to"
    )
    parser.add_argument(
        "--mode",
        default="native-direct",
        choices=["en_direct", "native-direct"],
        help="Mode of chain-of-thought",
    )
    args = parser.parse_args()

    gen_lang_yamls(output_dir=args.output_dir, overwrite=args.overwrite, mode=args.mode)


if __name__ == "__main__":
    main()
