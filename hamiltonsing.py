import sys
import os
rootdir = os.path.dirname(os.path.abspath(__file__))
sys.path += [rootdir + "/tmnt_wikipedia_bot", rootdir + "/lilysing"]
from lib import words
import lilysing

def generate_wav(input_str: str) -> bytes:
	pass

def main():
	outputwav = generate_wav(sys.argv[1])
	with open(sys.argv[2], "wb") as outfile:
		outfile.write(outputwav)

if __name__ == "__main__":
	main()
