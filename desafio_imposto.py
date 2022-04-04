
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
        valor1 = (self.imposto_total()) * 0.3
        valor2 = self.gastos_dedutiveis()
        if valor2 < valor1:
            return valor2
        else:
            return valor1
        
    def imposto_maximo_dedutivel(self):
        return self.imposto_total()*0.3
    
    def imposto_total(self):
        valor1 = self.imposto_salario(salario)
        valor2 = self.imposto_prest_servico(renda_prest) 
        valor3 = self.imposto_ganho_capital(renda_ganho)
        self.valor_total = valor1+valor2+valor3
        return self.valor_total
    
    def gastos_medicos(self,gastos):
        self.valor_gastos_medicos = gastos
        return self.valor_gastos_medicos

    def gastos_educacao(self,gastos):
        self.valor_gastos_educacao = gastos
        return self.valor_gastos_educacao
    
    def gastos_dedutiveis(self):
        self.valor_gastos_dedutiveis = self.gastos_medicos(gastos_med) + self.gastos_educacao(gastos_edu)
        return self.valor_gastos_dedutiveis


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
    print(f"Maximo dedutivel: R${calculo.imposto_maximo_dedutivel()}")
    print(f"Gastos dedutiveis: R${calculo.gastos_dedutiveis()}")

    print("\n RESUMO: ")
    print(f"Imposto bruto total: R${calculo.imposto_total()}")
    print(f"Abatimento: R${calculo.imposto_dedutivel()}")
    print(f"Imposto devido: R${(calculo.imposto_total() - calculo.imposto_dedutivel())}")
