"""
LIB Collections
MÓDULO COUNTER
    - Retorna um "dicionário", porém o type será collections-counter
    - Geralmente utilizado para recorrêcias
    - Quando precisamos processar dados massivos
"""
from collections import Counter

'''
frase = 'Python é legal'.lower()
print(frase.count('o'))

lista = ['Leonardo Alves', 'Juca Alves', 'Maria Alfredo',
         'Fernanda Almeida', 'Juca Alves', 'Leonardo Alves',
         'Maria Trindade', 'Maria Trindade', 'Paola Souza',
         'Paola Souza', 'Paola Souza', 'Manoel Bispo']

resposta = Counter(lista)
print(type(resposta))

for chave, valor in resposta.items():
    # if valor == 1:
    print(f'{chave} ==> {valor}')
'''

musica = '''Ó, nem me falou teu sobrenome pra eu te achar no Insta
Eu tô pra ver se alguém que eu conheço te conhece, ahn
Disse pra mim que foi bom me ver na pista
Que pessoalmente é melhor que na Internet, ahn

Ela brinca com a postura do homem
Joga na cara e depois ela some
Diz que perde pra minha cara de tralha
E que não acreditava que eu tava na 11, ahn

A cara do freio, que deixa ela louca, ahn
Bem que eu te avisei que vou beijar tua boca
Sem medo de nada, cheia de marra, maravilhosa
Pra acabar com tua marra eu chego no ouvido e falo: Gostosa

Cansado de ouvir quem nunca fez nada por mim
Eu devo nada a ninguém, nós pode fazer o que tiver a fim
Tipo, linda, dança pra mim
Faz o que tu quiser, tu sabe que eu tô a fim
Vai me dizer que não quer?

Dentro do carro com ela do lado eu fico suave
Se ela tá no volante é tipo avião pilotando a nave
Eu canetando várias frase e fazendo barulho
Escrevendo a vida e falando de tudo
Enquanto eles tão falando isso e aquilo
Meu som toca nos quatro canto do mundo, é
Eu vou beijar tua boca tirando tua roupa
Impossível querer te trocar por outra

[MC Chris]
Quero sentir a sensação da primeira vez que te vi
Explicar pro coração que cê faz falta nem sempre dá
Te vejo nos melhores sonhos, tenho planos pra nós
Se te beijo, ouço o som dos anjos
Com seu rosto, sua voz, tô indo te buscar
Ter onde voltar, pra onde chegar, chegar
Cê me deixa sem ar
Pra nunca faltar motivos pra comemorar

Sem compromisso, cê gosta disso
Amor como o nosso é tão bom
Muda esse disco, eu não corro risco
Minha melhor inspiração

[MC Ryan SP e MC Chris]
A medida do amor é amar sem ter medida
Por isso eu te amei muito, mulher
Quebrei a cara confiando em amar e você me ensinou como é
Me entreguei nessa ilusão, fui cobaia nessa palhaçada

Não vou mais me apaixonar, vou viver na revoada
Pra todo game over vai existir um play
Você jogou fora todo amor que eu te dei
Assim que quer, assim será, eu vou pra não voltar

Tubarão, se ela brota na sua revoada?
Juro, não vou deixar ela entrar
Se ela aparecer no quarto pelada?
Ah me desculpa, eu vou ter que evitar

Mas se ela te liga na madrugada?
Caixa postal, não adianta ligar
E todas as vezes que eu te perdoei
Achando que o amor poderia vingar?

Nega, por que me rejeita? Fiquei na sarjeta
Culpa do amor metido à besta
Beba, esqueça da princesa, celebra a sexta-feira
A riqueza do amor é ter pureza e você não teve

[Lourena]
Você prometeu, prometeu um final feliz
Mas se esqueceu, esqueceu, esqueceu de mim
Se não quer se iludir, quer ficar na revoada
Como confiar em ti se você não para em casa?

Eu sou mulher pra caralho, só você não percebeu
Que teus amigos queriam fechamento como eu
Mas, danado, sem querer eu gostei de você
Reclamo se eu vejo outra te querendo
Não que eu goste assim, só tô a fim de bagunçar
Lourena que lançou a braba

Hoje eu te faço enlouquecer
O que eu pedir tu vai ter que fazer
Caso o contrário eu vou dizer
Que eu não te amo, várias queixas de você
Por que fez isso comigo?
Hein, Xamã?

[Xamã]
Estamos junto e separados, baby
Por que somos tão errados? Ahn
Cês duas de papin
Geral tá ligado que nós tem um lancin
Sem caô, diamante, filme e lanchin
A passagem tá mó cara, falta amor aí

Eu te amo desde os tempos lá de Sepetiba
Tinha um par de asas e uma calça comprida
Isopor vendendo Bud, cinco conto à vista
Cheio de marra, só pegava capa de revista

Me beije com lip tint, vamo resolver essa porra em cima do beat
Ou tu quer eu ou tu quer ela, decide
Nós dois fazendo surubão de Nikity City
Xamã demônio da Viking, vixe
Essa relação deixou minha mente mais triste
Ou tu quer eu ou tu quer ele, decide
Se tu quer golpe, eu sou do Karatê Kid
Tira o sutiã do cabide
Sem compromisso, cê gosta disso
Fla-Flu, churrasco e cerva latão

A cara dos filho da Deise, ouvindo L7 bolado
Azzy tá vindo de lace, Xamãzin é o mais malvado
Deixa que eu me viro, deixa, de qualquer maneira
Baby, vou te amar pra vida inteira
Queixas, qual a cor das terças?
Por que não me beijas? Culpa do Xamã metido à besta

[Azzy]
Ei, quando você vem? Preciso saber pra eu não sair
Quero te ver, me resolver, amor, não faz assim
Então deixa eu te mostrar, aqui é teu lugar
Contigo não tenho segredo
Amor, você sabe que eu morro de medo da gente terminar

Nós bate de frente toda hora
Mas quando cê sai eu sempre choro
Pensa com carinho, vê se rola
Nós no escurinho, eu te devoro

Abraça meu papo que eu te abraço forte
Azar no jogo, muita fé na sorte
Não mente pra mim, não quero me enganar
Não, não, não, não, beija minha boca, beija
Os problemas deixa, deixa pra amanhã esses caô
Veja, numa sexta-feira, na praia, na beira
Amanhecendo e nós fazendo amor

[MC Poze do Rodo]
Oi, tá com saudade e quer me ver
E ama a minha pegada
Mas essa vida que eu levo
O tempo é curto, eu confesso
Bem que seria uma boa ter você por perto
Mas não tô podendo me apegar
Se for um lance, isso nós pode ver
A melhor forma de se entender

Mente criminosa, coração bandido
Não posso fugir desse meu instinto
Não faço poesia, faço trabalho lindo
Se o trem passar, melhor sair do trilho

É o Poze
Peita, a grana tá na mesa
Nós é faixa preta, têm várias princesa querendo fuder
Peita, Malak bandido, solta o beat ao vivo
Mente visionária faz acontecer

Oi, peita, a grana tá na mesa
Nós é faixa preta, têm várias princesa querendo fuder
Peita, Malak bandido, solta o beat ao vivo
Mente visionária faz acontecer

[Cynthia Luz]
Baby, eu te provo no contrário
Na boca que beija e nesse mesmo cenário
Todo dia eu quero o seu amor, eu nem disfarço
Baby, eu te chamei porque o nosso tempo é raro

Esquecer a dor nunca foi fácil
Valor do nosso laço, tu sempre do meu lado
Outras até tentaram, mas todas falharam
Nosso corpo é só um, pedidos em comum, só um

Peço a Deus que nos dê mais amor pra caminhar
Tire de nós o orgulho, a lembrança que sempre machuca
E nos meus olhos tu veja a vontade de te amar, amar
Sempre me escondo dessa escuridão que me assusta

Deixa que a gente se beija, chega de besteira
Pra nós todo dia é sexta-feira
Beija, sei que tu deseja, vem pra cama e beija
Baby, pode me culpar, enfim sós

Deixa que a gente se beija, chega de besteira
Pra nós todo dia é sexta-feira
Beija, sei que tu deseja, vem pra cama e beija
Baby, pode me culpar, enfim sós
Deixa, deixa, deixa
'''.lower()

palavras = musica.split()
contagem = Counter(palavras)
qtd10 = contagem.most_common(10)

# print(contagem)
# print(qtd10)

linha = 0

for dado in qtd10:
    for valor in enumerate(dado):
        print(valor[1], end=' ')

        linha += 1
        if linha % 2 == 0:
            print()








