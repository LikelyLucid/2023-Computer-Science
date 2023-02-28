class Toes:
    def __init__(self, sexyness, aroma, flavor, texture):
        self.sexyness = sexyness
        self.aroma = aroma
        self.flavor = flavor
        self.texture = texture
    def __str__(self):
        return f"{self.sexyness} {self.aroma} {self.flavor} {self.texture}"
    def __repr__(self):
        return f"{self.sexyness} {self.aroma} {self.flavor} {self.texture}"