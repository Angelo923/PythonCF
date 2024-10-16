# 1. Importar biblioteca flet
# 2. Definir constantes
# 3. Definir botões
# 4. Armazenar infornmações
# 5. Manipular infoprmações
# 6. Exibir informações

# 1. Importar biblioteca flet
import flet as ft

SALARIO_BRUTO = 6076.48
CONSIGNADOS = 1805.34
VA = 634.74
SEGURO_DE_VIDA = 2.31
FUNDO_MILITAR = 638.03
IR = 599.57
DESCONTO_SALARIO = SEGURO_DE_VIDA + FUNDO_MILITAR + IR
SALARIO_LIQUIDO = SALARIO_BRUTO + VA - CONSIGNADOS - DESCONTO_SALARIO
print(DESCONTO_SALARIO)
print(SALARIO_LIQUIDO)