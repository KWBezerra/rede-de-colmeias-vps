---

# 🌿 Rede de Colmeias

Portal educativo e colaborativo para iniciantes em **meliponicultura** (criação de abelhas nativas sem ferrão).
O projeto tem como objetivo **conectar pessoas, hortas comunitárias e iniciativas ambientais**, promovendo a preservação da biodiversidade e incentivando práticas sustentáveis.

---

## 📌 Funcionalidades

* **Página Inicial**

  * Apresenta o projeto e a importância da preservação das abelhas nativas.
  * Design responsivo e moderno, com destaque para a identidade visual.

* **Tutoriais**

  * Lista de tutoriais com sidebar dinâmica.
  * Conteúdo escrito em **Markdown**, renderizado no site.
  * Gerenciamento via **Django Admin**, facilitando a publicação de novos tutoriais.

* **Doações (Em desenvolvimento)**

  * Página de apresentação da futura funcionalidade.
  * Ideia: permitir que hortas comunitárias se cadastrem e recebam apoio (colmeias, materiais, conhecimento).
  * 
---

## 🛠️ Tecnologias utilizadas

* **Backend:** [Django](https://www.djangoproject.com/)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Banco de Dados:** SQLite (desenvolvimento)
* **Gerenciamento de dependências:** pip + venv
* **Markdown renderizado:** [markdown2](https://github.com/trentm/python-markdown2)

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/KWBezerra/rede-de-colmeias.git
cd rede-de-colmeias
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Realize as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6. Rode o servidor

```bash
python manage.py runserver
```

Acesse o projeto em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📸 Layout

### Página Inicial

* Destaque para o título, imagem estilizada em hexágono e botões de ação.

### Tutoriais

* Sidebar lateral com lista dinâmica de tutoriais.
* Conteúdo formatado em Markdown.

### Doações (futuro)

* Pessoas responsaveis por Hortas comunitarias, podem preencher um formulario solicitando particiapar da "Rede de colmeias".
* Pode solicitar o que deseja receber (ex:colmeias, instruçoes, materiais e etc...)
---

## 🎯 Objetivos do projeto

* **Extensão universitária:** desenvolver um portal de impacto social e ambiental.
* **Educação:** oferecer conteúdo acessível sobre meliponicultura.
* **Colaboração:** criar um espaço para troca de conhecimento e recursos entre interessados em abelhas sem ferrão.

---



