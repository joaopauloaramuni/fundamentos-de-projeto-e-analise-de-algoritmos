# Algoritmo resolvedor de Sudoku com backtracking | Sudoku Solver

**Última atualização no Geeks for Geeks:** 31 de janeiro de 2025

Dado um Sudoku incompleto na forma de matriz `mat[][]` de ordem 9×9, a tarefa é completar o Sudoku.

Uma solução de Sudoku deve satisfazer todas as seguintes regras:

- Cada um dos dígitos de 1 a 9 deve ocorrer exatamente uma vez em cada linha.
- Cada um dos dígitos de 1 a 9 deve ocorrer exatamente uma vez em cada coluna.
- Cada um dos dígitos de 1 a 9 deve ocorrer exatamente uma vez em cada uma das 9 subgrades 3×3 da matriz.

**Nota:** Zeros na `mat[][]` indicam espaços em branco, que devem ser preenchidos com algum número entre 1 e 9. Você não pode substituir o elemento em uma célula que não esteja em branco.

---

## Exemplos:

| <img src="https://joaopauloaramuni.github.io/python-imgs/Sudoku_Solver/imgs/Suduko-example-question.png" alt="Input" width="600"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/Sudoku_Solver/imgs/Suduko-example-answer.png" alt="Output" width="600"/> |
|:------:|:-----:|
| Input | Output | 

**Explicação:** Cada linha, coluna e caixa 3×3 da matriz de saída contém números únicos.

---

## [Abordagem Ingênua] Usando Backtracking

A ideia é usar backtracking e gerar recursivamente todas as configurações possíveis de números de 1 a 9 para preencher as células vazias da matriz `mat[][]`.

Para isso, para cada célula não atribuída, preencha a célula com um número de 1 a 9, um por um. Após preencher a célula não atribuída, verifique se a matriz é segura ou não. Se for segura, vá para a próxima célula; caso contrário, retroceda (backtrack) para testar outros casos.

Para verificar se é seguro colocar o valor `num` na célula `mat[i][j]`, percorra todas as colunas da linha `i`, todas as linhas da coluna `j` e a subgrade 3×3 que contém a célula `(i, j)` e verifique se já possuem o valor `num`. Se sim, retorne `false`, caso contrário, retorne `true`.

**Complexidade de Tempo:** `O(n * 9^(n*n))`  
Para cada índice não atribuído, há 9 opções possíveis e, para cada índice, estamos verificando outras colunas, linhas e caixas.

**Espaço Auxiliar:** `O(1)`

---

## [Abordagem Esperada] Usando Bitmasking com Backtracking — `O(9 * n * n)` Tempo e `O(n)` Espaço

Na abordagem acima, a função `isSafe()` (usada para verificar se é seguro colocar o número `num` na célula `(i, j)`) pesquisa o `num` em cada linha, coluna e caixa.

A ideia é otimizar isso usando **Bitmasking**. Para isso, crie três arrays: `rows[]`, `cols[]` e `boxs[]`, de tamanho `n`, para marcar os valores já utilizados na linha, coluna e caixa, respectivamente.

O elemento `rows[i]` marca os números já utilizados na linha `i`, e o mesmo vale para `cols[]` e `boxs[]` para colunas e caixas. Para marcar o número `num` na linha `i`, defina o bit correspondente ao `num` da esquerda para a direita em `rows[i]` e proceda de forma semelhante para `cols[]` e `boxs[]`.

Da mesma forma, para desmarcar o valor `num`, desfaça os bits definidos no passo atual.

**Complexidade de Tempo:** `O(9 * n * n)`  
**Espaço Auxiliar:** `O(n)`

---

## 💡 Conceitos Importantes

### 🔁 Backtracking (Retrocesso)

**Backtracking** é uma técnica usada para explorar **todas as possibilidades** de forma sistemática, **voltando atrás** quando percebe que determinada escolha não leva a uma solução.

#### 🧠 Como funciona no Sudoku?

1. **Percorre** a matriz em busca de uma célula vazia.
2. **Tenta** preencher a célula com um número de `1` a `9`.
3. **Verifica** se o número é seguro (respeita as regras do Sudoku).
4. Se for seguro:
   - **Avança** para a próxima célula.
5. Se não for:
   - **Volta atrás** (*backtrack*) e tenta o próximo número.
6. O processo continua até que toda a matriz seja preenchida corretamente.

> 📈 **Complexidade de Tempo (ingênua):** `O(n * 9^(n*n))`  
> 📦 **Espaço Auxiliar:** `O(1)`

---

### 💡 Bitmasking

**Bitmasking** é uma técnica de otimização que usa operações com bits (`&`, `|`, `^`, `<<`, `>>`) para representar conjuntos de forma compacta e rápida.

#### ⚙️ Como funciona no Sudoku?

Ao invés de verificar **toda a linha, coluna e caixa** toda vez que queremos testar um número, usamos **máscaras de bits** para marcar os números já usados:

- Criamos 3 arrays de inteiros:
  ```python
  row = [0] * n
  col = [0] * n
  box = [0] * n
  ```

- Cada posição é um número inteiro onde **os bits de 1 a 9** representam se aquele número já foi usado (`1`) ou não (`0`).

#### ✅ Para marcar o número `num`:

```python
row[i] |= (1 << num)
col[j] |= (1 << num)
box[i // 3 * 3 + j // 3] |= (1 << num)
```

#### ❌ Para desmarcar o número (quando fazemos backtrack):

```python
row[i] &= ~(1 << num)
col[j] &= ~(1 << num)
box[i // 3 * 3 + j // 3] &= ~(1 << num)
```

> 📈 **Complexidade de Tempo (com bitmasking):** `O(9 * n * n)` (mais eficiente)  
> 📦 **Espaço Auxiliar:** `O(n)`  

---

## Referências

- [Algoritmo resolvedor de Sudoku | Sudoku Solver - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/sudoku-backtracking-7/)

---
