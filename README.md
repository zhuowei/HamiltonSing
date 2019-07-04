Program to sing words to the tune of "Alexander Hamilton".

Inspired by [UINT\_MIN's @whatyournamebot](https://twitter.com/whatyournamebot).

Uses:
- [MBROLA](https://github.com/numediart/MBROLA) to synthesize
- [snappizz's LilySing](https://github.com/snappizz/lilysing) to generate MBROLA
- [catleeball's tmnt\_wikipedia\_bot](https://github.com/catleeball/tmnt_wikipedia_bot) to fix up input
- [aparrish's pronouncingpy](https://github.com/aparrish/pronouncingpy) to get syllables for each word

Running:

```
sudo apt install python3-venv mbrola mbrola-us2
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 hamiltonsing.txt "Alexander Hamilton" output.wav
```
