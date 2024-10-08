import json

# Abrindo e carregando o arquivo template.json
with open('template.json', 'r') as template_file:
    template_data = json.load(template_file)

# Abrindo e carregando o arquivo questoes.json
with open('questoes.json', 'r') as questoes_file:
    questoes_data = json.load(questoes_file)


# Comparar o cod-template dos dois arquivos
if template_data["cod-template"] == questoes_data["cod-template"]:

    ...


else:
    print("Erro : O template e a lista de geração tem codigos diferentes")