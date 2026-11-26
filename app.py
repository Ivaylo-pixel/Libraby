import streamlit as st

st.title("📚 Дигитална библиотека")

# Запазване в сесията
if "books" not in st.session_state:
    # Всяка книга е списък: [заглавие, автор, жанр]
    st.session_state.books = [
        ["Хари Потър", "Дж. К. Роулинг", "Фентъзи"],
        ["Малкият принц", "Антоан дьо Сент-Екзюпери", "Приказка"],
        ["Хобит", "Дж. Р. Р. Толкин", "Фентъзи"],
        ["1984", "Джордж Оруел", "Антиутопия"],
        ["Под игото", "Иван Вазов", "Роман"],
    ]

# ---------- ТЪРСЕНЕ ----------
st.subheader("🔍 Търсене на книга")
st.write("Попълнете едно или няколко полета:")
search_title = st.text_input("Търси по заглавие")
search_author = st.text_input("Търси по автор")
search_genre = st.text_input("Търси по жанр")

if st.button("Търси"):
    found = False
    for book in st.session_state.books:
        if (search_title.lower() in book[0].lower()
                and search_author.lower() in book[1].lower()
                and search_genre.lower() in book[2].lower()):
            st.success("📖 " + book[0] + " | Автор: " + book[1] + " | Жанр: " + book[2])
            found = True
    if found == False:
        st.warning("Няма такава книга!")

# ---------- ДОБАВЯНЕ ----------
st.subheader("➕ Добавяне на книга")
new_title = st.text_input("Заглавие")
new_author = st.text_input("Автор")
new_genre = st.text_input("Жанр")

if st.button("Добави"):
    if new_title != "":
        new_book = [new_title, new_author, new_genre]
        st.session_state.books.append(new_book)
        st.success("Книгата е добавена!")
    else:
        st.warning("Моля, въведете поне заглавие!")

# ---------- СТАТИСТИКА ----------
st.subheader("📊 Статистика")
total = len(st.session_state.books)
st.metric("Общ брой книги", total)

# ---------- ВСИЧКИ КНИГИ ----------
st.subheader("📖 Всички книги")
if len(st.session_state.books) == 0:
    st.info("Библиотеката е празна!")
else:
    for book in st.session_state.books:
        st.write("📖", book[0], "| Автор:", book[1], "| Жанр:", book[2])

# ---------- ИЗТРИВАНЕ ----------
st.subheader("🗑️ Изтриване на книга")
if len(st.session_state.books) > 0:
    labels = []
    for book in st.session_state.books:
        labels.append(book[0] + " - " + book[1])

    selected = st.selectbox("Изберете книга:", labels)

    if st.button("Изтрий"):
        position = labels.index(selected)
        st.session_state.books.pop(position)
        st.success("Книгата е изтрита!")
        st.rerun()
else:
    st.info("Няма книги за изтриване!")

# ---------- СОРТИРАНЕ ----------
st.subheader("🔤 Сортиране")
if st.button("Сортирай по азбучен ред"):
    st.session_state.books.sort()
    st.rerun()
