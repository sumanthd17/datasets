annotations_creators:
- no-annotation
language_creators:
- machine-generated
languages:
- '''en-US'''
- '''hi-IN'''
licenses:
- cc-by-4.0
multilinguality:
- translation
- multilingual
pretty_name: samanantar
size_categories:
- unknown
source_datasets:
- original
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
paperswithcode_id: samanantar

# Dataset Card for samanantar

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** Samanantar Homepage (https://indicnlp.ai4bharat.org/samanantar/)
- **Repository:** [Needs More Information]
- **Paper:** [Samanantar: The Largest Publicly Available Parallel Corpora Collection for 11 Indic Languages](https://arxiv.org/abs/2104.05596)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

Samanantar is the largest publicly available parallel corpora collection for Indic languages: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. The corpus has 49.6M sentence pairs between English to Indian Languages.

### Supported Tasks and Leaderboards

- `machine-translation`: The dataset can be used to train translation models. The dataset currently supports translation from 11 Indian languages to English and vice-verse. The model performance is measured by how high its BLEU score is

### Languages

Dataset supports 11 Indian languages and English. The associated BCP-47 codes are `as`, `bn`, `en`, `gu`, `hi`, `kn`, `ml`, `mr`, `or`, `pa`, `ta`, `te`

## Dataset Structure

### Data Instances

{'translation': {'as': '������� ���𾯼ǲ� �Ǩ� ��� ��ͯ������ͣ ���ͯͯ� ���ͤ ����?\n', 'en': 'When it comes to speaking Gods word, we will not disobey our God, even in lands where modern - day Amaziahs are fomenting cruel persecution.\n'}}

### Data Fields

[Needs More Information]

### Data Splits

The dataset only provides the training data

## Dataset Creation

### Curation Rationale

[Needs More Information]

### Source Data

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

- Gowtham Ramesh, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [IITM](https://www.iitm.ac.in))</sub>
- Sumanth Doddapaneni, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [IITM](https://www.iitm.ac.in))</sub>
- Aravinth Bheemaraj, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Mayank Jobanputra, <sub>([IITM](https://www.iitm.ac.in))</sub>
- Raghavan AK, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Ajitesh Sharma, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Sujit Sahoo, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Harshita Diddee, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Mahalakshmi J, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Divyanshu Kakwani, <sub>([IITM](https://www.iitm.ac.in), [AI4Bharat](https://ai4bharat.org))</sub>
- Navneet Kumar, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Aswin Pradeep, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Kumar Deepak, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Vivek Raghavan, <sub>([EkStep](https://ekstep.in))</sub>
- Anoop Kunchukuttan, <sub>([Microsoft](https://www.microsoft.com/en-in/), [AI4Bharat](https://ai4bharat.org))</sub>
- Pratyush Kumar, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>
- Mitesh Shantadevi Khapra, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>

### Licensing Information

Samanantar is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/). This license applies to datasets created as part of the project. For external datasets in the IndicGLUE benchmark, please look at the respective license terms.

### Citation Information

@misc{ramesh2021samanantar,
      title={Samanantar: The Largest Publicly Available Parallel Corpora Collection for 11 Indic Languages}, 
      author={Gowtham Ramesh and Sumanth Doddapaneni and Aravinth Bheemaraj and Mayank Jobanputra and Raghavan AK and Ajitesh Sharma and Sujit Sahoo and Harshita Diddee and Mahalakshmi J and Divyanshu Kakwani and Navneet Kumar and Aswin Pradeep and Kumar Deepak and Vivek Raghavan and Anoop Kunchukuttan and Pratyush Kumar and Mitesh Shantadevi Khapra},
      year={2021},
      eprint={2104.05596},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}