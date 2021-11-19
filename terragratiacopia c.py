import random
import time
import sys

def inicio(save_game, indicador, sentenca):
    print('Bem-vindo a Terragratia.')
    time.sleep(1)
    load_game = str(input('Deseja carregar um jogo salvo? s/n\n'))
    if load_game in ['s']:
        save_game = int(input('Insira o código de save_game: '))
        if save_game >= 100:
            capitulo1_henriqueparte2(save_game, indicador, sentenca)
        else: inicio(save_game, indicador, sentenca)
    elif load_game in ['n']:
        introducao(save_game, indicador, sentenca, load_game)
    else:
        inicio(save_game, indicador, sentenca)
        
def gameover():
    print('\n')
    time.sleep(1)
    print('---------')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('GAME OVER')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('---------')
    time.sleep(1)
    print('\n')
    return

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./30)

def introducao(save_game, indicador, sentenca, load_game):
    print('\nEu abro meus olhos e percebo que: ')
    time.sleep(1)
    print('\n1) Minha cabeça dói')
    time.sleep(1)
    print('2) Estou atrasado')
    time.sleep(1)
    print('3) Aquilo foi um sonho')
    time.sleep(1)
    print('Dica: digite o número da escolha desejada e tecle enter')
    time.sleep(1)
    indicador = int(input())
    if indicador == 1:
        capitulo1_henrique(save_game, indicador, sentenca)
    elif indicador == 3:
        print('\n')
        time.sleep(1)
        print('Obs: recomenda-se jogar primeiro uma das duas primeiras histórias (opções 1) ou 2)) para prosseguir com esse personagem.')
        time.sleep(5)
        print('\n')
        time.sleep(1)
        print('Deseja continuar? s/n')
        load_game = str(input(''))
        if load_game == 's':
            voceacreditaemterragratia(indicador)
        else:
            introducao(save_game, indicador, sentenca, load_game)
    else:
        capitulo1iglesias(indicador, save_game2, sentenca)


def grito():
    sentenca = str(input('\nDica: digite a seguir sentença que seja proferir\n'))
    print('\n')
    return sentenca.upper()

def pilar(indicador):
    print('O que devo fazer?')
    time.sleep(1)
    print('1) Soltar-me do pilar')
    time.sleep(1)
    print('2) Pegar a corda e fingir que ainda estou com as mãos presas')
    time.sleep(2)
    while indicador != 22:
        indicador = int(input('\n'))
        if indicador == 1:
            indicador = 21
            print('Tento me soltar do pilar, mas percebo que não tenho forças o suficiente.\n')
            time.sleep(3)
            print('Talvez outra coisa?\n')
            time.sleep(1)
            print('1) Soltar-me do pilar')
            time.sleep(1)
            print('2) Pegar a corda e fingir que ainda estou com as mãos presas')
            time.sleep(2)
        else:
            indicador = 22
            print('Pego a corda e enrolo em minhas mãos como se ainda estivesse com elas presas.')
            time.sleep(3)
    return
    
def nadaacontece():
    print('\n')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('Nada.')
    time.sleep(1)
    return

def interpretarpistas(indicador):
    print('\n')
    time.sleep(1)
    print('O que será que isso significa?')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('1) Fui raptado por uma seita')
    time.sleep(1)
    print('2) Cometi um crime e isso é uma tentativa de justiça popular')
    time.sleep(1)
    print('3) Estou alucinando')
    time.sleep(1)
    print('4) Sou adepto de uma religião que envolve usar entorpecentes ("E" posso ou não estar alucinando por causa deles)')
    time.sleep(1)
    indicador = int(input('\n'))
    if indicador == 1:
        print('\n')
        time.sleep(1)
        print('Devo ter sido raptado por alguma espécie de seita, espero que não sejam terroristas. Essa ideia toda parece uma maluquice, mas vou dar uma mínima credibilidade a minha capacidade de conectar os pontos.')
        time.sleep(6)
        indicador = 41
        print('\n')
        time.sleep(3)
        variacao1capitulo1henrique(indicador)
        return 
    elif indicador == 2:
        print('\n')
        time.sleep(1)
        print('Devo ter feito alguma coisa de errado, essas pessoas devem estar bravas comigo. Será que me prenderam aqui dentro?')
        time.sleep(5)
        indicador = 42
        print('\n')
        time.sleep(3)
        variacao1capitulo1henrique(indicador)
        return 
    elif indicador == 4:
        print('\n')
        time.sleep(1)
        print('Ok, essa hipótese vai soar bizarra. E se eu estiver dentro de uma comunidade religioso por vontade próprio e estou passando por um ritual de iniciação?')
        time.sleep(6)
        indicador = 44
        print('\n')
        time.sleep(3)
        variacao1capitulo1henrique(indicador)
        return 
    else:
        print('\n')
        time.sleep(1)
        print('Não consigo confiar em nada que percebo no estado que estou, devo estar delirando. Qualquer informação vinda dos meus sentidos não deve ser totalmente confiável.')
        time.sleep(6)
        indicador = 43
        print('\n')
        time.sleep(3)
        variacao1capitulo1henrique(indicador)
        return 

def descobrirperguntando(indicador):
    print('1) Fazer perguntas aos carregadores')
    time.sleep(1)
    print('2) Tentar fugir, agora que sei um pouco do cenário')
    time.sleep(1)
    print('3) Ficar quieto')
    time.sleep(1)
    indicador = int(input('\n'))
    if indicador == 1:
        fazerperguntasaoscarregadores()
        return
    elif indicador == 2:
        time.sleep(1)
        print('Resolvo descer do leito e sair em disparada. De alguma forma, com a adrenalina do momento, achei que teria uma chance contra dezenas de pessoas...')
        time.sleep(7)
        print('Mão soltas ou presas... pouco importa agora. Percebo meu corpo perfurado por uma flecha. Tudo fica branco...')
        time.sleep(6)
        gameover()
        input('Tecle enter para retornar ao checkpoint')
        descobrirperguntando(indicador)
    else:
        return

def interagircarregadores(indicador):
    print('\n')
    time.sleep(1)
    print('⦁	Preciso ir ao banheiro.')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('⦁	Você não precisa, apenas deseja. – Disse uma das pessoas a me carregar.')
    time.sleep(4)
    print("\n")
    time.sleep(1)
    return

def fazerperguntasaoscarregadores(indicador):
    time.sleep(1)
    print('⦁	Para onde estão me levando? Por que estou aqui?')
    time.sleep(3)
    print('⦁	Todas as respostas virão em seu momento. - Disse algum homem na frente.')
    time.sleep(4)
    return

def prologo():
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('-------')
    time.sleep(1)
    print('PRÓLOGO')
    time.sleep(1)
    print('-------')
    time.sleep(1)
    print('Já se foi um certo tempo desde que passei pela Libertação, mas ainda lembro como se fosse hoje. Inclusive, igual naquele dia, ainda não tenho tanta informação do que está acontecendo nessa vila ou por que estou aqui, mas a comunidade é amigável o suficiente com quem faz poucas perguntas. Tenho um lugar para ficar, comida e água. Ah, e trabalho, preciso trabalhar. Estou me comportando como se tudo tivesse normal e então quando não estiverem preparados, vou fugir. Uma das formas de se recuperar a própria memória é estando num lugar familiar, e esse lugar é a minha própria casa, longe daqui.')
    time.sleep(15)
    print('\n')
    time.sleep(1)
    input('Tecle enter para reiniciar')
    inicio(save_game, indicador, sentenca)

def capitulo1_henrique(save_game, indicador, sentenca):
    print('\nMinha cabeça dói.')
    time.sleep(1)
    print('Sinto o cheiro de óleo velho.')
    time.sleep(1)
    print('Um fino ruído atormenta meus tímpanos e sua vibração desce pela minha espinha.')
    time.sleep(2)
    print('Olho para minha frente na esperança de ver a mesa que eu estava encarando aparentemente apenas alguns minutos atrás, e perceber que apenas estava mal de bêbado. ')
    time.sleep(4)
    print('Tento coçar a cabeça e não consigo.')
    time.sleep(2)
    print('Minhas mãos estão amarradas.')
    time.sleep(2)
    print('O material parece frágil, acho que consigo arrebentar.')
    time.sleep(2)
    print('Mas ao mesmo tempo não sinto vontade de tentar, como se de alguma forma eu soubesse que não era uma boa ideia. ')
    time.sleep(3)
    print('\n')
    time.sleep(2)
    print('É levemente confuso, uma leveza que não me permite sentir apavorado.')
    time.sleep(2)
    print('Não consigo enxergar muita coisa, ou pelo menos entender o que vejo.')
    time.sleep(2)
    print('Por um momento apenas resolvo pensar como seria se eu tivesse sido sequestrado.')
    time.sleep(2.5)
    print('Porém, nesse caso, não faria tanto sentido.')
    time.sleep(1.5)
    print('Não sou de família rica, não tenho nenhum parente com muito dinheiro.')
    time.sleep(2)
    print('Provavelmente ninguém nem iria perceber que sumi depois de muitos dias.')
    time.sleep(2)
    print('Sinto sede, minha garganta está seca.')
    time.sleep(2)
    print('Há quanto tempo será que estou aqui?')
    time.sleep(2)
    print('\n1) Alguns dias?')
    time.sleep(1)
    print('2) 1 mês?')
    time.sleep(1)
    print('3) Muito tempo?')
    time.sleep(1)
    print('4) Pouco tempo, talvez algumas horas?')
    time.sleep(1)
    indicador = int(input('5) Não sei...\n'))
    if indicador == 1:
        time.sleep(1)
        print('\n')
        print('Hmmmmm... talvez alguns dias...')
    elif indicador == 2:
        time.sleep(1)
        print('\n')
        print('Hmmmmm... pelo jeito um mês inteiro...')
    elif indicador == 3:
        time.sleep(1)
        print('\n')
        print('Hmmmmm... não sei quanto tempo, mas sei que bastante...')
    elif indicador == 4:
        time.sleep(1)
        print('\n')
        print('Hmmmmmm... não sei quanto tempo, mas talvez tenho que ter chegado aqui recentemente...') 
    else:
        indicador = 5
        time.sleep(1)
        print('\n')
        print('Hmmmmm... difícil dizer...')
    print('\n')
    time.sleep(3)
    if indicador != 4:
        print('Não me sinto desnutrido e nem faminto, mas tenho a impressão de que tempo se passou.')
    else:
        print('Não me sinto desnutrido e nem faminto, então pouco tempo deve ter passado... ou será que não?')
    time.sleep(3)
    print('É uma mudança brusca do que lembro por último, perante minha situação.')
    time.sleep(3)
    print('É como se a minha vida antiga tivesse ido embora e eu soubesse disso.')
    time.sleep(3)
    print('\n')
    time.sleep(2)
    print('Que estivesse muito e muito longe.')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('Escuto pessoas conversando do lado de fora.')
    time.sleep(2)
    print('Não sei o que estão falando.')
    time.sleep(2)
    print('Não consigo decifrar, mas são dezenas de pessoas.')
    time.sleep(2)
    print('Alguém bateu na porta.')
    time.sleep(2)
    print('Há uma porta na direção leste em relação a mim.')
    time.sleep(2)
    print('Será que sabem que estou aqui?')
    time.sleep(2)
    print('\n')
    time.sleep(1)
    print('O que devo fazer?')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('1) Gritar')
    time.sleep(1)
    print('2) Soltar-se')
    time.sleep(1)
    print('3) Fingir de morto')
    time.sleep(1)
    indicador = int(input('4) Aguardar e tentar ouvir a conversa\n'))
    if indicador == 1:
        time.sleep(1)
        print('\n')
        print('Puxo todo ar que os pulmões me permitem e grito:')
        time.sleep(2)
        print('\n')
        time.sleep(1)
        print('⦁	',grito())
        time.sleep(2)
        nadaacontece()
        print('Talvez se eu tentar algo diferente?')
        time.sleep(1)
        print('1) Gritar novamente')
        time.sleep(1)
        print('2) Ficar quieto')
        time.sleep(1)
        indicador = int(input('\n'))
        if indicador == 1:
            indicador = 11
            print('\n')
            time.sleep(3)
            variacao1capitulo1henrique(indicador)
        else:
            indicador = 12
            print('\n')
            time.sleep(3)
            variacao1capitulo1henrique(indicador)
    elif indicador == 2:
        time.sleep(1)
        print('\n')
        print('Uso toda a minha força para tentar separar uma mão da outra.')
        time.sleep(3)
        print('Percebo que estou também amarrado junto a um pilar que estou encostado.')
        time.sleep(3)
        print('\n')
        time.sleep(1)
        print('Consigo livrar minhas mãos.')
        time.sleep(1)
        print('\n')
        time.sleep(1)
        pilar(indicador)
    elif indicador == 3:
        time.sleep(1)
        print('\n')
        print('Provavelmente vão perceber que estou vivo, mas fingir que estou inconsciente deve me dar pelo menos alguma vantagem...')
        time.sleep(2)
        print('\n')
        time.sleep(3)
        variacao1capitulo1henrique(indicador)
    elif indicador == 4:
        time.sleep(1)
        print('\n')
        print('Hmmmmmm... são muitas pessoas murmurando. Concentro-me, mesmo atordoado, e tento fazer sentido das palavras que ouço e entendo.') 
        time.sleep(5)
        print('São conversas que parecem acontecer em torno das palavras "crime", "renascimento", "fé", "sociedade".')
        time.sleep(4)
        interpretarpistas(indicador)
    else:
        indicador = 5
        time.sleep(1)
        print('\n')
        print('Hmmmmm... difícil dizer...')
    print('\n')
    time.sleep(3)
    save_game = indicador
    # or indicador == 12 or indicador == 3 or indicador == 41 or indicador == 42 or indicador == 43 or indicador == 44:
    save_game += 100
    print('Obs: jogo salvo, código ', save_game)
    capitulo1_henriqueparte2(save_game, indicador,sentenca)

def capitulo1_henriqueparte2(save_game, indicador, sentenca):       
    print('Desabo no chão.')
    time.sleep(2)
    print('Estou mais fraco do que pensei.')
    time.sleep(2)
    print('Então sinto dois pares de mãos a me carregarem e me levarem para fora do pequeno edifício com o auxílio do que imagino ser uma espécie de leito carregável.')
    time.sleep(7)
    print('Sinto vontade de urinar.')
    time.sleep(2)
    print('Isso é bom e ruim.')
    time.sleep(2)
    print('Significa que bebi água recentemente. ')
    time.sleep(3)    
    print('Mas também significa que agora preciso satisfazer minha necessidade fisiológica de alguma forma.')
    time.sleep(5)
    print('Existem banheiros onde estou?')
    time.sleep(2)
    print('Onde estou, na verdade? ')
    time.sleep(2)
    print('Não sinto que estou completamente acordado, muito provavelmente essa é a sensação de ter sido privado de carboidratos por um extenso período de tempo.')
    time.sleep(7)
    print('\n')
    time.sleep(1)
    print('---------------------------------')
    time.sleep(1)
    print('Novo objetivo: descubra onde está')
    time.sleep(1)
    print('----------------------------------')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('O que devo fazer?')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('1) Fazer perguntas aos carregadores')
    time.sleep(1)
    print('2) Pular do leito e tentar fugir')
    time.sleep(1)
    print('3) Ficar quieto')
    time.sleep(1)
    indicador = int(input('\n'))
    while indicador == 2:
        print('Resolvo ignorar meus dons estratégicos e fugir em território desconhecido para qualquer lugar onde meus pés me levassem.')
        time.sleep(6)
        print('Me jogo no chão e me levanto cambaleando, correndo em direção ao Sol que a pouco me cegava.')
        time.sleep(5)
        if save_game == 122:
            print('Minhas mãos soltas me dão a vantagem de poder balancear meu equilíbrio e correr um pouco... apenas para desabar e ser raptado novamente, dessa vez recebendo uma seringa no pescoço...')
            time.sleep(7)
            print('...')
            time.sleep(1)
            gameover()
            time.sleep(1)
            input('Tecle enter para retroceder ao checkpoint')
            print('\n')
        else:
            print('Apenas para passos depois tropeçar e cair no chão... sendo raptado novamente... Talvez se eu estivesse soltado as mãos?')
            time.sleep(6)
            print('Recebo uma seringa no pescoço e tudo fica escuro...')
            time.sleep(3)
            gameover()
            time.sleep(1)
            input('Tecle enter para retroceder ao checkpoint')
            print('\n')
        print('---------------------------------------------')
        time.sleep(1)
        print('\n\n\n\n\n\n')
        print('O que devo fazer?')
        time.sleep(1)
        print('\n')
        time.sleep(1)
        print('1) Fazer perguntas aos carregadores')
        time.sleep(1)
        print('2) Pular do leito e tentar fugir')
        time.sleep(1)
        print('3) Ficar quieto')
        time.sleep(1)
        indicador = int(input('\n'))
    if indicador == 1:
        interagircarregadores(indicador)
    print('Começo a conseguir identificar o que estou vendo.')
    time.sleep(3)
    print('Alguns tons de verde.')
    time.sleep(2)
    print('Sinto um ar florestal pelas minhas narinas.')
    time.sleep(2)
    print('E não é qualquer ar florestal, tem um leve frescor de eucalipto.')
    time.sleep(3)
    print('Estão me levando por uma trilha no meio de uma floresta de eucalipto.')
    time.sleep(3)
    print('Posso ouvir o som dos passos de dezenas de pessoas atrás de nós.')
    time.sleep(3)
    print('E se isso for uma seita e eu sou uma oferenda?')
    time.sleep(3)
    print('Começo finalmente a sentir o pavor.')
    time.sleep(2)
    print('Começo finalmente a sentir a adrenalina pelo meu corpo e um pouco de vida.')
    time.sleep(3)
    print("\n")
    time.sleep(1)
    print('Isso tudo faz sentido.')
    time.sleep(1)
    print('Me alimentaram e me hidrataram.')
    time.sleep(1)
    print('Uma oferenda precisa estar fresca, certo?')
    if save_game == 111:
        time.sleep(2)
        print('O único problema seria aquelas pessoas rindo naqueles momentos.')
        time.sleep(3)
        print('Não se ri de uma oferenda.')
        time.sleep(2)
        print('Uma oferenda é algo sério.')
    time.sleep(2)
    print('Talvez eu apenas possa descobrir perguntando.')
    time.sleep(2)
    print('O que devo fazer?')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    descobrirperguntando(indicador)
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('Preciso orquestrar meu plano de fuga.')
    time.sleep(2)
    print('Não estou amarrado no leito. ')
    time.sleep(2)
    print('Posso simplesmente me jogar no chão, me levantar e correr.')
    time.sleep(3)
    print('Porém não acho que eu iria longe.')
    time.sleep(2)
    print('Provavelmente seria pego antes de me levantar.')
    time.sleep(3)
    print('Eles provavelmente vão me abaixar em algum momento.')
    time.sleep(4)
    print('Talvez neste momento irei correr.')
    time.sleep(1)
    time.sleep(1)
    print('-----------------------------------------')
    time.sleep(1)
    print('Novo objetivo: orquestre um plano de fuga')
    time.sleep(1)
    print('-----------------------------------------')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('Olhando ao meu redor, ainda com a vista irritada, vejo que estamos caminhando realmente por uma trilha na mata.')
    time.sleep(7)
    print('O máximo que posso ver adiante é onde o terreno diminui seu nível, cerca de 20 metros direção sul, minha visão oeste está mais comprometida pelo excesso de luz, do outro lado vejo apenas verde.')
    time.sleep(9)
    print('Há um rio nesses arredores?')
    time.sleep(2)
    print('O ar é um pouco úmido.')
    time.sleep(2)
    print('Pela floresta de eucalipto faz sentido ter um rio próximo.')
    time.sleep(3)
    print('O plantio de uma árvore de eucalipto necessita de um solo mais úmido.')
    time.sleep(4)
    print('\n')
    time.sleep(1)
    print('Como muito provavelmente não faço algum exercício físico por um tempo, talvez nem minha coordenação esteja das melhores.')
    time.sleep(7)
    print('Ou simplesmente nem aguente correr tanto antes de passar um pouco mal.')
    time.sleep(5)
    print('\n')
    time.sleep(1)
    print('Qual caminho devo considerar?')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('1) Sul. O terreno diminui e não consigo ver adiante, mas é melhor do que ir para dentro da floresta.')
    time.sleep(1)
    print('2) Norte. Pela floresta, fica mais difícil de eles me perseguirem e já sei o que esperar (é uma floresta de eucaliptos, afinal... nada absurdo).')
    time.sleep(1)
    print("3) Oeste, em direção ao Sol. Prefiro seguir a trilha até a saída. Mesmo que me sujeite a mais riscos, o terreno não proverá surpresas.")
    time.sleep(1)
    indicador = int(input('\n')*1000)
    time.sleep(1)
    print('\n')
    time.sleep(1)
    if indicador == 1000:
        sentenca = 'sul. O terreno diminui e não consigo ver adiante, mas é melhor do que ir para dentro da floresta.'
    elif indicador == 2000:
        sentenca = 'norte, pela floresta, fica mais difícil de eles me perseguirem e já sei o que esperar (é uma floresta de eucaliptos, afinal... nada absurdo).'
    else:
        indicador = 3000
        sentenca = 'oeste, em direção ao Sol. Prefiro seguir a trilha até a saída. Mesmo que me sujeite a mais riscos, o terreno não proverá surpresas.'
    print('Acho que já sei minha direção... obviamente será', sentenca)
    time.sleep(6)
    print('\n')
    time.sleep(1)
    print('Estamos chegando numa espécie de altar de madeira.')
    time.sleep(3)
    print('Avisto uma pessoa sentada no chão com uns homens em volta.')
    time.sleep(3)
    print('Quando olho a primeira vez, não acredito em meus olhos.')
    time.sleep(3)
    print('Mas quando olho pela segunda vez, sei que é Randall.')
    time.sleep(3)
    print('Randall era um de meus únicos amigos.')
    time.sleep(2)
    print('Randall era basicamente invisível para sua família.')
    time.sleep(3)
    print('Era o único que não era casado, não tinha emprego fixo e vivia numa casinha simples num bairro ruim.')
    time.sleep(5)
    print('Randall possuía apenas as mesmas peças de roupa que eu: uma bermuda feita de material desconhecido e coloração amarelo-esverdeada.')
    time.sleep(5)
    print('Nem tinha reparado nisso antes.')
    time.sleep(2)
    print('\n')
    time.sleep(1)
    print('Os guardas me abaixam e me ordenam sentar ao lado de Randall.')
    time.sleep(3)
    if save_game == 122:
        print('Diferentemente de mim, Randall está com as mãos amarradas.')
        time.sleep(3)
    print('\n')
    time.sleep(1)
    print('⦁	Randall?')
    time.sleep(1)
    print('⦁	Como você sabe meu nome?- ele pergunta.')
    time.sleep(2)
    print('\n')
    time.sleep(1)
    print('De repente sinto uma leve perda de consciência, como se eu estivesse um pouco dopado ao invés de apenas enfraquecido.')
    time.sleep(6)
    print('Durou pequenos segundos, mas  acredito que seja lá qual substância esteja em nossos corpos, provavelmente também afetou nossa memória de curto e médio-prazo.')
    time.sleep(7)
    print('O problema é que conheço Randall há muito tempo, não faria sentido ele não se lembrar de mim.')
    time.sleep(6)
    print('\n')
    time.sleep(1)
    print('⦁	Não se lembra de mim?')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('⦁	Por que você está amarrado?')
    time.sleep(2)
    print('⦁	Fugir não é uma boa ideia- ele responde.')
    time.sleep(2)
    print('\n')
    time.sleep(1)
    print('Randall não estava com nenhuma marca de agressão física que consigo reparar.')
    time.sleep(4)
    print('Isso pelo menos me aliviava um pouco.')
    time.sleep(3)
    print('Os membros dessa seita, ou seja o que for, não parecem tão hostis e, de alguma forma, sinto que em algum momento fiz parte do que está acontecendo aqui.')
    time.sleep(7)
    print('\n')
    time.sleep(1)
    print('-----------------------------------------')
    time.sleep(1)
    print('Novo objetivo: sobreviva')
    time.sleep(1)
    print('-----------------------------------------')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    agoraeomomento(save_game, indicador)


     

def variacao1capitulo1henrique(indicador):
    if indicador == 11:
        print('⦁	OLÁ, ESTOU PRESO NESSE LUGAR! ALGUÉM PODE ME AJUDAR?')
        time.sleep(2)
        print('\n')
        time.sleep(2)
        print('Dessa vez pude compreender alguma coisa, pois escuto risos. É de mim que estão rindo?')
        time.sleep(3)
    print('A porta se abre.')
    time.sleep(1)
    if indicador == 12 or indicador == 11 or indicador == 41 or indicador == 42 or indicador == 43 or indicador == 44:
        print('De repente a sala toda se ilumina.')
        time.sleep(2)
        print('Continuo sem conseguir ver nada, a luz me cega mais que a escuridão.')
        time.sleep(3)
        print('A sensação é a de que sou um pirata sem tapa-olho que subiu da parte inferior e escura do navio para olhar o céu do meio-dia.')
        time.sleep(5)
        print('Reparo que estou amarrado a uma espécie de coluna.')
    else:
        print('Consigo sentir a luz atravessando minhas pálpebras, mesmo com os olhos fechados.')
        time.sleep(3)
        print('Se estivesse com eles abertos, provavelmente estaria vendo menos do que veria na escuridão, já que meus olhos não estariam acostumados.')
        time.sleep(5)
        print('Percebo que meu corpo a uma espécie de coluna também, ao invés de apenas minhas mãos.')
        time.sleep(1)
    time.sleep(3)
    print('Pela reverberação do som da porta se abrindo, posso sentir que o local deve ser um pouco apertado e com pouca ventilação pela sensação térmica.')
    time.sleep(5)
    if indicador == 3:
        print('Recebo um "splash" de água gelada na cara. Minha reação natural é abrir os olhos e inspirar num ato momentâneo de adrenalina, pelo susto.')
        time.sleep(5)
    print('Alguém me desamarra da coluna.')
    time.sleep(3)
    return

def agoraeomomento(save_game, indicador):
    print('Agora é o momento...')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('1) Aproveitar a distração dos guardas com a preparação do ritual e seguir meu plano de fuga sozinho.')
    time.sleep(1)
    print('2) Convencer Randall a fugir, e então seguimos meu plano.')
    time.sleep(1)
    print('3) Ficar com Randall.')
    time.sleep(1)
    save_game += indicador
    indicador = int(input('\n'))
    indicador = indicador*10000
    save_game += indicador
    #print(save_game)
    if save_game == 11122:
        print('"Com as minhas mãos livres, já que eu estava apenas fingindo que ainda estava amarrado, sou capaz de me levantar rapidamente e correr em direção sul, mesmo sem saber o que me espera. Após chegar na parte onde o terreno desce, percebo que cometi um erro: há apenas água, muita água. Olho para trás e nem consigo reagir enquanto recebo uma flechada e tudo começa a ficar branco...."')
        time.sleep(10)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
        agoraeomomento()
    elif save_game == 11111 or save_game == 12111 or save_game == 13111 or save_game == 11112 or save_game == 12112 or save_game == 13112 or save_game == 11103 or save_game == 12103 or save_game == 13103:
        print('"Apesar de estar com as mãos ainda amarradas, sou capaz de me levantar com cuidado e começar a correr, mas um dos guardas percebe minha reação e me impede de seguir qualquer caminho... recebo uma seringa no pescoço e tudo começa a ficar branco..."')
        time.sleep(8)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
        agoraeomomento()
    elif save_game == 12122:
        print('"Com as minhas mãos livres, já que eu estava apenas fingindo que ainda estava amarrado, sou capaz de me levantar rapidamente e correr em direção norte, mesmo sem saber o que me espera. Após adentrar na floresta, resolvo apenas continuar correndo sem olhar para trás."')
        time.sleep(8)
        print('\n')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('"Começo a avistar o fim da floresta de eucaliptos e percebo que estou numa vila e acabei de sair em outra extremidade dela. Então ao invés de fugir, entrei mais fundo onde estava preso... Nem consigo reagir enquanto recebo uma flechada de alguém da vila e tudo começa a ficar branco...."')
        time.sleep(10)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
        agoraeomomento()
    elif save_game == 13122:
        print('"Com as minhas mãos livres, já que eu estava apenas fingindo que ainda estava amarrado, sou capaz de me levantar rapidamente e correr em direção oeste, sem nem ver direito onde estou indo. Só percebo uma laçada em meu corpo e desabo no chão. O guarda então me aplica uma seringa no pescoço e tudo fica branco..." ')
        time.sleep(10)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
        agoraeomomento()
    elif save_game == 21111 or save_game == 21112 or save_game == 21103:
        print('"Eu me aproximo de Randall e tento convencer ele a tentar fugir mais uma vez, já que agora somos dois. Ele me pergunta qual o meu plano e eu explico. Ele apenas me responde que é um plano idiota, e então resolvo prosseguir sozinho."')
        time.sleep(8)
        print('\n')
        time.sleep(1)
        print('"Apesar de estar com as mãos ainda amarradas, sou capaz de me levantar com cuidado e começar a correr, mas um dos guardas percebe minha reação e me impede de seguir qualquer caminho... recebo uma seringa no pescoço e tudo começa a ficar branco..."')
        time.sleep(8)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
        agoraeomomento()
    elif save_game == 21122:
        print('"Eu me aproximo de Randall e tento convencer ele a tentar fugir mais uma vez, já que agora somos dois. Ele me pergunta qual o meu plano e eu explico. Ele apenas me responde que é um plano idiota, e então resolvo prosseguir sozinho."')
        time.sleep(8)
        print('\n')
        time.sleep(1)
        print('"Com as minhas mãos livres, já que eu estava apenas fingindo que ainda estava amarrado, sou capaz de me levantar rapidamente e correr em direção sul, mesmo sem saber o que me espera. Após chegar na parte onde o terreno desce, percebo que cometi um erro: há apenas água, muita água. Olho para trás e nem consigo reagir enquanto recebo uma flechada e tudo começa a ficar branco...."')
        time.sleep(10)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
        agoraeomomento()
    elif save_game == 22111 or save_game == 21112 or save_game == 21103:
        print('"Eu me aproximo de Randall e tento convencer ele a tentar fugir mais uma vez, já que agora somos dois. Ele me pergunta qual o meu plano e eu explico. Ele apenas me responde que é um plano idiota, e então resolvo prosseguir sozinho."')
        time.sleep(8)
        print('\n')
        time.sleep(1)
        print('"Apesar de estar com as mãos ainda amarradas, sou capaz de me levantar com cuidado e começar a correr, mas um dos guardas percebe minha reação e me impede de seguir qualquer caminho... recebo uma seringa no pescoço e tudo começa a ficar branco..."')
        time.sleep(8)
        gameover()
        time.sleep(1)
        input('Tecle enter para retornar ao checkpoint')
    elif save_game == 22122:
        print('"Eu me aproximo de Randall e tento convencer ele a tentar fugir mais uma vez, já que agora somos dois. Ele me pergunta qual o meu plano e eu explico. Ele apenas me responde que é um plano idiota, e então resolvo prosseguir sozinho."')
        time.sleep(8)
        print('\n')
        time.sleep(1)
        print('"Com as minhas mãos livres, já que eu estava apenas fingindo que ainda estava amarrado, sou capaz de me levantar rapidamente e correr em direção norte, mesmo sem saber o que me espera. Após adentrar na floresta, resolvo apenas continuar correndo sem olhar para trás."')
        time.sleep(8)
        print('\n')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('"Começo a avistar o fim da floresta de eucaliptos e percebo que estou numa vila e acabei de sair em outra extremidade dela. Então ao invés de fugir, entrei mais fundo onde estava preso... Nem consigo reagir enquanto recebo uma flechada de alguém da vila e tudo começa a ficar branco...."')
        time.sleep(10)
        gameover()
    else:
        prologo()

def interagirrelogio(indicador, sentenca):
    slowprint('\nO que fazer?\n1) Examinar visor\n2) Examinar botões\n3) Jogar para longe\n')
    indicador = int(input(''))
    if indicador == 1:
        print('"00:00 3"')
        slowprint('\nO horário parece estar travado em 00:00. Não sei o que o 3 significado.')
        interagirrelogio(indicador, sentenca)
    elif indicador == 2:
        print('"Mode\nValue\nOverpower"\n')
        slowprint('Começo a apertar os botões para ver o que fazer. Quando aperto o botão value, a voz robótica alterna entre "1 point" e "2 points". Quando aperto o botão value a voz alterna entre "strenght", "agility" e "luck". Quando aperto o botão de overpower, um som de confirmação acontece e escuto a voz robótica novamente.\n')
        print('"1 ponto adicionado ao atributo força, você ainda tem mais 1 ponto".')
        time.sleep(4)
        print('\n')
        return
    else:
        indicador = 3
        nadaacontece()
        interagirrelogio()
        
def testestrength(indicador):
    indicador = int(input(''))
    if indicador == 1:
        slowprint('Pego um pouco de impulso e pulo com todas as minhas forças. Caio em cima da plataforma, mas escorrego. Consigo me agarrar na extremidade e subir devolta. Uma porta se abre a minha frente. Pulo novamente e caio dentro de uma nova sala.')
        return
    else:
        slowprint('Tento me esquivar indo pelas beiradas da sala até o outro lado. Mas percebo que não tenho habilidade o suficiente e resolvo voltar. Acabo errando o pé e caindo na água embaixo. Reparo que a água começa a corroer o meu compor, assim como corrói minhas consciência e tudo fica branco...')
        gameover()
        input('Tecle enter para voltar ao checkpoint')
        testestrength(indicador)

def testeagility(indicador):
    indicador = int(input(''))
    if indicador == 1:
        slowprint('Pego impulso e me jogo para a plataforma... apenas para perceber que não cheguei nem perto dela e cair no líquido corrosivo. Tudo fica branco...')
        gameover()
        input('Tecle enter para continuar')
        testeagility
    else:
        slowprint('Resolvo me esquivar pelas beiradas da sala. Consigo me equilibrar pelos detalhes da parade até chegar do outro lado. A porta se abre e entro dentro da nova sala.')
        return

def testeluck():
    slowprint('E então sem nem pensar direito resolvo agir... Meu pé escorrega e acabo caindo no líquido corrosivo. Apenas para perceber que é água. Nado normalmente até o outro lado e subo numa corda que também está ali, convenientemente..')
    return


def capitulo1iglesias(indicador, save_game2, sentenca):
    slowprint('Eu abro os olhos e percebo que estou atrasado. Já são 8:55 e preciso estar no serviço as 9. Não que eu goste necessariamente da atividade de pintar muros e prédios públicos, muito menos de continuar lá até as 16:00 quando o Sol já está estralando nas costas.')
    print('\n')
    slowprint('Levanto rapidamente, pego meu relógio, visto as pressas minha roupa separada na mesinha do lado da cama. Corro para a porta. Ainda estava escuro. Estranho. Eclipse? Deve ser impressão.')
    print('\n')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    slowprint('Nem me preocupo em abrir as cortinas da sala para verificar. Eu estava descansado, certeza que eram 9 horas. Quando não durmo direito fico destruído. Passo pelo corredor que da acesso à cozinha. Abro a geladeira e vejo.')
    slowprint('1) Leite\n2) Suco de laranja\n3) Bolo')
    while indicador != 0:
        indicador = int(input('Dica: insira o número da escolha desejada e tecle enter\n'))
        if indicador == 1:
            slowprint('Pego um copo e encho de leite gelado, bebo rapidamente queimando a garganta. Corro no banheiro checar o cabelo, arrumo com as mãos, e saio em disparada pela porta da sala.Sinto uma pancada e tudo fica claro.')
            save_game2 = indicador
            indicador = 0
        elif indicador == 2:
            slowprint('Pego um copo e encho de suco de laranja, bebo rapidamente queimando a garganta. Dou uma engasgada, acho que tinha uma mosca. Corro no banheiro checar o cabelo, arrumo com as mãos, e saio em disparada pela porta da sala.Sinto uma pancada e tudo fica claro.')
            save_game2 = indicador
            indicador = 0
        else:
            slowprint('Pego uma fatia de bolo e na pressa acabo derrubando no chão...')
    print('-----------------------------------------------------------')
    slowprint('"Olá, seja muito bem-vindo ao exame".\nOuço uma voz ao longe.\nMe levanto, extremamente descordenado e desorientado. Com a vista toda embaçada, sem entender o que estou vendo.\nOnde estou?\n')
    slowprint('1) Balada\n2) Cativeiro\n3) Trote\n4) ???\n')
    indicador = int(input(''))
    if indicador == 1:
        print('\n')
        slowprint('Será que bebi demais?')
    elif indicador == 2:
        print('\n')
        slowprint('Será que fui sequestrado?')
    else: 
        indicador = 3
        print('\n')
        slowprint('Será que isso é alguma brincadeira estúpida?')
    print('\n')
    save_game2 += (indicador*10)
    slowprint('"Por favor se dirija a uma das portas".\nQue voz é essa?\n')
    slowprint('1) Alto-falante?\n2) Alguém ao longe\n3) Minha imaginação?\n')
    indicador = int(input(''))
    if indicador == 1:
        slowprint('\nSerá que é um alto-falante?')
    elif indicador == 2:
        slowprint('\nSerá que tem mais alguém aqui?')
    else:
        slowprint('\nSó posso estar delirando.')
    print('\n')
    slowprint('Começo a fazer sentido do que vejo.\nEstou num salão com cerca de 30 metros quadrados, a iluminação não é boa, mas consigo ver os cantos que possuem luminárias de baixa qualidade.\nEm cada canto do salão parece ter uma porta. Tem uma a minha frente, uma atrás e uma em cada lado.\n"Senhor, se dirija a uma das portas imediatamente".\nO som da voz reverbera, mas consigo identificar que vem da minha frente. Olho para o alto e consigo ver o pequeno alto-falante.\n--\nO que devo fazer?\n')
    print('-----------------------')
    slowprint('1) Tentar me comunicar\n2) Me dirigir a uma das portas\n3) Procurar uma saída alternativa\n4) Procurar algo que possa usar como arma\n')
    primeirainteracaoIglesias(indicador, sentenca)
    slowprint('Hmmmmm.... essa porta parece diferente das outras... há um visor nela. Eu me aproximo para ler o que está escrito, e é:\n"Digite seu nome:"\nHá um teclado embaixo para digitar.')
    sentenca = str(input('Dica: digite seu nome e tecle enter '))
    slowprint('\nUma voz robótica começa a conversar comigo.')
    print('Nome: ', sentenca)
    print('Sobrenome: Iglesias')
    slowprint('\n"Iglesias. Por favor, entre..."\nA porta a minha frente abre verticalmente. Sem muitas opções, resolvo prosseguir por agora..."')
    slowprint('Entro numa sala apertada. A minha frente há uma porta metálica. A meu lado esquerdo há uma espécie de cama metálica, não há nada em cima exceto um aparelho. Vejo o que parece ser um dispositivo com um visor. Como um relógio digital de mesa. Seu formato é retangular com as bordas arredondadas. Pego para ver e vejo que ele tem um botão na parte superior e três botões atrás dele.')
    interagirrelogio(indicador, sentenca)
    slowprint('Sinto uma leve tontura.')
    slowprint('Sento no chão para ver se me recupero.\nO equipamento apita e começa a mostrar uma contagem no visor:\n"30:00"\n ouço um bip.\nCom certeza é timer para alguma coisa.\nAguardo um momento e levanto para decidir o que vou fazer.\n"29:00" ouço um bip.\n')
    slowprint('1) Tentar abrir a porta a minha frente\n2) Arremessar o equipamento na porta\n')
    indicador = int(input(''))
    if indicador == 2:
        slowprint('Só pode ser uma bomba. Arremesso o equipamento na porta, mas no momento que ia me virar e correr, percebo que joguei ele com tanta força que a maçaneta da porta quebrou.\nComo isso aconteceu?\nOuço um bip.\n"28:00"\n')
        equipamentovsporta(indicador)
    slowprint('O que me resta é tentar abrir a porta da frente... mas agora sei que consigo por força bruta.')
    slowprint('\nCom uma facilidade inacreditável, derrubo a porta a minha frente\nAcho que devo upar mais algum atributo nesse aparelho, seja lá o que for.\n')
    slowprint('O que devo upar?\n1) Strength\n2) Agility \n3) Luck')
    indicador = int(input('\n'))
    slowprint('E no momento que vou pisar na nova sala, percebo que não há chão. As luzes acendem. A sala está inundada de algum líquido. Não consigo ver a profundidade, mas começa há 5 metros abaixo da altura da porta. Há um plataforma no meio da sala, a 5 metros de onde estou.\nO que devo fazer?\n1) Pular para a plataforma\n2) Me esquivar pelas beiradas até o outro lado\n')
    if indicador == 1:
        testestrength(indicador)
    elif indicador == 2:
        testeagility(indicador)
    else:
        indicador = 3
        testeluck()
    save_game2 += (indicador*100)
    slowprint('\n"Olá, sou eu de novo, aqui do alto falante".\nOlho para cima e encontro um auto-falante na parte superior da parede a minha frente. A sala parece ser do mesmo tamanho que a que encontrei o equipamento de status.\n"Esse é seu último teste. Se você passar, pode ir embora com o aparelho que em breve lhe chamaremos para trabalhar conosco. Os benefícios incluem Plano Dental. Se não passar, será executado."')
    print('\n')
    time.sleep(1)
    print('"Boa sorte!"')
    slowprint('Que tipo de tortura terei e passar agora? Se eu não meditasse todos os dias e não fosse extremamente estoico como sou, estaria em pânico agora.')
    slowprint('\n"Vamos lá"\nO meio do chão se abre e sai uma mesa com três botões. Em cima, horizontalmente, há um visor.')
    primeirapergunta(indicador, save_game2)
    segundapergunta(indicador, save_game2)
    terceirapergunta(indicador, save_game2)
    slowprint('"E temos um vencedor!!""\n Um rádio cai na minha cabeça, dessa vez. Fiquei com um calo. Começou a tocar um música animada que nunca ouvi na vida, a porta a minha frente abriu e eu avistei avistei um robô jogando confete pela sala...\n')
    print('---------')
    time.sleep(1)
    print('Continua')
    time.sleep(1)
    print('---------')
    input('Tecle enter para reiniciar')
    inicio(save_game, indicador, sentenca)


def primeirapergunta(indicador, save_game2):
    slowprint('Olho para o visor e leio:\n" O que você bebeu antes de vir para cá?"\n1) Suco\n2) Leite\n')
    indicador = int(input(''))
    if (save_game2%2) == 0:
        if indicador == 1:
            slowprint('Resposta correta.')
            return
        if indicador == 2:
            slowprint('Sinto um campo de energia começar a se formar em volta de mim. O desconforto e os espasmos aumentam até que tudo fica branco...')
            gameover()
            print('Tecle enter para retornar ao checkpoint')
            input('')
            primeirapergunta(indicador, save_game2)
    else:
        if indicador ==1:
            slowprint('Sinto um campo de energia começar a se formar em volta de mim. O desconforto e os espasmos aumentam até que tudo fica branco...')
            gameover()
            print('Tecle enter para retornar ao checkpoint')
            input('')
            primeirapergunta(indicador, save_game2)
        else: 
            slowprint('Resposta correta.')
            return

def segundapergunta(indicador, save_game2):
    slowprint('Olho para o visor e leio:\n" Qual foi seu último emprego?"\n1) Pintor\n2) Auxiliar de construção\n')
    indicador = int(input(''))
    if indicador == 1:
        slowprint('"A sua resposta está...............e.................................xata!"')
        return
    else:
        slowprint('Sinto um campo de energia começar a se formar em volta de mim. O desconforto e os espasmos aumentam até que tudo fica branco...')
        gameover()
        print('Tecle enter para retornar ao checkpoint')
        input('')
        segundapergunta(indicador, save_game2)

def terceirapergunta(horario):
    slowprint('Olho para o visor e leio:\n" Que hora você acordou hoje?"\n')
    slowprint('Um teclado cai na minha cabeça... sem fio... eita tecnologia...')
    horario = str(input('Insira horário: (formato 00:00)'))
    if horario == '08:55':
        slowprint('"A sua resposta está e.................................xata!"')
        return
    else:
        slowprint('"A sua resposta está e...........................rrada!"')
        slowprint('Recebo um choque tão forte do teclado que não tenho tempo de reagir, tudo apenas fica branco...')
        gameover()
        input('Tecle enter para reiniciar do checkpoint')
        terceirapergunta()
        
def primeirainteracaoIglesias(indicador, sentenca):
    while indicador != 21:
        indicador = int(input(''))
        if indicador == 1:
            print('⦁	',grito())
            nadaacontece()
            time.sleep(1)
            print('\n')
            slowprint('Talvez devo tentar outra coisa...')
            print('--------------------------')
            print('\n')
            time.sleep(1)
            print('1) Tentar me comunicar\n2) Me dirigir a uma das portas\n3) Procurar uma saída alternativa\n4) Procurar algo que possa usar como arma\n')
        elif indicador == 2:
            porta2(indicador)
            return
        elif indicador == 3:
            slowprint('Olho para cima e vejo que o telhado é muito alto... então nada de fugir por tubulação. Não parece ter nada que me leve abaixo do solo também, não consigo ver direito. Talvez deva dar uma olhada nas portas para ver se acho algo no meio do caminho... só espero que não tenha nenhuma armadilha.' )
        else:
            slowprint('Talvez eu deva também checar as portas enquanto busco, já que o espaço é grande demais para eu achar algo dessa forma...')
    

def porta2(indicador):
    print('Qual das portas devo testar?')
    print('\n')
    slowprint('1) Porta norte\n2) Porta sul\n3) Porta leste\n4) Porta oeste\n')  
    indicador = int(input(''))  
    if indicador == 1:
        indicador = 21
        return
    else:
        slowprint('Dirijo-me a porta. O meio do caminho possui apenas chão sólido, nada demais no chão. Chego mais próximo da porta e não vejo nada demais... é uma porta sem fechadura, inclusive bem presa ao chão. Não vejo possibilidade de abrir ou arrombar isso... parece ser feita de um material extremamente resistente também...')
        porta2(indicador)     

def equipamentovsporta(indicador):
    slowprint('1) Examinar equipamento\n2) Examinar porta\n3) Correr \n')
    indicador = int(input(''))
    if indicador == 1:
        slowprint('O equipamento está intacto.\n')
        equipamentovsporta(indicador)
    elif indicador == 2:
        slowprint('A porta parece sólida. Sem a maçaneta não sei como vou passar...\n')
        equipamentovsporta()
    else:
        indicador = 3
        slowprint('Resolvo não correr o risco e corro em disparada para fora da salinha. Para minha surpresa, outra porta sólida desce verticalmente, me impedindo de voltar.')
        slowprint('Dou um soco na porta por frustração, e magicalmente ele amassa. Resolvo testar se consigo fazer novamente e derrubo a porta.')
        slowprint('Corro para fora e aguardo alguns minutos...\n')
        print('...')
        time.sleep(1)
        print('\n')
        nadaacontece()
        return

def voceacreditaemterragratia(indicador):
    slowprint('Abro meus olhos e percebo que... aquilo tudo foi um sonho.\nNunca vivenciei Terragratia e provavelmente nunca existiu.\n...\nVocê já ouviu falar de Terragratia?\n')
    print('--------------------------------------------------')
    time.sleep(1)
    print('Objetivo: convença-me da existência de Terragratia.\n')
    time.sleep(1)
    print('--------------------------------------------------')
    time.sleep(1)
    slowprint('1) Já sim... conheço algumas histórias\n2) Nunca... mas vou pesquisar sobre\n3) O que é Terragratia?\n')
    indicador = int(input(''))
    if indicador == 1:
        slowprint('Hmmmmmm.... interessante, interessante...')
    elif indicador == 2:
        slowprint('Bom, é uma pena... quando estiver pronto podemos conversar...')
        gameover()
        input('Tecle enter para retornar ao checkpoint')
        voceacreditaemterragratia(indicador)
    else:
        slowprint('Haha... ficção... apenas ficção...')
        gameover()
        input('Tecle enter para retornar ao checkpoint')
        voceacreditaemterragratia(indicador)
    qualhistoriacontar(indicador)
    slowprint('Uau.... que estranho! Isso foi exatamente o que sonhei... um dos sonhos que tive essa noite. Acho que vou realmente considerar a existência de Terragratia. Obrigado pela história!')
    time.sleep(1)
    input('Tecle enter para reiniciar o jogo')
    inicio(save_game, indicador, sentenca)

def qualhistoriacontar(indicador):
    slowprint('Se importa em contar uma dessas histórias?\n1) Era uma vez um cachorro chamado Bob\n2) Era uma vez um ex-criminoso chamado Henrique\n')
    indicador = int(input(''))
    if indicador == 1:
        slowprint('Bob? haha existe um cachorro chamado Bob em toda ficção...')
        gameover()
        input('Tecle enter para retornar ao checkpoint')
        qualhistoriacontar(indicador)
    else:
        historiahenrique(indicador)

def historiahenrique(indicador):
    print('---------------------------------------------------')
    time.sleep(1)
    print('Objetivo: relembre detalhes da história de Henrique')
    time.sleep(1)
    print('---------------------------------------------------')
    time.sleep(1)
    indicador = 0
    while indicador != 1:
        indicador = int(input(''))
        slowprint('Tudo começou quando\n1) Ele foi sequestrado\n2) Ele se perdeu na mata\n3) Foi escolhido pelos deuses')
        if indicador == 2:
            slowprint('Se perdeu na mata? Só pode estar brincando... já ouvi diversas versões dessa história, e cada um me inventa uma nova. Você está desperdiçando meu tempo.')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
        elif indicador == 3:
            slowprint('Por favor... quero histórias realistas, assim fica difícil acreditar em vocês...')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
    slowprint('Hmmmmmmmm.... continue.')
    indicador = 0
    while indicador != 1:
        slowprint('\n1) E ele foi parar numa vila longe da civilização, localizada numa ilha\n2) E ele foi parar numa comunidade que morava nave espacial\n3) E ele foi parar numa vila que ficava no meio de uma floresta\n')
        indicador = int(input(''))
        if indicador == 2:
            slowprint('Ah sim, claro, naves espaciais. Você parece um conspiracionista.')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
        elif indicador == 3:
            slowprint('Essa parece uma história que já ouvi, mas menos precisa... acho que vou perguntar para outra pessoa com mais contato.')
            gameover()
            input('Tecle enter para retroceder ao checkpoint')
    slowprint('Hmmmmmmm... eu sonhei com uma ilha, será que é um sinal? rs. Continue. Como ele escapou?')
    indicador = 0
    while indicador != 3:
        slowprint('\n1) Roubou um bote\n2) Escapou disfarçado de motorista de barco\n3) Ele ficou lá... era onde ele pertencia')
        indicador  = int(input(''))
        if indicador == 1:
            slowprint('Ele roubou um bote e escapou de uma ilha longe da civilização? Essa foi boa.')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
        elif indicador == 2:
            slowprint('Parece mais inteligente essa... mas motorista mesmo parece improvável... não acredito ser possível.')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
    slowprint('Ele ficou? Ah... que coincidência... o que sonhei foi assim. Ele encontrou alguém conhecido, lá? Se encontrou, quem?')
    indicador = 0
    while indicador != 2:
        slowprint('1) Não conhecia ninguém, mas fez várias amizades...\n2) Reconheceu um amigo de infância')
        indicador = int(input(''))
        if indicador == 1:
            slowprint('Ah sim... é diferente do que sonhei. Uma pena, se você tivesse acertado mais alguma coisa eu passaria e acreditar na magia de Terragratia...')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
    slowprint('É mesmo? E como era o nome dele?')
    indicador = 0
    while indicador != 3:
        slowprint('1) Roberto\n2) Lucas\n3) Chris\n4) Randall\n')
        indicador = int(input(''))
        if indicador != 3:
            slowprint('Ah sim... se você tivesse acertado o nome da pessoa que apareceu no meu sonho, eu acreditaria em você')
            gameover()
            input('Tecle enter para retornar ao checkpoint')
    return

def historiaiglesias(indicador):
    return

save_game = 0
save_game2 = 0
indicador = 0
sentenca = 'a'
inicio(save_game, indicador, sentenca)