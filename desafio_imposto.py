
# calculando o valor do imposto sobre o salario

class DesafioImposto:
   
    def imposto_salario(self,salario):
        salario_mes= salario/12
        if salario_mes < 3000:
            self.valor_imposto = salario * 0
            return self.valor_imposto    
        elif 3000 <= salario_mes < 5000:
            self.valor_imposto = salario * 0.1
            return self.valor_imposto
        else:
            self.valor_imposto = salario * 0.2
            return self.valor_imposto
    
    def imposto_prest_servico (self,renda):
        self.renda = renda
        self.valor_imposto_renda = self.renda * 0.15
        return self.valor_imposto_renda
    
    def imposto_ganho_capital(self, ganho):
        self.ganho = ganho
        self.valor_imposto_ganho = self.ganho * 0.2
        return self.valor_imposto_ganho

    def imposto_dedutivel(self):
        return self.imposto_total() * 0.3
    
    def imposto_total(self):
        self.imposto_total = self.imposto_salario(salario) + self.imposto_prest_servico(renda_prest) + self.imposto_ganho_capital(renda_ganho)
        return self.imposto_total
    
    def gastos_medicos(self,gastos):
        self.gastos_medicos = gastos
        return self.gastos_medicos

    def gastos_educacao(self,gastos):
        self.gastos_educacao = gastos
        return self.gastos_educacao
    
    def gastos_dedutiveis(self):
        self.gastos_dedutiveis = self.gastos_medicos(gastos_med) + self.gastos_educacao(gastos_edu)
        return self.gastos_dedutiveis


if __name__=="__main__":
    salario = float(input("Renda anual com salario: "))
    renda_prest = float(input("Renda anual com prestacao de servicos: "))
    renda_ganho = float(input("Renda anual com ganho de capital: ")) 
    gastos_med = float(input("Gastos medicos: "))
    gastos_edu = float(input("Gastos educacionais: "))
    
    print("\n****************Relatório de imposto de renda*************")

    print("CONSOLIDADO DE RENDA")
    calculo = DesafioImposto()
    print(f"Imposto sobre salario: R${calculo.imposto_salario(salario)}")
    print(f"Imposto sobre servicos: R${calculo.imposto_prest_servico(renda_prest)}")
    print(f"Imposto sobre ganho de capital: R${calculo.imposto_ganho_capital(renda_ganho)}")
    
    print("\n DEDUCOES: ")
    print(f"Maximo dedutivel: R${calculo.imposto_dedutivel()}")
    print(f"Gastos dedutiveis: R${calculo.gastos_dedutiveis()}")

    print("\n RESUMO: ")
    #print(f"Imposto bruto total: R${calculo.imposto_total()}")
    #print(f"Abatimento: R${calculo.imposto_dedutivel()}")
    #print(f"Imposto devido: R${(calculo.imposto_total())}")
