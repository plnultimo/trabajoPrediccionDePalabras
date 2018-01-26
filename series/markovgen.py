# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:51:20 2017
@author: Cesia
"""
import random
class Markov(object):

    def __init__(self):
        self.cache = {}
        self.texto ="";
        self.cachee={}

    #convierte el arhivo en palabras
    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words

    def texto_to_words(self):
        words = self.texto.split()
        return words

    def addText(self,text):
        self.texto=self.texto+" "+text
        self.cache = {}
        self.words = self.texto_to_words()
        self.word_size = len(self.words)
        self.database()
        self.generate()

    def generate(self):
        self.cachee={}
        for i in range(0,self.word_size-1):
            if self.words[i] in self.cachee:
                if self.words[i+1] in self.cachee[self.words[i]]:
                    self.cachee[self.words[i]][self.words[i+1]]=self.cachee[self.words[i]][self.words[i+1]]+1
                else:
                    self.cachee[self.words[i]][self.words[i+1]]=1

#                self.cachee[self.words[i]].append(self.words[i+1])
#                self.cachee[self.words[i]]=list(set(self.cachee[self.words[i]]))
            else:
                self.cachee[self.words[i]]={self.words[i+1]:1}


    #genera triples
    def triples(self):
        """ Genera triples a partir de la cadena de datos dada. Si nuestra cadena fuera
                "What a lovely day", generariamos (What, a, lovely) y luego
                (a, lovely, day).
        """
        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    
    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    #genera texto de markov tomando solo un fragmento de 50 palabras
    def generate_markov_text(self, size=3):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return gen_words


