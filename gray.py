
class Library:
    
    def __init__(self):
        self._symbols = [',','/','\\','\n','\t','.','{','}','(',')','[',']',
                         '|','!','@','#','$','%','^','&','*','-','_','+','=',
                         '`','~',':',';','\'','"','?','\0','\xa0', '¼', '’','–',
                         'ー','´',"¨",'©','°','﹠','¸','º','³','�','¥','«',
                         '“','£','ˆ','‹','·','‘','•','，','・','®','™','—']
        self._umlautList = {
            'ğ' : 'g',
            'č' : 'c',
            'ţ' : 't',
            'ł' : 'l',
            'ž' : 'z',
            'Œ' : 'oe',
            'š' : 's',
            'ř' : 'r',
            '¡' : 'i',
            'ō' : 'o',
            'ś' : 's',
            'ń' : 'n',
            'Ł' : 't',
            'г' : 'r',
            'ę' : 'e',
            'ş' : 's',
            'ů' : 'u',
            'ď' : 'd',
            'ī' : 'i',
            'ē' : 'e',
            'ı' : 'l',
            'Ÿ' : 'Y',
            'в' : 'B',
            'н' : 'H',
            'У' : 'y',
            'χ' : 'X',
            'Ţ' : 'T'
        }
    
    def isValidEnglish(self,character):
        val = ord(character[0])
        if val>=ord('a') and val<=ord('z'):
            return True
        elif val>=ord('A') and val<=ord('Z'):
            return True
        elif val>=ord('0') and val<=ord('9'):
            return True
        elif character[0]==' ':
            return True
        return False
    
    def isUmlaut(self,character):
        val = ord(character[0])
        if val>=192 and val<=246:
            return True
        elif val==138:
            return True
        elif val==159:
            return True
        elif val>=248 and val<=255:
            return True
        elif val==154:
            return True
        if character[0] in self._umlautList.keys():
            return True
        return False
    
    def umlautToEnglish(self,character):
        if self.isUmlaut(character)==False:
            raise ('Invalid Umlaut Error')
        val = ord(character[0])
        if character[0] in self._umlautList.keys():
            return self._umlautList.get(character[0])
        if val>=192 and val<=198:
            return 'A'
        elif val==199:
            return 'C'
        elif val>=200 and val<=203:
            return 'E'
        elif val>=204 and val<=207:
            return 'I'
        elif val==208:
            return 'D'
        elif val == 209:
            return 'N'
        elif val>=210 and val <= 216:
            return 'O'
        elif val==138:
            return 'S'
        elif val>=217 and val<=220:
            return 'U'
        elif val==221 or val==159:
            return 'Y'
        elif val==222:
            return 'th'
        elif val==223:
            return 'B'
        elif val>=224 and val<=230:
            return 'a'
        elif val==231:
            return 'c'
        elif val>=232 and val<=235:
            return 'e'
        elif val>=236 and val<=239:
            return 'i'
        elif val==240:
            return 'd'
        elif val==241:
            return 'n'
        elif val>=242 and val<=248:
            return 'o'
        elif val==154:
            return 's'
        elif val>=249 and val<=252:
            return 'u'
        elif val==253 or val==255:
            return 'y'
        elif val==254:
            return 'Th'
        raise ('Something Wrong Error')
    
    def cleanString(self,string):
        newstring = string
        for symb in self._symbols:
            newstring = newstring.replace(symb,'')
        return newstring
    
    def parseToEnglish(self,string):
        #newstring = string#self.cleanString(string)
        outp = ''
        for i in range(len(string)):
            ch = string[i]
            if self.isUmlaut(ch):
                ch = self.umlautToEnglish(ch)
            outp+=ch
        return outp
    
    def hasForeign(self,string):
        #string = self.cleanString(string)
        for char in string:
            if self.isValidEnglish(char) or self.isUmlaut(char) or char==' ' or char=='' or char in self._symbols or char=='nan':
                continue
            else:
                """old = ''
                with open('debug.txt','r+',encoding='utf-8') as fle:
                    old = fle.read()
                old += str(char)
                with open('debug.txt','w+',encoding='utf-8') as fle:
                    fle.write(old)"""
                return True
        return False
    
    def extractForeignString(self,string):
        outp = ''
        for ch in string:
            if self.isValidEnglish(ch)==False:
                if self.isUmlaut(ch)==False:
                    outp+=ch
        return outp
    
    def isEmpty(self,ls):
        if ls=='' or ls=='nan' or ls=='NaN' or ls==None:
            return True
        else :
            return False
    
        
"""
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
40 41 42 43
"""