import json

class Itens():
    def arquivos():
        class dados():
            arquivo = ""
            dicionario = ""
            letras_por_linha = 100
        try:
            req =  open('requirements.json','r' )
            req_json = json.load(req)
            dados.arquivo = req_json['Arquivo']
            dados.dicionario = req_json['Dicionario']
            dados.letras_por_linha = req_json['Letras_por_linha']
            
        except:
            new_req = open('requirements.json','w')
            json_ = {"Arquivo": "arquivo.txt","Dicionario": "dic.json","Letras_por_linha": 100}
            dados.arquivo = json_['Arquivo']
            dados.dicionario = json_['Dicionario']
            dados.letras_por_linha = json_['Letras_por_linha']
            json.dump(json_,new_req,indent=4 )
        finally:
            def config_lpl():
                dados.letras_por_linha -= 1
            config_lpl()
            return(dados)
    
    def verificar_arquivos():
        #arquivo
        err= False
        try:
            arquivo = open(Itens.arquivos().arquivo,'r')
        except:
            novo_arquivo = open(Itens.arquivos().arquivo,'w')
            err = True
        #dicionario
        try:
            dicionario = open(Itens.arquivos().dicionario,'r') 
        except:
            dicionario_json = {"a": 1, "b": 2, "c": 32, "d": 112, "e": 122, "f": 31, "g": 21, "h": 12, "i": 41, "j": 3, "k": 3213, "l": 876, "m": 545, "n": 4113, "o": 6940, "p": 5243, "q": 1245, "r": 23134, "s": 123, "t": 231, "u": 976, "v": 987, "w": 87, "x": 7654, "y": 42, "z": 78, " ": 0, "?": 52, "!": 60, "#": 64, "*": 65, "/": 341, "(": 765, ")": 751, "'": 523, "&": 141, "<": 423, ">": 424, ":": 1231, ";": 1233, "-": 421, "=": 323, ",": 56780, ".": 732, "0": 3542, "1": 2124, "2": 564, "3": 8754, "4": 653, "5": 4123, "6": 574, "7": 53, "8": 125, "9": 578}
            novo_dicionario = open(Itens.arquivos().dicionario,'w')
            json.dump(dicionario_json,novo_dicionario,indent=4)
            err = True
        # if err == True:
        #     Itens.verificar_arquivos()

    def verificar_formato(arquivo):
        class informations():
            tipo = ""
            texto = ""
        try:
            a = 1
            for linha in open(arquivo,'r').readlines():
                linha = str(linha)
                linha = linha.lower()
                linha = linha.strip()
                if a >= 1:
                    informations.tipo = linha
                    a-=1
                else:
                    informations.texto = informations.texto + linha + " "
        except:
            pass
        informations.texto = informations.texto.strip()
        return informations

    def csl(arq,dic,texto,cm):
        try:
            comando = ""
            try:
                comando = Itens.cm(cm)
            except:
                pass
            dicionario = json.load(open(dic,'r'))
            arquivo = open(arq,'w')
            arquivo.write('nmr '+str(comando)+'\n')
            for o in texto:
                for i in dicionario:
                    if o == i:
                        arquivo.write(str(dicionario[i]) + '\n')
                if o == "^":
                    arquivo.write("^" + '\n')
        except:
            pass

    def csn(arq,dic,texto,cm):
        try:
            comando = ""
            try:
                comando = Itens.cm(cm)
            except:
                pass
            dicionario = json.load(open(dic,'r'))
            arquivo = open(arq,'w')
            arquivo.write('csn '+str(comando)+'\n')
            for o in texto:
                for i in dicionario:
                    if o == i:
                        arquivo.write(str(dicionario[i]) + '\n')
                if o == "^":
                    arquivo.write("^" + '\n')
        except:
            pass

    def nmr(arq,arq2,dic,l_l,cm):
        try:
            comando = ""
            try:
                comando = Itens.cm(cm)
            except:
                pass
            dicionario = json.load(open(dic,'r'))
            letra_p_l = l_l
            with open(arq2,'w') as arq_2:
                arq_2.write('csl '+str(comando)+'\n')
                for i in arq:
                    i = i.strip()
                    i = i.lower()
                    i = str(i)
                    for o in dicionario:
                        if i == str(dicionario[o]):             
                            if letra_p_l >= 1:
                                arq_2.write(str(o))
                                letra_p_l -= 1
                            else:
                                arq_2.write(str(o) + "\n") 
                                letra_p_l = l_l 
                    if i == "^":
                        arq_2.write('\n'.strip())
                        letra_p_l = l_l
        except:
            pass

    def cm(cm):
        com = str(cm)
        back = com.find('{')
        forward = com.find('}')
        if back >-1 and forward > back:
            new_com = com[back+1:forward]
            texto = ""
            for i in new_com:
                if i == "'":
                    texto = texto + '"'
                else:
                    texto = texto + i
            
            new_com = "<" + texto + ">"
            return new_com
        else:
            return ""


def iniciar():
    arquivos = Itens.arquivos()
    Itens.verificar_arquivos()
    
    inf = Itens.verificar_formato(arquivos.arquivo)
    def comandos():
        comandos = inf.tipo[3:]
        comandos = comandos.strip()
        comandos = comandos.lower()

        back = comandos.find('<')
        forward = comandos.find('>')
        comands = comandos[back+1:forward]
        text = ""
        for i in comands:
            if i == "'":
                text = text + '"'
            else:
                text = text + i
        try:
            comandos_json= json.loads("{"+str(text)+"}")
            if back > -1 and forward > back:
                return comandos_json
            else:
                return 0
        except:
            return 0
    comando = comandos()

    if inf.tipo[:3] == "nmr":
        dic = arquivos.dicionario
        letras_p_l = arquivos.letras_por_linha
        try:
            if comandos != 0:
                try:
                    dic = comando['dic']
                except:
                    pass
                try:
                    letras_p_l = int(comando['lpl']) or int(comando['letras_por_linha'])
                except:
                    pass
        finally:
            Itens.nmr(open(arquivos.arquivo,'r').readlines(), arquivos.arquivo,dic,letras_p_l,comando)
    elif inf.tipo[:3] == "csl":
        dic = arquivos.dicionario
        try:
            if comandos != 0:
                try:
                    dic = comando['dic']
                except:
                    pass
        finally:
            Itens.csl(arquivos.arquivo,dic,inf.texto,comando)
    elif inf.tipo[:3] == "csn":
        dic = arquivos.dicionario
        try:
            if comandos != 0:
                try:
                    dic = comando['dic']
                except:
                    pass
        finally:
            Itens.csn(arquivos.arquivo,dic,inf.texto,comando)
    
        
iniciar()
