# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors and the HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Samanantar is the largest publicly available parallel corpora collection for Indic languages"""


import datasets


_DESCRIPTION = """\
Training datasets for machine translation: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu to English.
"""

_CITATION = """\
@misc{ramesh2021samanantar,
      title={Samanantar: The Largest Publicly Available Parallel Corpora Collection for 11 Indic Languages},
      author={Gowtham Ramesh and Sumanth Doddapaneni and Aravinth Bheemaraj and Mayank Jobanputra and Raghavan AK and Ajitesh Sharma and Sujit Sahoo and Harshita Diddee and Mahalakshmi J and Divyanshu Kakwani and Navneet Kumar and Aswin Pradeep and Kumar Deepak and Vivek Raghavan and Anoop Kunchukuttan and Pratyush Kumar and Mitesh Shantadevi Khapra},
      year={2021},
      eprint={2104.05596},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""

_LICENSE = """\
Samanantar is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. This license applies to datasets created as part of the project. For external datasets in the IndicGLUE benchmark, please look at the respective license terms.
"""

_HOMEPAGE = "https://indicnlp.ai4bharat.org/samanantar/"

_LANGUAGES = ["as", "bn", "gu", "hi", "kn", "ml", "mr", "or", "pa", "ta", "te"]
_BASE_DATA_URL = "https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-{}.zip"

ALL_PAIRS = []
for i in range(len(_LANGUAGES)):
    ALL_PAIRS.append(("en", _LANGUAGES[i]))

_VERSION = "1.0.0"


class SamanantarConfig(datasets.BuilderConfig):
    """Custom config to take both source and target languages"""

    def __init__(self, *args, lang1=None, lang2=None, **kwargs):
        super().__init__(
            *args,
            name=f"{lang1}-{lang2}",
            **kwargs,
        )
        self.lang1 = lang1
        self.lang2 = lang2

    def _lang_pair(self):
        return (self.lang1, self.lang2)

    def _is_valid(self):
        return self._lang_pair() in ALL_PAIRS


class Samanantar(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version(_VERSION)

    BUILDER_CONFIG_CLASS = SamanantarConfig
    BUILDER_CONFIGS = [
        SamanantarConfig(lang1=lang1, lang2=lang2, version=datasets.Version(_VERSION)) for lang1, lang2 in ALL_PAIRS
    ]

    def _info(self):
        """This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset."""
        features = datasets.Features(
            {
                "translation": datasets.Translation(languages=(self.config.lang1, self.config.lang2)),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""

        if not self.config._is_valid():
            raise ValueError(f"{self.config._lang_pair()} is not a supported language pair. Choose among: {ALL_PAIRS}")

        # download data files
        datafiles = dl_manager.download_and_extract(_BASE_DATA_URL.format(self.config.lang2))

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={"datafiles": (datafiles), "lang": self.config.lang2},
            )
        ]

    def _generate_examples(self, datafiles, lang):
        with open(f"{datafiles}/en-{lang}/train.en", "r") as f:
            en = f.readlines()
        with open(f"{datafiles}/en-{lang}/train.{lang}", "r") as f:
            lang = f.readlines()

        for _id, (s, t) in enumerate(zip(en, lang)):
            yield _id, {"translation": {self.config.lang1: s, self.config.lang2: t}}
