# multispeaker-glow-tts

Tensorflow Implementation of Glow-TTS, Jaehyeon Kim et al., in NeurIPS 2020. 

- Glow-TTS: A Generative Flow for Text-to-Speech via Monotonic Alignment Search [[arXiv:2005.11129](https://arxiv.org/abs/2005.11129)]
- Full code is based on original github repository [jaywalnut310/glow-tts](https://github.com/jaywalnut310/glow-tts)

## Structure

### Training
<img src='./Figures/Training.svg' width=50% />

### Inference
<img src='./Figures/Inference.svg' width=41.5% />



## Requirements

Tested in python 3.7.11 conda environment, [requirements.txt](./requirements.txt)

## Usage

Put dataset specific symbols list in config file [base_blank.json](./configs/base_blank.json)

train, valid filelists format

> absolute_filepath|numerical_speaker_id|transcript

To start training, run [train_ddi.sh](./train_ddi.sh)

To inference the audio, run [inference.py](./inference.py)
