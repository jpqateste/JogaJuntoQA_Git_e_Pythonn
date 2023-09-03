#Em SQUADs
"""Leiam o caso abaixo e executem usando Python.
A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens 
nominais a cada um. A mensagem seria a seguinte:
Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no 
valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10.
"""
#Variaveis
nomeCliente = "Paula Martins"
mesCompra  = "Janeiro"
valorCompra = "500"
valorDesconto = "10"
tagCupom = "PAULAE10"

print ('Olá, '+nomeCliente+ '. Em ' + mesCompra + ' você realizou uma compra no valor de R$ '+valorCompra+',00 e ganhou um desconto de '+ valorDesconto +'% em sua próxima compra, use o cupom '+tagCupom+'.')

#Com interpolação

print (f"Olá, {nomeCliente}. Em {mesCompra} você realizou uma compra no valor de R$ {valorCompra},00 e ganhou um desconto de {valorDesconto}% em sua próxima compra, use o cupom {tagCupom}.")
