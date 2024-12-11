class Persona:
    def __init__(self):

        self.__peso=0
        self.__altura=0.0
        self.__imc=0.0


    #metodos: 1 metodo por cada caso de uso
    #def nombreCasodeUso(self,parametros)(precondiciones separadas con comas)
    def valorerror (self, peso,altura):
        if not (1 <= peso <= 600):
            raise ValueError("Ingresa un peso válido")
        if not(0.5 <= altura <= 2.6):
            raise  ValueError("Ingresa una altura válida.")
        self.__peso = peso
        self.__altura = altura
    


    def calcularIndicedeMasaCorporal(self):
        self.__imc= (self.__peso/(self.__altura*self.__altura))
        return self.__imc
    
    def clasificarimc(self):
        if self.__imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= self.__imc < 24.9:
            return "Peso normal"
        elif 25 <= self.__imc < 29.9:
            return "Sobrepeso"
        if self.__imc > 30.0:
            return "Obesidad" 
    
