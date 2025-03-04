'''def talk(phrase):
    def say(word):
        print(word)
    words =  phrase.split(' ')
    for word in words:
        say(word)

talk ('Oh no our table its broken')'''
def change(value): #nested functonnnnnnnnnnnnn
    def no(val):
        val =  value - 10
        print(val)
    no(value)

change(9)