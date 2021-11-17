import random
import time

def inicio(save_game):
    print('Bem-vindo a Terragratia.')
    time.sleep(1)
    load_game = str(input('Deseja carregar um jogo salvo? s/n\n'))
    if load_game in ['s']:
        save_game = int(input('Insira o código de save_game: '))
    elif load_game in ['n']:
        introducao()
    else:
        inicio(save_game)
        
def introducao():
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
        capitulo1_henrique()

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
    indicador = 300
    while indicador != 2:
        indicador = int(input('\n'))
        if indicador == 1:
            indicador = 21
            print('Tento me soltar do pilar, mas percebo que não tenho forças o suficiente.')
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

def capitulo1_henrique():
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
    # or indicador == 12 or indicador == 3 or indicador == 41 or indicador == 42 or indicador == 43 or indicador == 44:
    time.sleep(3)
    print(indicador)
    time.sleep(2)
    print('Não sei o que estão falando.')
    time.sleep(2)
    print('Não sei o que estão falando.')
    
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

save_game = 0
inicio(save_game)