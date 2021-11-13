# Condificador_de_texto

esse codificador de texto tera a utilidade de transformar texto em numeros com possibilidade de você mandar 
mensagem em numeros para alguem e ninguem sabera qual a mensagem e esses arquivos txt e todas as letras serao 
transformadas em minusculas(A -> a) e não aceita letras assentuadas (á,à,â,ã...) e para o codigo saber qual 
o tipo da tradução sera nessera ter a primeira linha apenas para definir o formato e para colocar os comandos
e entre os formatos(tipos) estão: 
# Csl
Transforma texto em numeros
exemplo: Oi -> 6940
               41
# Nmr
Transforma numeros em letras
exemplo> 6940
         41 > oi
# Csn
Tem a capacidade de transformar letras em numeros
e numeros em numeros, para deixar mais dificil a tradução
e tem a função de deixar mais dificil caso outra pessoa
que use o seu computador e saiba da existencia desse codificador de traduzir
exemplo: Oi -> 6940
               41
exemplo 2: 6940
           41 > 574
                578
                653
                3542
                0
                653
                2124

# Primeiros passos
após ter o codigo em mãos inicie-o, ele criará um arquivo.txt, um dicionario.json e um requirements
o dicionario serve para saber qual numero ele ira colocar para cada letra
exemplo:
"a":1
"b":2
"c":3
....
e você poderá alterar os numeros
o requirements servirá para você mostrar ao programa qual arquivo ele irá traduzir
e qual dicionario ele irá utilizar e para quantas letras por linha você quer que o arquivo tenha.
Para testar o programa escreva assim no arquivo (nao escreva essas chaves " {  } ":
{
csl
ola
}
e inicie o programa
# Comandos
os comandos ficarão na primeira linha junto com o tipo.
Atualmente existe 2 comandos:
"dic" e "lpl"
dic = dicionario
lpl = letras por linhas
e os comandos servem para caso você queira traduzir varios arquivos mas com dicionarios diferentes
e quantidade de letras por linha diferente e olhe um exemplos de utilização:
{
csl <"dic":"dicionario2.json">
ola
}
e para escrever mais comandos é so escrever uma virgula:
{
csl <"dic":"dicionario2.json","lpl":10>
ola
}
