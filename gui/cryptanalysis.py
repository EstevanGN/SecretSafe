from score.ioc import IocScorer
from breaking.vigenere import KeylengthDetector
from score.ngram import NgramScorer
from data.en import load_ngrams
from breaking.vigenere import VigenereBreak

def cryptoanalyze(text):
    s = IocScorer(alphabet_size=26)
    scores = KeylengthDetector(s).detect(text)
    scorer = NgramScorer(load_ngrams(1))
    results = []
    for i in scores:
        breaker = VigenereBreak(i, scorer)
        decryption, score, key = breaker.guess(text)[0]
        results.append("Key : " + str(i) + "\n" + "Vigenere decryption (key={}, score={}):\n---\n{}---\n".format(key, score, decryption))
    return results