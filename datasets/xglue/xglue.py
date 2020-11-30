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
"""The General Language Understanding Evaluation (GLUE) benchmark."""

from __future__ import absolute_import, division, print_function

import os
import textwrap

import datasets


_XGLUE_CITATION = """\
@article{Liang2020XGLUEAN,
  title={XGLUE: A New Benchmark Dataset for Cross-lingual Pre-training, Understanding and Generation},
  author={Yaobo Liang and Nan Duan and Yeyun Gong and Ning Wu and Fenfei Guo and Weizhen Qi
  and Ming Gong and Linjun Shou and Daxin Jiang and Guihong Cao and Xiaodong Fan and Ruofei
  Zhang and Rahul Agrawal and Edward Cui and Sining Wei and Taroon Bharti and Ying Qiao
  and Jiun-Hung Chen and Winnie Wu and Shuguang Liu and Fan Yang and Daniel Campos
  and Rangan Majumder and Ming Zhou},
  journal={arXiv},
  year={2020},
  volume={abs/2004.01401}
}
"""

_XGLUE_DESCRIPTION = """\
XGLUE is a new benchmark dataset to evaluate the performance of cross-lingual pre-trained
models with respect to cross-lingual natural language understanding and generation.
The benchmark is composed of the following 11 tasks:
- NER
- POS Tagging (POS)
- News Classification (NC)
- MLQA
- XNLI
- PAWS-X
- Query-Ad Matching (QADSM)
- Web Page Ranking (WPR)
- QA Matching (QAM)
- Question Generation (QG)
- News Title Generation (NTG)

For more information, please take a look at https://microsoft.github.io/XGLUE/.
"""

_XGLUE_ALL_DATA = "https://msmarco.blob.core.windows.net/xglue/xglue_public.tar.gz"


class XGlueConfig(datasets.BuilderConfig):
    """BuilderConfig for XGLUE."""

    def __init__(
        self,
        text_features,
        data_dir,
        citation,
        url,
        **kwargs,
    ):
        """BuilderConfig for GLUE.

        Args:
          text_features: `dict[string, string]`, map from the name of the feature
            dict for each text field to the name of the column in the tsv file
          label_column: `string`, name of the column in the tsv file corresponding
            to the label
          data_dir: `string`, the path to the folder containing the files in the
            downloaded .tar
          citation: `string`, citation for the data set
          url: `string`, url for information about the data set
          label_classes: `list[string]`, the list of classes if the label is
            categorical. If not provided, then the label will be of type
            `datasets.Value('float32')`.
          process_label: `Function[string, any]`, function  taking in the raw value
            of the label and processing it to the form required by the label feature
          **kwargs: keyword arguments forwarded to super.
        """
        super(XGlueConfig, self).__init__(version=datasets.Version("1.0.0", ""), **kwargs)
        self.text_features = text_features
        self.data_dir = data_dir
        self.citation = citation
        self.url = url


class XGlue(datasets.GeneratorBasedBuilder):
    """The Cross-lingual Pre-training, Understanding and Generation (XGlue) Benchmark."""

    BUILDER_CONFIGS = [
        XGlueConfig(
            name="ner",
            description=textwrap.dedent(
                """\
            The shared task of CoNLL-2003 concerns language-independent named entity recognition.
            We will concentrate on four types of named entities:
            persons, locations, organizations and names of miscellaneous entities
            that do not belong to the previous three groups.
            """
            ),
            text_features=["words", "ner"],
            data_dir="dataset/NER",
            citation=textwrap.dedent(
                """\
            @article{Sang2003IntroductionTT,
              title={Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition},
              author={Erik F. Tjong Kim Sang and Fien De Meulder},
              journal={ArXiv},
              year={2003},
              volume={cs.CL/0306050}
            },
            @article{Sang2002IntroductionTT,
              title={Introduction to the CoNLL-2002 Shared Task: Language-Independent Named Entity Recognition},
              author={Erik F. Tjong Kim Sang},
              journal={ArXiv},
              year={2002},
              volume={cs.CL/0209010}
            }"""
            ),
            url="https://www.clips.uantwerpen.be/conll2003/ner/",
        ),
    ]

    def _info(self):
        features = {
            text_feature: datasets.Sequence(datasets.Value("string")) for text_feature in self.config.text_features
        }
        features["id"] = datasets.Value("int32")
        return datasets.DatasetInfo(
            description=_XGLUE_DESCRIPTION,
            features=datasets.Features(features),
            homepage=self.config.url,
            citation=self.config.citation + "\n" + _XGLUE_CITATION,
        )

    def _split_generators(self, dl_manager):
        all_data_folder = dl_manager.download_and_extract(_XGLUE_ALL_DATA)
        data_folder = os.path.join(all_data_folder, self.config.data_dir)

        if self.config.name == "ner":
            return [
                datasets.SplitGenerator(
                    name=datasets.Split.TRAIN, gen_kwargs={"data_file": os.path.join(data_folder, "en.train")}
                ),
                datasets.SplitGenerator(
                    name=datasets.Split("validation.de"), gen_kwargs={"data_file": os.path.join(data_folder, "de.dev")}
                ),
                datasets.SplitGenerator(
                    name=datasets.Split("test.de"), gen_kwargs={"data_file": os.path.join(data_folder, "de.test")}
                ),
            ]

    def _generate_examples(self, data_file, split=None):
        if self.config.name == "ner":
            words = []
            ner = []
            idx = 0
            with open(data_file, "r") as f:
                for line in f:
                    if line.strip() == "":
                        if len(words) > 0:
                            yield idx, {"words": words, "ner": ner, "id": idx}
                            words = []
                            ner = []
                            idx += 1
                    else:
                        splits = line.strip().split(" ")
                        words.append(splits[0])
                        ner.append(splits[1])
