import streamlit as st
from PIL import Image

# Ler arquivo CSS e injetar na página
with open("style.css") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Exibir título e texto via markdown e HTML
html_content = """
<h1 class="apresentacao__conteudo__titulo">A Copa Libertadores da América <strong class="titulo-destaque">é Nossa!</strong></h1>
<p class="apresentacao__conteudo__texto">O título mais prestigioso do futebol sul-americano permanece na capital carioca! O Botafogo de Futebol e Regatas conquistou
a Copa Libertadores da América ao vencer o Atlético Mineiro por 3 a 1, mesmo jogando
com um atleta a menos desde o primeiro minuto da partida. Uma vitória histórica que
celebra a garra, a superação e o talento alvinegro!</p>
<div class="apresentacao__links">
    <a class="apresentacao__links__botons" href="https://www.youtube.com/watch?v=edpaMmfiD9w&t=7752s">Veja os melhores momentos da partida</a>
</div>
"""
st.markdown(html_content, unsafe_allow_html=True)

# Abrir e exibir imagem local
st.title("É Nossa!")
img = Image.open("liberta.jpg")
st.image(img, caption="Imagem da perna do jogador Luiz com tatuagem da taça da libertadores")
st.markdown("<p class='apresentacao__imagem__legenda'>Foto: Reprodução/TV</p>", unsafe_allow_html=True)