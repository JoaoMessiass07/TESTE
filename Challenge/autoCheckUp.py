# diagnostico do problema do veiculo
import os
import datetime
import time
os.system("cls")

# --------------------------------------------------------------------------------
ar_Condicionado = 150
amortecedores = 500
pastilhas_Freios = 110
pneus = 200
suspensao = 350
direcao = 800
cambagem = 250
alinhamento_Direcao = 150
diagnostico = "Falha na valvula X no MOTOR"
opcao = "s"
# ------------------------------------------------------------------------------------

centros_Auto_perto_Residencia = ["AV CRUZEIRO DO SUL", "AV RIO BRANCO", "R FRANÇA PINTO", "R TIJUCO PRETO"]

print("""============================ Bem Vindos ao diagnostico AutoCheckUp ================================""")
print("Para começar por favor nos informe seus dados pessoais: ")
nome_Cliente = input("nome: ")
telefone_Cliente = int(input("telefone: "))
cpf_Cliente = int(input("cpf: "))
cep = int(input("CEP (digite somente os números): "))
while opcao == 'S' or opcao == 's':
    os.system("cls")
    print("""Agora escolha uma das opções abaixo:
        1 - Cadastrar Veiculo
        2 - Diagnostico do Veiculo
        3 - Orçamentos
        4 - Centros Automotivos
        5 - Consultar Diagnosticos 
        6 - Agendamento de Reparo
        7 - Finalizar Programa
    """)
    opcao = int(input("Escolha uma das opções para prosseguir: "))
    if opcao < 1 or opcao > 7:
        os.system("cls")
        print(f"ERRO !!! Opção {opcao} invalida, por favor digite uma opção válida")
        print("""Agora escolha uma das opções abaixo:
        1 - Cadastrar Veiculo
        2 - Diagnostico do Veiculo
        3 - Orçamentos
        4 - Centros Automotivos
        5 - Consultar Diagnosticos 
        6 - Agendamento de Reparo
        7 - Finalizar Programa
    """)
        opcao = int(input("Escolha uma das opções para prosseguir: "))

    anoAtual = datetime.date.today().year

    match opcao:
        # OPÇÃO 1 - CADASTRAR VEICULO
        case 1:
            print("\n------------- CADASTRANDO VEÍCULO -------------")
            modeloVeiculo = str(input("modelo: "))
            marcaVeiculo = str(input("marca: "))
            anoVeiculo = int(input("ano: "))
            while anoVeiculo > anoAtual:
                print("ano do carro não existe")
                anoVeiculo = int(input("ano: "))
            quilometragem = float(input("quilometragem: "))
            if quilometragem <= 0:
                print(f"consumo invalido: {quilometragem}")
            corVeiculo = str(input("Cor: "))
            transmissao = str(input("Transmissão: "))
            placaVeiculo = str(input("Placa: "))
            print(f"""
            ------------- CARRO CADASTRADO COM SUCESSO !!!! -------------
                modelo {modeloVeiculo}
                marca {marcaVeiculo}, 
                ano de fabricação {anoVeiculo} 
                quilometragem {quilometragem}
                cor {corVeiculo}
                transmissão {transmissao}
                placa {placaVeiculo}
            """)
            opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))

        # OPÇÃO 2 - DIAGNOSTICO DO VEICULO
        case 2:
            print("Diagnostico do Veiculo")
            print("\n------------- Relatando O Problema -------------")
            relato = str(input("Por favor relate o problema com seu veiculo:\n "))
            print(f"registrando o seu problema ({relato})...")
            time.sleep(2)
            print("Problema registrado\n")
            os.system("cls")
            print("Realizando Diagnostico...\n")
            time.sleep(1)
            print(f"""
                            | Diagnostico realizado |
                    ----------------------------------------
                    Segunda a análise feita, foi constatado
                    que o problema pode ser:\n
                    - {diagnostico}
                    """)
            opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))

        # OPÇÃO 3 - ORÇAMENTOS
        case 3:
            print(f"""ORÇAMENTOS DOS SERVIÇOS DISPONÍVEIS: 
                1 - Troca e higienização do AR CONDICIONADO  --> R$ {ar_Condicionado:7.2f}
                2 - Troca dos AMORTECEDORES  ------------------> R$ {amortecedores:7.2f} 
                3 - Troca das PASTILHAS DE FREIOS  ------------> R$ {pastilhas_Freios:7.2f} 
                4 - Troca dos PNEUS  --------------------------> R$ {pneus:7.2f} 
                5 - Troca da SUSPENSÃO  -----------------------> R$ {suspensao:7.2f}
                6 - Troca da DIREÇÃO  -------------------------> R$ {direcao:7.2f} 
                7 - Troca da CAMBAGEM / CASTER  ---------------> R$ {cambagem:7.2f} 
                8 - Ajuste do ALINHAMENTO DA DIREÇÃO ----------> R$ {alinhamento_Direcao:7.2f}""")
            escolha_servico = int(input(f"O(A) Sr(Sra) deseja solicitar algum dos serviços disponíveis: [1] SIM ou [2] Não:   "))
            while escolha_servico < 1 or escolha_servico > 2:
                os.system("cls")
                print(f"ERRO OPÇÃO {escolha_servico} INVÁLIDA")
                print(f"""ORÇAMENTOS DOS SERVIÇOS DISPONÍVEIS: 
                    1 - Troca e higienização do AR CONDICIONADO  --> R$ {ar_Condicionado:7.2f}
                    2 - Troca dos AMORTECEDORES  ------------------> R$ {amortecedores:7.2f} 
                    3 - Troca das PASTILHAS DE FREIOS  ------------> R$ {pastilhas_Freios:7.2f} 
                    4 - Troca dos PNEUS  --------------------------> R$ {pneus:7.2f} 
                    5 - Troca da SUSPENSÃO  -----------------------> R$ {suspensao:7.2f}
                    6 - Troca da DIREÇÃO  -------------------------> R$ {direcao:7.2f} 
                    7 - Troca da CAMBAGEM / CASTER  ---------------> R$ {cambagem:7.2f} 
                    8 - Ajuste do ALINHAMENTO DA DIREÇÃO ----------> R$ {alinhamento_Direcao:7.2f}""")
                escolha_servico = int(input(f"O(A) Sr(Sra) deseja solicitar algum dos serviços disponíveis: [1] SIM ou [2] Não:   "))

            if escolha_servico == 1:
                servicos = int(input("Qual / Quais do serviços o(a) Sr(Sra) gostaria de escolher: "))
                while servicos < 1 or servicos > 8:
                    os.system("cls")
                    print(f"""ORÇAMENTOS DOS SERVIÇOS DISPONÍVEIS: 
                    1 - Troca e higienização do AR CONDICIONADO  --> R$ {ar_Condicionado:7.2f}
                    2 - Troca dos AMORTECEDORES  ------------------> R$ {amortecedores:7.2f} 
                    3 - Troca das PASTILHAS DE FREIOS  ------------> R$ {pastilhas_Freios:7.2f} 
                    4 - Troca dos PNEUS  --------------------------> R$ {pneus:7.2f} 
                    5 - Troca da SUSPENSÃO  -----------------------> R$ {suspensao:7.2f}
                    6 - Troca da DIREÇÃO  -------------------------> R$ {direcao:7.2f} 
                    7 - Troca da CAMBAGEM / CASTER  ---------------> R$ {cambagem:7.2f} 
                    8 - Ajuste do ALINHAMENTO DA DIREÇÃO ----------> R$ {alinhamento_Direcao:7.2f}""")
                    servicos = int(input("Qual / Quais do serviços o(a) Sr(Sra) gostaria de escolher: "))

                match servicos:
                    case 1:
                        # os.system("cls")
                        print(f"Você escolheu a opção 1 - Troca e higienização do AR CONDICIONADO  --> R$ {ar_Condicionado:7.2f}")
                        # mais_servicos = int(input("Gostaria de adicionar outro serviço: [1]- Sim ou [2]- Não:  "))
                        # while mais_servicos == 1:
                        #     print(f"""ORÇAMENTOS DOS SERVIÇOS DISPONÍVEIS: 
                        #         2 - Troca dos AMORTECEDORES  ------------------> R$ {amortecedores:7.2f} 
                        #         3 - Troca das PASTILHAS DE FREIOS  ------------> R$ {pastilhas_Freios:7.2f} 
                        #         4 - Troca dos PNEUS  --------------------------> R$ {pneus:7.2f} 
                        #         5 - Troca da SUSPENSÃO  -----------------------> R$ {suspensao:7.2f}
                        #         6 - Troca da DIREÇÃO  -------------------------> R$ {direcao:7.2f} 
                        #         7 - Troca da CAMBAGEM / CASTER  ---------------> R$ {cambagem:7.2f} 
                        #         8 - Ajuste do ALINHAMENTO DA DIREÇÃO ----------> R$ {alinhamento_Direcao:7.2f}""")
                        # mais_servicos = int(input("Gostaria de adicionar outro serviço: [1]- Sim ou [2]- Não:  "))
                        # if mais_servicos == 2:
                        #     orcamento_final = ar_Condicionado
                        #     print(f"Orçamento final: R$ {orcamento_final:7.2f}")
                        #     # break

                    case 2:
                        print(f"2 - Troca dos AMORTECEDORES  ------------------> R$ {amortecedores:7.2f} ")

                    case 3: 
                        print(f"3 - Troca das PASTILHAS DE FREIOS  ------------> R$ {pastilhas_Freios:7.2f} ")

                    case 4:
                        print(f"4 - Troca dos PNEUS  --------------------------> R$ {pneus:7.2f} ")

                    case 5:
                        print(f"5 - Troca da SUSPENSÃO  -----------------------> R$ {suspensao:7.2f}")

                    case 6:
                        print(f" 6 - Troca da DIREÇÃO  -------------------------> R$ {direcao:7.2f}")

                    case 7:
                        print(f" 7 - Troca da CAMBAGEM / CASTER  ---------------> R$ {cambagem:7.2f}")

                    case 8:
                        print(f"8 - Ajuste do ALINHAMENTO DA DIREÇÃO ----------> R$ {alinhamento_Direcao:7.2f}""")

                opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))

            else:
                print("Encerrando orçamento")
                opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))

        # OPÇÃO 4 - CENTROS AUTOMOTIVOS
        case 4:
            os.system("cls")
            print("------------- CENTROS AUTOMOTIVOS -------------")
            print(f"""
            R PEDROSO, 394 - BELA VISTA - SAO PAULO;

            AV RIO BRANCO, 1448 - CAMPOS ELISEOS - SAO PAULO;
                
            AV CRUZEIRO DO SUL, 607 - CANINDÉ - SAO PAULO;
                
            AV BRIGADEIRO LUIZ ANTONIO, 3383 - JARDIM PAULISTANO - SAO PAULO;
                
            AV LINS DE VASCONCELOS, 2474 - VILA MARIANA - SAO PAULO;
                
            R DOS TRILHOS, 1327 - MOOCA - SAO PAULO;
                
            R QUIRINO DOS SANTOS, 230 - BARRA FUNDA - SAO PAULO;
                
            R CARDEAL ARCOVERDE, 93 - PINHEIROS - SAO PAULO;
                
            R FRANÇA PINTO, 1115 - IBIRAPUERA - SAO PAULO;
                
            AV SUMARÉ, 73 - PERDIZES - SAO PAULO;
                
            R SILVA BUENO, 1176 - IPIRANGA - SAO PAULO;
                
            AV ENGENHEIRO CAETANO ALVARES, 1179 - CASA VERDE MEDIA - SAO PAULO;
                
            R CLODOMIRO AMAZONAS, 57 - ITAIM BIBI - SAO PAULO;
                
            R DEPUTADO LACERDA FRANCO, 410 - PINHEIROS - SAO PAULO;
                
            AV ABEL FERREIRA, 334 - VILA REGENTE FEIJO - SAO PAULO;
                
            R TUIUTI, 398 - TATUAPE - SAO PAULO;
                
            AV ALBERTO BYNGTON, 1401 - VILA MARIA ALTA - SAO PAULO;
                
            R TIJUCO PRETO, 434 - TATUAPÉ - SAO PAULO;
                
            R CERRO CORÁ, 419 - VILA ROMANA - SAO PAULO;
                
            R RUA ISABEL GARCIA, 89 - VILA PRUDENTE - SAO PAULO;
                
            R FAUSTOLO, 1855 - LAPA - SAO PAULO;
                
            AV DR. VITAL BRASIL, 963 - BUTANTÃ - SAO PAULO;
                
            AV GENERAL EDGAR FACO, 783 - VILA OLGA CECÍLIA - SAO PAULO;
                
            AV AMADOR BUENO DA VEIGA, 112 - PENHA DE FRANÇA - SAO PAULO;
                
            AV JORGE JOAO SAAD, 52 - VILA PROGREDIOR - SAO PAULO;
                
            R MARIO GOMES, 21 - PENHA DE FRANÇA - SAO PAULO;
                
            R GUAIPÁ, 1380 - VILA LEOPOLDINA - SAO PAULO;
                
            AV CORIFEU DE AZEVEDO MARQUES, 3297 - VILA LAGEADO - SAO PAULO;
                
            R AUGUSTO FARINA, 918 - JARDIM BONFIGLIOLI - SAO PAULO;
                
            AV WALDEMAR CARLOS PEREIRA, 1322 - VILA MATILDE - SAO PAULO;
                
            AV ELISIO CORDEIRO DE SIQUEIRA, 369 - SÃO DOMINGOS - SAO PAULO;
            """)

            opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))

        # OPÇÃO 5 - CONSULTAR DIAGNOSTICOS
        case 5:
            os.system("cls")
            print("Diagnósticos recentes:")
            print(f"""
                Nome.......: {nome_Cliente}
                CPF........: {cpf_Cliente}
                Telefone...: {telefone_Cliente}
                CEP........: {cep}
                Diagnostico: {diagnostico}
                """)
            opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))
            
        # OPÇÃO 6 - AGENDAMENTO DE REPAROS
        case 6:
            os.system("cls")
            print("------------- AGENDAMENTO DE REPAROS -------------")
            # print("""O(A) Sr(Sra) gostaria de agendar uma consulta para realizar algum reparo indispensável ?
            #       1 - SIM
            #       2 - NÃO""")
            # consulta_Mecanica = int(input("escolha uma das opções: "))
            # while consulta_Mecanica < 1 or consulta_Mecanica > 2:
            #     os.system("cls")
            #     print(f"ERRO OPÇÃO {consulta_Mecanica} INVÁLIDA !!!!! Por favor digite uma opção válida")
            #     print("""O(A) Sr(Sra) gostaria de agendar uma consulta para realizar algum reparo indispensável ?
            #       1 - SIM
            #       2 - NÃO""")
            #     consulta_Mecanica = int(input("escolha uma das opções: "))

            # if consulta_Mecanica == 1:
            print("Obrigado por escolher agendar uma consulta ")
            hora_consulta = input("Melhor horário para a consulta (digite no formato 24 horas exemplo (22:07)): ")
            data_consulta = input("Melhor data para consulta(digite a data completa exemplo (20/04/2024)).....: ")

            print("""Qual seria o local mais adequado para a consulta ?\n
                        1 - Minha Residência
                        2 - Centro Automotivo\n  """)
            local_consulta = int(input("escolha uma das opções: "))
            while local_consulta < 1 or local_consulta > 2:
                os.system("cls")
                print(f"ERRO OPÇÃO {local_consulta} INVÁLIDA !!!! Por gentileza  ")
                print("""Qual seria o local mais adequado para a consulta ?\n
                        1 - Minha Residência
                        2 - Centro Automotivo\n  """)
                local_consulta = int(input("escolha uma das opções: "))
            
            match local_consulta:
                case 1:
                    endereco = input("Endereço: ")
                    print(f"""
                        Localização............: {endereco}                  
                        Horário................: {hora_consulta} 
                        Data...................: {data_consulta}
                        Preço da consulta......: R$100,00
                        """)
                    print("AGENDAMENTO REALIZADO COM SUCESSO")

                case _:
                    endereco = input("Endereço: ")
                    print("Verificando Centros Automotivos perto da sua localização...")
                    time.sleep(1)
                    print(f"""
                        
                        Centros Automotivos perto:
                        Centro 1 - {centros_Auto_perto_Residencia[0]}
                        Centro 2 - {centros_Auto_perto_Residencia[1]}
                        Centro 3 - {centros_Auto_perto_Residencia[2]} 
                        Centro 4 - {centros_Auto_perto_Residencia[3]}
                        """)
                    escolha_centro_perto = int(input("Escolha um dos Centros Automotivos perto da sua residência: "))
                    while escolha_centro_perto < 1 or escolha_centro_perto > 4:
                        os.system("cls")
                        print(f"ERRO OPÇÃO {escolha_centro_perto} INVÁLIDA, Por gentileza digite uma opção válida")
                        print(f"""Centros Automotivos perto:
                        Centro 1 - {centros_Auto_perto_Residencia[0]}
                        Centro 2 - {centros_Auto_perto_Residencia[1]}
                        Centro 3 - {centros_Auto_perto_Residencia[2]} 
                        Centro 4 - {centros_Auto_perto_Residencia[3]}""")
                        escolha_centro_perto = int(input("Escolha um dos Centros Automotivos perto da sua residência: "))

                    match escolha_centro_perto:
                        case 1:
                            print(f"""
                        Centro Automotivo escolhido: {centros_Auto_perto_Residencia[0]} 
                        Horário....................: {hora_consulta} 
                        Data.......................: {data_consulta} 
                        Preço da consulta..........: R$100,00\n""")
                            print("AGENDAMENTO REALIZADO COM SUCESSO")

                        case 2:
                            print(f"""
                        Centro Automotivo escolhido: {centros_Auto_perto_Residencia[1]} 
                        Horário....................: {hora_consulta} 
                        Data.......................: {data_consulta} 
                        Preço da consulta..........: R$100,00\n""")
                            print("AGENDAMENTO REALIZADO COM SUCESSO")

                        case 3:
                            print(f"""
                        Centro Automotivo escolhido: {centros_Auto_perto_Residencia[2]} 
                        Horário....................: {hora_consulta} 
                        Data.......................: {data_consulta} 
                        Preço da consulta..........: R$100,00\n""")
                            print("AGENDAMENTO REALIZADO COM SUCESSO")

                        case _:
                            print(f"""
                            Centro Automotivo escolhido: {centros_Auto_perto_Residencia[3]} 
                            Horário....................: {hora_consulta} 
                            Data.......................: {data_consulta} 
                            Preço da consulta..........: R$100,00\n""")
                            print("AGENDAMENTO REALIZADO COM SUCESSO")
                    
                    opcao = str(input("Deseja escolher outra opção? <S>IM ou <N>AO: "))
        case 7:
            print("============================ Obrigado por contar com AutoCheckUp ================================")
            print("Finalizando programa...")
    if(opcao == 'n'):
        print("============================ Obrigado por contar com AutoCheckUp ================================")
        print("Finalizando programa...")
        break       

            

                    