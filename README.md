# **Web Scraping de Filmes de Natal**


### **Preparando o Sistema** 

Para conseguir rodar o projeto é preciso instalar as bibliotecas e frameworks python que estão no arquivo requirements.txt. Caso use o sistema operacional Linux, abra o terminal e rode o seguinte comando:

```pip install -r requirements.txt```

Caso não tenha o pip instalado, execute:

```sudo apt-get install python-pip```

Para instalar o Jupyter Notebook, rode o comando:

```pip install jupyter```

### **Gerador de Nuvem de Palavras**

Para gerar a imagem .png das nuvens de palavras das sinopses que estão no arquivo sinopses.txt, execute o seguinte comando:

```python3 gerardor_wordcloud.py sinopses.txt nuvem_de_palavras```