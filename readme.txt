receber dois arquivos json
arquivo-1 : nome-questoes.json
arquivo-2 : nome-template.json

    estrutura template json :
        stem : texto / {{variavel}} / {{{layer}}}
        cod-template : 1001
        stem-var
            nome-var :
                "valor-1"
                "valor-2"
                "valor-n"
        layer1 :
            layer-nome : "nome-layer"
            stem : texo {{variavel}} / texto
            layer-1-var
                nome-var-1:
                    "valor-1"
                    "valor-2"
                    "valor-n"
                nome-var-2 :
                    "valor-1"
                     "valor-2"
                     "valor-n"

    estrutura questoes json
        cod-template : 1001
        stem-var
            var-1  : 0
            var-2  : 1
            var-n  : n
        layer-1-var:
            var-1  : 0
            var-2  : 1
            var-n  : n
