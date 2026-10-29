# CORPO & CENA
Skill de integração fotorrealista de pessoas e animais em fotografias e renders arquitetônicos. Preserva arquitetura, materiais, mobiliário, luz, câmera e composição da referência.

## Entrega
Análise técnica, três propostas distintas (minimalista, social e lifestyle adaptáveis), **seis prompts completos: três PT-BR e três EN**, restrições/negativo e recomendação. Cada prompt é independente. Preferências de quantidade e espécie prevalecem; pets não são adicionados sem pedido.

## Capacidades preservadas
Leitura arquitetônica, luz, perspectiva, escala humana, pessoas/pets, três variações, bilinguismo, preservação, realismo físico, contexto e engenharia de prompts. Especificação original integral em [docs](docs/SOURCE_SPECIFICATION.md). “Preservado” descreve documentação e instruções, não equivalência comprovada com um agente original.

## Uso e instalação
Copiar a pasta `.agents/skills/corpo-cena` para a mesma estrutura do projeto alvo. O host deve reconhecer Skills ou carregar [SKILL.md](.agents/skills/corpo-cena/SKILL.md) explicitamente.
Pedido: “Nesta foto da varanda, crie três composições com uma pessoa em cada opção, sem pets; mantenha tudo no ambiente”. Requer visão e imagem acessível para análise real. Sem visão, a proposta por descrição é explicitamente não verificada.
Modelo de linguagem gera os prompts; editor de imagem externo só é necessário para renderização. A Skill não gera imagens por padrão, não configura APIs e não pede credenciais. [Instalação e atualização](docs/INSTALLATION.md).

## Melhorias e limitações
Tratamento de entradas incompletas, quantidade explícita, regiões proibidas, revisão contextual, perfis e continuidade textuais. Comparação é visual e condicional; máscaras não são aplicadas automaticamente. Não há garantia pixel a pixel, medição física, EXIF inferido ou validação de projeto. [Auditoria](docs/AUDIT.md).

## Testes
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py'
```
Validação verifica YAML, links, regras essenciais e seis prompts do exemplo; não verifica a imagem ou equivalência semântica. [Aceitação](tests/acceptance-tests.md), [comparação](tests/comparison-matrix.md), [resultados](tests/RESULTS.md). Actions configurado para integridade estrutural.

MIT. [Histórico](CHANGELOG.md). A especificação fornecida é documentação funcional, não acesso a configurações privadas ou código do agente original.
