# TITANIC
# Vamos a intentar resolver el problema con un solo modelo o funcion objetivo
import csv
import time

# import urllib.request
from urllib.request import Request, urlopen
from xml.dom.expatbuilder import parseString
from optparse import _parse_num

# open a connection to a URL using urllib
# webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')
# webUrl = urllib.urlopen('https://www.vademecum.es/atc-A03A')

# METODO A - WEBSCRAP 
# webUrl = urllib.request.urlopen('http://www.vademecum.es/atc-A03AA')
# get the result code and print it
# print ("result code: " + str(webUrl.getcode()))
# read the data from the URL and print it
# data = webUrl.read()
# print (data)

# METODO B - WEBSCRAP
# headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# reg_url = 'http://www.vademecum.es/atc-A03AA'
# req = urllib.request.urlopen(url=reg_url, headers={'User-Agent': 'Mozilla/5.0'}) 
# html = req.read() 


# METOCO C - WEBSCRAP
def comenzar():
    outF = open("myOutFile.txt", "w")
    url_root = 'https://www.vademecum.es/'
    url_add = 'atc'
    camino = 'Clasificacion ATC'
    global WEBS_TOTAL
    WEBS_TOTAL = 0
    global MEDS_TOTAL
    MEDS_TOTAL = 0
    print('----------------------------')
    print('WEB SCRAPPING DEL VADEMECUM')
    print(' ')
    print(' ')

    def calcu():
        global WEBS_TOTAL
        WEBS_TOTAL = WEBS_TOTAL + 1

    def calcu2():
        global MEDS_TOTAL
        MEDS_TOTAL = MEDS_TOTAL + 1

    def scrap(url_rt, url_ad):
        # global WEBS_TOTAL
        # WEBS_TOTAL = WEBS_TOTAL + 1
        # wbtot = str(WEBS_TOTAL)
        global WEBS_TOTAL
        global MEDS_TOTAL
        calcu()
        wbtot = str(WEBS_TOTAL)
        medtot = str(MEDS_TOTAL)
        print('')
        print('LEYENDO URL ' + wbtot + ', +' + medtot + ' Medtos. -> ' + url_rt + url_ad)
        req = Request(url_rt + url_ad, headers={'User-Agent': 'XYZ/3.0'})
        webpage = urlopen(req).read() 
        # outF = open("myOutFile.txt", "a")
        data = webpage.decode('UTF-8', 'strict') 
        d1 = data.replace('&aacute;', 'á')
        d2 = d1.replace('&eacute;', 'é')
        d3 = d2.replace('&iacute;', 'í')
        d4 = d3.replace('&oacute;', 'ó')
        d5 = d4.replace('&uacute;', 'ú')
        d6 = d5.replace('&Aacute;', 'Á')
        d7 = d6.replace('&Eacute;', 'É')
        d8 = d7.replace('&Iacute;', 'Í')
        d9 = d8.replace('&Oacute;', 'Ó')
        d10 = d9.replace('&uacute;', 'ú')
        d11 = d10.replace('&ntilde;', 'ñ')
        d12 = d11.replace('&Ntilde;', 'Ñ')
        d13 = d12.replace('&uuml;', 'ü')
        d14 = d13.replace('&Uuml;', 'Ü')
        d15 = d14.replace('&nbsp;', ' -> ')
        # outF.write(d15)
        # outF.close()
        return d15

    def lectura(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 0 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura1(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura1(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura1(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 1 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura2(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura2(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura2(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 2 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist ] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura3(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura3(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura3(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 3 -> ' + Camino)
        index = len(string)
        ind = -index
        global MEDS_TOTAL
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura4(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura4(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura4(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 4 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist ] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura5(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura5(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura5(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 5 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura6(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura6(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura6(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 6 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura7(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura7(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura7(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 7 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura8(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura8(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura8(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 8 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -100:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura9(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura9(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura9(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 9 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura10(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura10(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura10(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 10 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura11(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura11(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura11(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 11 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura12(url_root2, url_add3, camin)
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                lectura12(url_root2, url_add3, camin)
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    def lectura12(url_root2, url_add2, Camino):
        string = scrap(url_root2, url_add2)
        print ('-NIVEL 12 -> ' + Camino)
        index = len(string)
        global MEDS_TOTAL
        ind = -index
        cont = 0
        cont2 = 0
        while ind < -1000:
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 34] == '"') & (string[ind + 35] == 's') & (string[ind + 36] == 'm') & (string[ind + 37] == 'a') & (string[ind + 38] == 'l') & (string[ind + 39] == 'l') & (string[ind + 40] == '-'):
                cont2 = cont2 + 1
                calcu2()
                ind1 = 0
                YA = 0
                clist = 0
                list1 = list('                                                                                                                                                ')
                while YA != 2:
                    if (YA == 1) & (string[ind1 + ind + 60] == '<') & (string[ind1 + ind + 61] == '/') & (string[ind1 + ind + 62] == 'a') & (string[ind1 + ind + 63] == '>'):
                        YA = 2
                    if YA == 1:
                        if (string[ind1 + ind + 60] != ' '):
                            list1[clist] = string[ind1 + ind + 60]
                        if (string[ind1 + ind + 60] == ' '):
                            list1[clist] = '@'
                        clist = clist + 1
                    if (string[ind1 + ind + 60] == ' ') & (string[ind1 + ind + 59] == '-') & (string[ind1 + ind + 58] == ' '):
                        YA = 1
                    ind1 = ind1 + 1
                list1[clist] = ''
                medicament = ''.join(list1)
                medicament = medicament.replace(' ', '')
                medicament = medicament.replace('@', ' ')
                outF.write(medicament + '@' + Camino + '¡')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 4] == '<') & (string[ind + 5] == 'a') & (string[ind + 6] == ' ') & (string[ind + 7] == 'c') & (string[ind + 8] == 'l') & (string[ind + 9] == 'a') & (string[ind + 10] == 's') & (string[ind + 11] == 's') & (string[ind + 12] == '=') & (string[ind + 14] == 'b') & (string[ind + 15] == 'u') & (string[ind + 16] == 't') & (string[ind + 17] == 't') & (string[ind + 18] == 'o') & (string[ind + 19] == 'n') & (string[ind + 20] == ' ') & (string[ind + 21] == 'a') & (string[ind + 22] == 't') & (string[ind + 23] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 23] != '"':
                    list1[ind1] = string[ind + 9 + 23 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 23]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 23 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 23] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 23] == '<') & (string[ind + ind1 + ind2 + 9 + 23 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 23 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 23 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                print(' * * * ERROR * * * Sobrepasa los 12 niveles')
            if (string[ind] == '<') & (string[ind + 1] == 'l') & (string[ind + 2] == 'i') & (string[ind + 3] == '>') & (string[ind + 5] == '<') & (string[ind + 6] == 'a') & (string[ind + 7] == ' ') & (string[ind + 8] == 'c') & (string[ind + 9] == 'l') & (string[ind + 10] == 'a') & (string[ind + 11] == 's') & (string[ind + 12] == 's') & (string[ind + 13] == '=') & (string[ind + 15] == 'b') & (string[ind + 16] == 'u') & (string[ind + 17] == 't') & (string[ind + 18] == 't') & (string[ind + 19] == 'o') & (string[ind + 20] == 'n') & (string[ind + 21] == ' ') & (string[ind + 22] == 'a') & (string[ind + 23] == 't') & (string[ind + 24] == 'c'):
                cont = cont + 1
                ind1 = 0
                url_add1 = '                                                                                   '
                list1 = list(url_add1)
                list2 = list('                                                                                                                                                                                                        ')
                while string[ind + ind1 + 9 + 24] != '"':
                    list1[ind1] = string[ind + 9 + 24 + ind1 + 1]
                    ind1 = ind1 + 1
                list1[ind1 - 1] = ''
                YA = 0
                ind2 = 0
                dif = 0
                while YA != 2:
                    if YA == 1:
                        list2[ind2 - dif - 1] = string[ind + ind1 + ind2 + 9 + 24]
                        if list2[ind2 - dif - 1] == ' ':
                            list2[ind2 - dif - 1] = '#'
                    if (string[ind + ind1 + ind2 + 9 + 24 - 1] == '-') & (string[ind + ind1 + ind2 + 9 + 24] == ' '):
                        YA = 1
                        dif = ind2
                    if (string[ind + ind1 + ind2 + 9 + 24] == '<') & (string[ind + ind1 + ind2 + 9 + 24 + 1] == '/') & (string[ind + ind1 + ind2 + 9 + 24 + 2] == 'a') & (string[ind + ind1 + ind2 + 9 + 24 + 3] == '>'):
                        YA = 2
                    ind2 = ind2 + 1
                list2[ind2 - dif - 1] = ''
                list2[ind2 - dif - 2] = ''
                ultimo = ''.join(list2)
                ultimo = ultimo.replace(' ', '')
                ultimo = ultimo.replace('#', ' ')
                camin = Camino
                camin = camin + ';' + ultimo
                url_add3 = ''.join(list1)
                url_add3 = url_add3.replace(" ", "")
                print(' * * * ERROR * * * Sobrepasa los 12 niveles')
            ind = ind + 1
        conn = str(cont)
        conn2 = str(cont2)
        print ('  -' + url_add2 + ' = ' + conn)
        print ('  -pppios = ' + conn2)
        return(cont)

    contador = lectura(url_root, url_add, camino)
    wto=str(WEBS_TOTAL)
    mto=str(MEDS_TOTAL)
    print('')
    print('--------------------------------------')
    print('   * * * FINALIZADO EL SCRAP * * *')
    print('--------------------------------------')
    print('')
    print(' -> TOTAL DE PAGINAS EXPLORADAS     = ' + wto + ' páginas web')
    print(' -> TOTAL DE MEDICINAS ENCONTRADAS  = ' + mto + ' medicinas')
    print('')
    print('--------------------------------------')
    outF.close()


comenzar()

# IMPORTAMOS LOS DATOS TRAIN DESDE EL CSV
with open('train.csv', newline='') as csvfile:
    data_bruta = list(csv.reader(csvfile))

# CADA ENTRADA DE LA LISTA TIENE LA SIGUIENTE CONFIGURACION 
# ['0.PassengerId', '1.Survived', '2.Pclass', '3.Name', '4.Sex', '5.Age', '6.SibSp', '7.Parch', '8.Ticket', '9.Fare', '10.Cabin', '11.Embarked']
print(data_bruta[0])
print(' ')
TOTAL_DATOS = len(data_bruta) - 1
print('Existe un total de' , TOTAL_DATOS, 'individuos a estudiar en el TRAIN SET')
print(' ')
time.sleep(1.5)

# 1 - VAMOS A HACER EL ESTUDIO PREVIO DE LOS DATOS
print('ESTUDIO DE LOS DATOS ORIGINALES')

# Calculamos primero datos globales de supervivencia
Rate_survive = 0
for x in data_bruta:
    if x[1] == '1':
        Rate_survive = Rate_survive + 1
print('Sobreviven', Rate_survive, 'personas (', Rate_survive / TOTAL_DATOS * 100, '% de los navegantes)')
print(' ')

# -> PCLASS (Variable sencilla de estudiar)
print(' -PCLASS')
PR_Pclass = [0, 0, 0]
N_Pclass = [0, 0, 0]
for x in data_bruta:
    if x[2] == '1':
        N_Pclass[0] = N_Pclass[0] + 1
        if x[1] == '1':
            PR_Pclass[0] = PR_Pclass[0] + 1
    if x[2] == '2':
        N_Pclass[1] = N_Pclass[1] + 1
        if x[1] == '1':
            PR_Pclass[1] = PR_Pclass[1] + 1
    if x[2] == '3':
        N_Pclass[2] = N_Pclass[2] + 1
        if x[1] == '1':
            PR_Pclass[2] = PR_Pclass[2] + 1
N_suman = N_Pclass[0] + N_Pclass[1] + N_Pclass[2]
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
PR_Pclass[0] = PR_Pclass[0] / N_Pclass[0]
PR_Pclass[1] = PR_Pclass[1] / N_Pclass[1]
PR_Pclass[2] = PR_Pclass[2] / N_Pclass[2]
print(' ', PR_Pclass)
print(' ', N_Pclass)
print('')
time.sleep(1.5)

# -> GENDER or SEX (Variable sencilla de estudiar)
print(' -GENDER')
PR_gender = [0, 0]
N_gender = [0, 0]
for x in data_bruta:
    if x[4] == 'female':
        N_gender[0] = N_gender[0] + 1
        if x[1] == '1':
            PR_gender[0] = PR_gender[0] + 1
    if x[4] == 'male':
        N_gender[1] = N_gender[1] + 1
        if x[1] == '1':
            PR_gender[1] = PR_gender[1] + 1
N_suman = N_gender[0] + N_gender[1]
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
PR_gender[0] = PR_gender[0] / N_gender[0]
PR_gender[1] = PR_gender[1] / N_gender[1]
print(' ', PR_gender)
print(' ', N_gender)
time.sleep(1.5)
print('')

# -> EMBARKED (Variable sencilla de estudiar)
print(' -EMBARKED')
PR_embarked = [0, 0, 0]
N_embarked = [0, 0, 0]
for x in data_bruta:
    if x[11] == 'C':
        N_embarked[0] = N_embarked[0] + 1
        if x[1] == '1':
            PR_embarked[0] = PR_embarked[0] + 1
    if x[11] == 'Q':
        N_embarked[1] = N_embarked[1] + 1
        if x[1] == '1':
            PR_embarked[1] = PR_embarked[1] + 1
    if x[11] == 'S':
        N_embarked[2] = N_embarked[2] + 1
        if x[1] == '1':
            PR_embarked[2] = PR_embarked[2] + 1
N_suman = N_embarked[0] + N_embarked[1] + N_embarked[2]
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
PR_embarked[0] = PR_embarked[0] / N_embarked[0]
PR_embarked[1] = PR_embarked[1] / N_embarked[1]
PR_embarked[2] = PR_embarked[2] / N_embarked[2]
print(' ', PR_embarked)
print(' ', N_embarked)
time.sleep(1.5)
print('')

# -> HONOUR (forma parte del nombre y se refiere al estatus del viajero, sencillo de estudiar)
print(' -HONOUR')
Honours = ('Mr.', 'Mrs.', 'Miss.', 'Master.', 'Rev.', 'Ms.', 'Don.', 'Mme.', 'Major.', 'Dr.', 'Col.', 'Mlle.', 'Capt.')
print(' ', Honours)
PR_honour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N_honour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = -1
for x in Honours:
    i = i + 1
    j = 0
    for y in data_bruta:
        j = j + 1
        if y[3].__contains__(x):
            N_honour[i] = N_honour[i] + 1
            if y[1] == '1':
                PR_honour[i] = PR_honour[i] + 1
N_suman = sum(N_honour)
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
i = -1
for x in PR_honour:
    i = i + 1
    PR_honour[i] = x / N_honour[i]
print(' ', PR_honour)
print(' ', N_honour)
time.sleep(1.5)
print('')

# -> SIBLINGS AND SPOUSES ()
print(' -SIBLING AND SPOUSE')
SSValues = ('0', '1', '2', '3', '4', '5', '6', '7', '8')
PR_SSValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
N_SSValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = -1
for x in SSValues:
    i = i + 1
    j = 0
    for y in data_bruta:
        j = j + 1
        if y[6] == x:
            N_SSValues[i] = N_SSValues[i] + 1
            if y[1] == '1':
                PR_SSValues[i] = PR_SSValues[i] + 1
N_suman = sum(N_SSValues)
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
i = -1
for x in PR_SSValues:
    i = i + 1
    if N_SSValues[i] == 0:
        PR_SSValues[i] = 0
    if N_SSValues[i] != 0:
        PR_SSValues[i] = x / N_SSValues[i]
print(' ', PR_SSValues)
print(' ', N_SSValues)
time.sleep(1.5)
print('')

# -> PARENTS AND CHILDRENS ()
print(' -PARENTS AND CHILDRENS')
PCValues = ('0', '1', '2', '3', '4', '5', '6')
PR_PCValues = [0, 0, 0, 0, 0, 0, 0]
N_PCValues = [0, 0, 0, 0, 0, 0, 0]
i = -1
for x in PCValues:
    i = i + 1
    j = 0
    for y in data_bruta:
        j = j + 1
        if y[7] == x:
            N_PCValues[i] = N_PCValues[i] + 1
            if y[1] == '1':
                PR_PCValues[i] = PR_PCValues[i] + 1
N_suman = sum(N_PCValues)
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
i = -1
for x in PR_PCValues:
    i = i + 1
    if N_PCValues[i] == 0:
        PR_PCValues[i] = 0
    if N_PCValues[i] != 0:
        PR_PCValues[i] = x / N_PCValues[i]
print(' ', PR_PCValues)
print(' ', N_PCValues)
time.sleep(1.5)
print('')

# -> AGE (Intentaremos crear diferentes grupos de edad con un numero de muestras similar)
Grupos = [0, 11, 22, 40, 100]
PR_Age = [0, 0, 0, 0]
N_Age = [0, 0, 0, 0]
i = -1
for x in Grupos:
    i = i + 1
    j = 0
    if i > 0:
        for y in data_bruta:
            j = j + 1
            if j > 1:
                edad = float(y[5])
                print(edad)

                
def ff(x):
    return x[1] + x[2] + x[3] + x[4] 
