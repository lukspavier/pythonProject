#!/usr/bin/env python
# coding: utf-8
No Brasil, a multa por excesso de velocidade pode ser enquadrada em três categorias: média, grave e gravíssima. Os valores são definidos de acordo com o percentual em que o motorista excede o limite da via. Por exemplo, se o motorista é flagrado a 48 km/h em uma via que a velocidade máxima permitida é de 40 km/h, ele ultrapassou o limite em 20%.

Os valores e as categorias são:
1. até 20% acima do limite permitido na via, infração média. Valor: R$ 130,16;
2. de 21% até 50% acima do limite permitido na via, infração grave. Valor: R$ 195,23;
3. a partir de 51% acima do limite permitido na via, infração gravíssima. Valor: R$ 880,41.

Para ajudar os agentes de trânsito em sua fiscalização de rotina, crie um programa para preparar a infração por excesso de velocidade. Considere que o programa deve receber, pelo menos, o número da placa do veículo, a velocidade analisada e o limite de velocidade da via. Em seguida, retorne uma mensagem ao agente informando os dados do veículo (placa), a categoria da infração e o valor da multa aplicada.

Suba seu código na conta do Github e compartilhe o link do projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

# In[18]:


placa = input("Placa do carro: ")
velomax = int(input("Velocidade máxima permitida: "))
velocar = int(input("Velocidade do veículo: "))

quo = velocar / velomax

if quo > 1 and quo < 1.20:
    print("Infração média, multa: R$130,16")
elif quo > 1.21 and quo < 1.50:
    print("Infração grave, multa: R$195,23")
elif quo > 1.51:
    print("Infração Gravíssima, multa: R$880,41")
else:
    print("Velocidade permitida")
    
print("Placa do veículo: "+placa)


# In[ ]:




