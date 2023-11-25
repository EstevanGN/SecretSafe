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
        results.append("Key length : " + str(i) + "\n" + "Vigenere Decryption Key={0} \n\n {1}---\n\n".format(key, decryption))
    return results