# IPStats - Verificador de Dispositivos e Portas Abertas 🌐🔓

O IPStats é um script em Python que permite verificar a disponibilidade de dispositivos na rede e também verificar as portas abertas de um determinado host.

## Requisitos 📋

- Python 3.x 🐍
- Nmap (para a funcionalidade de verificação de portas abertas) 🌐
- Tabulate (instalado automaticamente durante a execução) 📊

## Como Usar 🚀

1. Certifique-se de ter o Python 3.x instalado em seu sistema. Caso não tenha, você pode baixá-lo [aqui](https://www.python.org/downloads/).

2. Instale o Nmap (Network Mapper) em seu sistema. Você pode fazer isso através do terminal com o seguinte comando:
   ```
   pkg installl nmap
   ```

3. Clone este repositório para o seu computador ou baixe o arquivo `IPStats.py`.

4. Abra um terminal e navegue até o diretório onde o arquivo `IPStats.py` está localizado.

5. Execute o script usando o Python 3:
   ```
   python3 IPStats.py
   ```

6. Siga as instruções do menu para selecionar as opções desejadas.

## Funcionalidades 🛠️

- Verificação de dispositivo online por IP individual.
- Verificação de múltiplos dispositivos online por meio de uma lista de IPs.
- Exibição do histórico de verificações realizadas.
- Limpeza do histórico.
- Verificação de portas abertas para um determinado host.

## Observações 🧐

- Certifique-se de ter permissões para executar o Nmap e outras operações de rede.
- A funcionalidade de verificação de portas abertas requer a instalação do Nmap.
- Lembre-se de obter permissão antes de executar verificações em dispositivos ou redes que não sejam de sua propriedade.
