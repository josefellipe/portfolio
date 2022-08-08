# Find repetitions excel with python (pandas)

Esse programa importa uma tabela do excel e analisa as ocorrências repetidas, além de contar e criar uma aba para o número de repetições. Para importar a tabela foi usada a biblioteca pandas.


Alguns dos desafios encontrados e como solucionei:

- Primeiro tive que importar os dados e formatalos em uma matriz para poder manipula-los.
- Como parte do objetivo era deletar as ocorrências repetidas depois de contá-las, foi necessário criar uma PrimaryKey para facilitar a distinção entre um dado repetido e outro.
- Depois de totalmente tratada e com o contador e a PrimaryKey adicionados introduzi algumas funcionalidades e interações com o usuário.
- Em cada imput de interação com o usuário foi verificado se a entrada era correta, para livrar o programa de erros e loops, quando a entrada não era a esperada então o programa manda uma mensagem de chave inválida e refaz a pergunta.
- Uma das interações foi a criação de um filtro para mostrar apenas a parte da lista que interessa ao usuário.
