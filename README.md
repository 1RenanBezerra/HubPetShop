# HubPetShop_SemIntegraçãoOracle

## Descrição

Este projeto é uma interface simples de um pet shop desenvolvida em Python. Ele permite o gerenciamento básico de pets, incluindo cadastro, listagem, alteração e exclusão de registros. Os dados são armazenados temporariamente em uma lista na memória, sem integração com banco de dados. É ideal para demonstrações ou projetos educacionais.

**Nota:** Este projeto não possui integração com banco de dados, conforme indicado no nome. Todos os dados são perdidos ao fechar o programa.

## Funcionalidades

- **Cadastrar Pet**: Adicione um novo pet informando nome, tipo (ex: cachorro, gato) e idade.
- **Listar Pets**: Visualize todos os pets cadastrados com seus detalhes.
- **Alterar Pet**: Modifique as informações de um pet existente (nome, tipo e idade).
- **Excluir Pet**: Remova um pet específico da lista.
- **Excluir Todos os Pets**: Limpe toda a lista de pets com confirmação.
- **Sair**: Encerre o programa.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `pandas` (para manipulação de dados, embora neste projeto seja usada principalmente para importação)
- Biblioteca `os` (incluída no Python padrão)
- Biblioteca `time` (incluída no Python padrão)

## Instalação

1. **Clone ou baixe o repositório:**
   ```
   git clone https://github.com/seu-usuario/HubPetShop_SemIntegraçãoOracle.git
   cd HubPetShop_SemIntegraçãoOracle
   ```

2. **Instale as dependências:**
   Se você não tiver o `pandas` instalado, execute:
   ```
   pip install pandas
   ```

   As outras bibliotecas (`os` e `time`) já vêm com o Python.

## Como Usar

1. **Execute o programa:**
   Abra um terminal no diretório do projeto e execute:
   ```
   python atvPetShop.py
   ```

2. **Navegação no Menu:**
   - O programa exibirá um menu com opções numeradas de 1 a 6.
   - Digite o número da opção desejada e pressione Enter.
   - Siga as instruções na tela para cada operação.

3. **Exemplo de Uso:**
   - Escolha "1" para cadastrar um pet: Digite nome (apenas letras), tipo (apenas letras) e idade (número inteiro).
   - Escolha "2" para listar pets: Veja todos os pets cadastrados.
   - Para alterar ou excluir, digite o nome do pet quando solicitado.

**Atenção:** Os dados são armazenados apenas na memória. Ao fechar o programa, todos os registros são perdidos.

## Estrutura do Projeto

```
HubPetShop_SemIntegraçãoOracle/
├── atvPetShop.py    # Arquivo principal com o código do programa
└── README.md        # Este arquivo de documentação
```

- `atvPetShop.py`: Contém todas as funções do programa, incluindo menu, validações e operações CRUD básicas.

## Validações Implementadas

- **Nome e Tipo**: Aceitam apenas letras (sem números ou caracteres especiais).
- **Idade**: Aceita apenas números inteiros.
- **Opções do Menu**: Validação para garantir que a escolha esteja entre 1 e 6.
- **Confirmação**: Para exclusão em massa, há uma confirmação para evitar acidentes.

## Limitações

- Dados não persistem após o fechamento do programa.
- Não há integração com banco de dados.
- Interface baseada em terminal (linha de comando).
- Não suporta múltiplos pets com o mesmo nome (a busca é por nome exato).

## Possíveis Melhorias Futuras

- Integração com banco de dados (SQLite, PostgreSQL, etc.).
- Interface gráfica (usando Tkinter ou web com Flask/Django).
- Validações mais robustas (ex: limites de idade).
- Exportação de dados para CSV ou JSON.
- Funcionalidades adicionais como agendamento de serviços.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes (se aplicável).

## Autor

Desenvolvido por [Seu Nome]. Para dúvidas ou sugestões, entre em contato via [seu-email@example.com].

---

**Última atualização:** Abril 2026 
