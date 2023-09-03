#Em SQUADs
"""
Objetivo da atividade: Praticar os conceitos vistos até aqui. 
Como: Faça um programa que capture o nome do usuário, altura em metros, 
idade e imprima esses dados na tela. 
"""
#Variaveis

nome = input("Olá, por favor, insira o seu nome: ")
altura = input(f"{nome}, digite a sua altura em metros: ")
idade = input("agora digite, por favor, a sua idade: ")

#Saida com interpolação

print (f"{nome}, sua altura é {altura} e sua idade é {idade}.")

#Nova Feature Notas

primeiraNota = float(input(f'{nome}, digite a nota da sua primeira avaliação: '))

segundaNota = float(input('agora digite a nota da sua segunda avaliação: '))

somaNota = primeiraNota + segundaNota
mediaNota = somaNota/2

print(f"{nome} a soma das notas de suas avaliações é: {somaNota}, e a média é: {mediaNota}")
