from aig_tools import generate_questions

# gerar questões 50 questões (if simples)
generate_questions('files/if-simples-template.json', 'files/if-simples-questoes.json', qtd_itens=10)

# gerar questões 50 questões (if composto)
generate_questions('files/if-composto-template.json', 'files/if-composto-questoes.json', qtd_itens=10)
