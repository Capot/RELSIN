import conexao
import pandas as pd


class relatorio():

    def __init__(self):

        self.conn = conexao.conexao()
        self.curr = self.conn.conectar()
        #self.curr.cursor()

        self.saida = 'Contas Pagas.xlsx'

    def con_sql(self, empresa):
        sql = "SELECT " \
              "ECPGBAIXA.NUTITULO Titulo," \
              "ECPGBAIXA.NUPARCELA Parcela, " \
              "ECPGBAIXA.DTPAGTO Pago, " \
              "ECPGBAIXA.NUCONTA Conta, " \
              "CASE ECPGBAIXA.CDEMPRESA " \
              "WHEN 2 THEN '100' " \
              "WHEN 7 THEN '400' " \
              "WHEN 10 THEN '2' " \
              "END Empresa, " \
              "ECPGBAIXA.VLPAGTO Valor, " \
              "ECPGBAIXA.VLDESCONTO Desconto, " \
              "ECPGBAIXA.VLJUROS Juros, " \
              "ECPGBAIXA.VLMULTA Multa, " \
              "ECPGBAIXA.VLIMPOSTO Imposto, " \
              "ECPGBAIXA.FLPARCIALTOTAL Baixa, " \
              "ECPGBAIXA.DEOBSERVACAO OBS, " \
              "ECPGFINANCBANCARIO.VLCONTRATO Valor_Contrato, " \
              "ECPGFINANCBANCARIO.VLIOF IOF, " \
              "ECPGFINANCBANCARIO.VLTXESTRUTURACAO Taxa, " \
              "ECPGFINANCBANCARIO.PEJUROSMENSAL Juros_Mensal, " \
              "ECPGFINANCBANCARIO.TPSISTEMAAMORTIZACAO Sis_Amort, " \
              "ECPGFINANCBANCARIO.NUPRAZOCARENCIA Carencia, " \
              "ECPGFINANCBANCARIO.TPJUROS Tipo_Juros, " \
              "ECPGFINANCBANCARIO.NMCONTRATO Contrato, " \
              "ECPGFINANCBANCARIO.TPCARENCIA Tipo_Carencia " \
              "FROM ECPGBAIXA " \
              "FULL JOIN ECPGFINANCBANCARIO " \
              "ON ECPGBAIXA.NUTITULO = ECPGFINANCBANCARIO.NUTITULO " \
              "WHERE 1=1" \
              "AND ECPGBAIXA.NUTITULO IS NOT NULL " \
              "AND ECPGBAIXA.NUCONTA NOT IN ('REAPROPFIN') " \
              "AND ECPGBAIXA.CDEMPRESA = {} " \
              "ORDER BY ECPGBAIXA.DTPAGTO, ECPGBAIXA.NUTITULO, ECPGBAIXA.NUPARCELA ;" .format(empresa)
        self.curr.execute(sql)

    def imprimeTerminal(self):
        for lista in self.curr.fetchall():
            print(lista)

    def imprimi(self):
        #########PEGA NOME COLUNAS###########
        # coluna = [desc[0] for desc in cur.description]
        coluna = []
        i = 0
        for i in self.curr.description:
            coluna.append(i[0])

        print(coluna)
        #data = self.cur.fetchall()                              # ATRIBUI CONSULTA
        data = self.curr.fetchmany(100)
        consulta = pd.DataFrame(list(data), columns=coluna)     # MONTA DATAFRAME
        escreve = pd.ExcelWriter(self.saida)                    # CRIA ARQUIVO DE SAIDA
        consulta.to_excel(escreve, sheet_name='Contas Pagas')   # ESCREVE DATAFRAME NO ARQUIVO
        escreve.save()

    def closeconect(self):
        self.curr.close()



#rel = relatorio()
#rel.con_sql(2)
#rel.imprimeTerminal()
#rel.closeconect()