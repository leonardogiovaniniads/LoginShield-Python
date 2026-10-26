from datetime import datetime
print('============================================\nLoginShield — Analisador de Logins Suspeitos\n============================================')
nome = str(input('Digite o nome do usuario: ')).lower().strip()
pais = str(input('De qual país esta sendo realizado o acesso?: ')).lower().strip()
hora = input('Qual o horário do acesso? (HH:MM): ')
horario = datetime.strptime(hora, '%H:%M')
tentativas = int(input('Quantas tentativas de senha incorreta ocorream?: '))
dispositivo = str(input('O dispositivo utilizado é conhecido? (Sim/Não): ')).lower().strip()
pontos = 0
print('============================================\nRELATÓRIO DE SEGURANÇA\n============================================\nUsuario:{}'.format(nome))
if pais != 'brasil':
    pontos += 30
    print('Acesso internacional: +30 pontos')
if 0 <= horario.hour < 6:
    pontos += 15
    print('Horário suspeito: +15 pontos')
if tentativas >= 3:
    pontos += 25
    print('Tentativas incorretas: +25 pontos')
if dispositivo in ('nao', 'não'):
    pontos += 30
    print('Despositivo desconhecido: +30 pontos')
print('Pontuaçao total {}/100 '.format(pontos))
if pontos >=60:
    print('\033[31mCLASSIFICAÇAO: RISCO ALTO\033[m')
    print('\033[33mALERTA: Verificação adicional recomendada!\033[m')
elif pontos >=25:
    print('\033[33mCLASSIFICAÇAO: RISCO MEDIO\033[m')
else:
    print('\033[32mCLASSIFICAÇAO: RISCO BAIXO\033[m')





