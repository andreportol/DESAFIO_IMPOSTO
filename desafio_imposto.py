
# calculando o valor do imposto sobre o salario

class DesafioImposto:

    def imposto_salario(self,salario):
        self.valor_imposto = 0
        salario = float(input("Renda anual com salario: "))
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

if __name__=="__main__":
    calculo = DesafioImposto()
    print(calculo.imposto_salario(35000))

