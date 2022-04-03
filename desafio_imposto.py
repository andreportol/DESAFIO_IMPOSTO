
# calculando o valor do imposto sobre o salario

class DesafioImposto:
   
    def imposto_salario(self,salario):
        salario = salario/12
        if salario < 3000:
            self.valor_imposto = salario * 0
            return self.valor_imposto    
        elif 3000 <= salario < 5000:
            self.valor_imposto = salario * 0.1
            return self.valor_imposto
        else:
            self.valor_imposto = salario * 0.2
            return self.valor_imposto
    
    def imposto_prest_servico (self,renda):
        self.renda = renda
        valor_imposto_renda = self.renda * 0.15
        return self.valor_imposto
    
    def imposto_ganho_capital(self, ganho):
        self.ganho = ganho
        valor_imposto_ganho = self.ganho * 0.2
        return valor_imposto_ganho
    
    def gastos_medicos(self,gastos):
        self.gastos_medicos = gastos
        return self.gastos_medicos

    def gastos_educacao(self,gastos):
        self.gastos_educacao = gastos
        return self.gastos_educacao


if __name__=="__main__":
    salario = float(input("Renda anual com salario: "))
    renda_prest = float(input("Renda anual com prestacao de servicos: "))
    renda_ganho = float(input("Renda anual com ganho de capital: ")) 
    gastos_med = float(input("Gastos medicos: "))
    gastos_edu = float(input("Gastos medicos: "))
    
