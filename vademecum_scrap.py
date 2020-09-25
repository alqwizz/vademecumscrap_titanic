import csv
import time

# import urllib.request
from urllib.request import Request, urlopen
from xml.dom.expatbuilder import parseString
from optparse import _parse_num


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
    wto = str(WEBS_TOTAL)
    mto = str(MEDS_TOTAL)
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
