from os.path import abspath

class Gestore:

#questa classe di supporto permette di ottenere il path assoluto del file corrente
    def returnPth(self):
        abp = abspath("")
        split = [abp.split("\\")]
        pthArr = []
        finPth = ""

        for element in split:
            if element == split[len(split) - 1]:
                pthArr += element
        for x in range(len(pthArr)-1):
            finPth += str(pthArr[x]) + "/"

        return finPth