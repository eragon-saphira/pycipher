'''
base cipher object that other ciphers extend
really only provides mappings a2i and i2a for letter->int->letter conversions
Author: James Lyons
Created: 2012-04-28
'''
import string
import warnings

class Cipher(object):
    def encipher(self,string):
        return string
        
    def decipher(self,string):
        return string
        
    def a2i(self,ch):
        return ord(ch)-65 if ch.isupper() else ord(ch)-97

    def i2a(self,i,lower=False):
        i=i%26
        return chr(i+97) if lower else chr(i+65)
        
    def remove_punctuation(self,text,characters=None):
        no_punctuation = text.translate(str.maketrans("","",string.punctuation))
        if characters:
            filtered_chars = ''.join(ch for ch in no_punctuation if ch in characters)
            if len(filtered_chars) != no_punctuation:
                warnings.warn(message="The data contains characters missing in key which will be removed",category=ResourceWarning)
        return no_punctuation
