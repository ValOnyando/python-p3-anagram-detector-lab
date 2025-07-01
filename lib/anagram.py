class Anagram:
    def __init__(self, ina):
        self.ina = ina

    @property
    def ina(self):
        return self._ina
    
    @ina.setter
    def ina(self, ina):
        if isinstance(ina, str):
            self._ina = ina
    
    def match(self, word_list):
        result = []
        sorted_ina = sorted(self.ina.lower())
        for word in word_list:
            if word.lower() != self.ina.lower() and sorted(word.lower()) == sorted_ina:
                result.append(word)
        return result