# Projetos com Pandas

1 - Contando repetições em uma planilha do excel.
2 - Sistema de gestão de uma academia de luta (Pandas | Excel como banco de dados)


1 - Contando repetições em uma planilha do excel.
  O código foi feito na linguagem Python com o uso da biblioteca Pandas.
  
  Proposta:
    - Pegar uma tabela do excel com ocorrencias repetidas e então contar quantas ocorrência repetidas há e também selecioná-las dizendo quantas vezes acontecem, além de remover tais repetições para manter apenas uma delas. 
  
  O que foi feito:
    - Importei os dados da tabela com o pandas.
    - Tratei e organizei os dados, para então poder manipula-los com facilidade.
    - Adicionei uma Primary-Key para conseguir remover as ocorrências repetidas.
    - Criei um filtro para o usuário poder selecionar somente as informações que eram de seu interesse.
    - Adicionei mensagens de erros e retornos para quando o usuário clicasse em uma tecla inválida."
    

2 - Sistema de gestão de uma academia de luta (Pandas)
  O código foi feito na linguagem Python com o uso da biblioteca Pandas.
  
  Proposta:
    - Criar um sistema para gerenciar as mensalidades, despesas e graduções, além de um controle de alunos ativos.
    
 O que foi feito:
    - O sistema conta com 3 planilhas no excel para utilizar como banco de dados. 
    - Cadastrar os alunos, cada aluno tem sua data de vencimento de mensalidade e valor da mesma, além de seus dados, como nome, faixa, grau...
    - Pode-se adicionar, editar, consultar ou excluir tanto o cadastro de um aluno quanto um lançamento financeiro, tudo pelo programa.
    - Lançar recebimentos como a mensalidade ou outros, além de pagamentos de contas, como aluguéis e luz.
    - As mensalidades são atualizadas automaticamente todo mês no dia do vencimento do aluno e fica como um débito no nome do mesmo.
    - Na área de consulta financeira pode ser salvo um relatório de determinado mês, onde é mostrado cada gasto ou recebível, além do faturamento líquido.
