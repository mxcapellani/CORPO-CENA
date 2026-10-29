---
name: corpo-cena
description: Analisa fotografias, renderizações arquitetônicas e ambientes visuais para gerar prompts altamente detalhados de inserção fotorrealista de pessoas e animais, preservando rigorosamente arquitetura, iluminação, materiais, geometria, perspectiva e composição originais. Use quando o usuário pedir para adicionar pessoas, figuras humanas ou animais a uma imagem de ambiente.
---

# CORPO-CENA

Skill para criar prompts de inserção fotorrealista de pessoas e animais em imagens existentes, sem alterar a cena original.

## Princípio central

A imagem original é **intocável**. Apenas pessoas/animais são adicionados. Nada na arquitetura, iluminação, materiais, geometria, perspectiva ou composição pode mudar.

## Fluxo de trabalho

1. **Analisar a imagem** e registrar:
   - **Arquitetura e geometria**: tipo de espaço, elementos construtivos, linhas de fuga, pé-direito, escala (portas ≈ 2,10 m, degraus, mobiliário).
   - **Perspectiva e câmera**: altura do horizonte, ângulo, distância focal aparente, profundidade de campo, enquadramento.
   - **Iluminação**: direção, temperatura de cor (K), dureza das sombras, fontes (natural/artificial), reflexos e luz ambiente.
   - **Materiais e superfícies**: texturas, brilho, reflexividade, cores predominantes.
   - **Composição**: pontos focais, áreas livres, planos (primeiro, médio, fundo), zonas de circulação plausíveis.
   - **Qualidade técnica**: granulação, nitidez, estilo (foto real ou render), pós-processamento.
2. **Definir as inserções**: quantidade, posição (plano e coordenadas relativas), escala coerente com a câmera, pose, ação natural para o espaço, vestuário adequado ao estilo e clima, direção do olhar, espécie/raça e porte dos animais.
3. **Garantir integração física**: sombras de contato e projetadas conforme a luz existente, iluminação e cor de reflexo compatíveis, oclusão correta por objetos, reflexos em superfícies brilhantes, desfoque conforme a profundidade de campo, mesma granulação e nitidez da imagem.
4. **Redigir o prompt** na estrutura abaixo.
5. **Revisar** com o checklist.

## Estrutura do prompt gerado

1. **Instrução principal**: "Insira [descrição] na imagem fornecida, mantendo todo o restante idêntico."
2. **Descrição da cena original** (resumo objetivo do que deve ser preservado).
3. **Inserções**: para cada pessoa/animal — posição, escala, pose, ação, vestuário/pelagem, expressão, direção do olhar.
4. **Integração de luz e sombra**: direção, temperatura, sombras, reflexos.
5. **Perspectiva e escala**: altura do horizonte, proporções, profundidade de campo.
6. **Restrições de preservação**: lista explícita do que não pode mudar.
7. **Prompt negativo**: o que evitar.

## Restrições de preservação (sempre incluir)

- Não alterar arquitetura, geometria, proporções ou perspectiva.
- Não alterar iluminação, cores, materiais, texturas ou reflexos existentes.
- Não mover, remover ou adicionar objetos além das pessoas/animais solicitados.
- Não recortar, reenquadrar nem mudar resolução ou proporção da imagem.
- Não aplicar filtros, estilização ou mudança de atmosfera.

## Prompt negativo (modelo)

deformações anatômicas, mãos ou dedos extras, proporções incorretas, escala errada, pessoas flutuando, sombras ausentes ou incoerentes, iluminação divergente, aparência de recorte/colagem, bordas serrilhadas, pessoas olhando para a câmera sem motivo, rostos distorcidos, texto, marca d'água, alteração do cenário, mudança de perspectiva.

## Checklist final

- [ ] Escala das figuras coerente com portas, mobiliário e distância da câmera.
- [ ] Pés/patas apoiados com sombra de contato.
- [ ] Sombras e luz na mesma direção e temperatura da cena.
- [ ] Nitidez, granulação e profundidade de campo iguais às da imagem.
- [ ] Nenhum elemento original alterado.
- [ ] Poses e ações naturais para o uso do espaço.
- [ ] Prompt em linguagem objetiva, detalhada e sem ambiguidades.

## Exemplo resumido

> Insira duas pessoas conversando em pé ao lado do sofá e um cachorro golden retriever deitado no tapete, na imagem fornecida, mantendo todo o restante idêntico. Cena: sala contemporânea, câmera a 1,2 m de altura, lente ~24 mm, luz natural quente (~4500 K) vinda da janela à esquerda, sombras suaves projetadas para a direita. As pessoas medem ~1,70 m em relação à porta de 2,10 m, vestem roupas casuais em tons neutros, com sombras de contato no piso de porcelanato e leve reflexo nele. Preservar arquitetura, materiais, iluminação, perspectiva e composição originais. Negativo: deformações, escala errada, sombras incoerentes, aparência de colagem, alteração do cenário.
