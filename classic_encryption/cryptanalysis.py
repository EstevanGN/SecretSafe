from score.ioc import IocScorer
from breaking.vigenere import KeylengthDetector
from score.ngram import NgramScorer
from data.en import load_ngrams
from breaking.vigenere import VigenereBreak

text = input("De el texto cifrado en mayusculas y sin espacios: ")

print("\nCracking...\n")

print("Inferring key length...")
s = IocScorer(alphabet_size=26)
scores = KeylengthDetector(s).detect(text)
scorer = NgramScorer(load_ngrams(1))

print("Los posibles textos son: ")
for i in scores:
    breaker = VigenereBreak(i, scorer)
    decryption, score, key = breaker.guess(text)[0]
    print("Vigenere decryption (key={}, score={}):\n---\n{}---\n"
          .format(key, score, decryption))