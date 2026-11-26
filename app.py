import streamlit as st

st.title("📚 Дигитална библиотека")

# Запазване в сесията
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "books" not in st.session_state:
    st.session_state.books = []

# ---------- ВХОД ----------
if st.session_state.logged_in == False:
    st.subheader("Вход за библиотекар")
    password = st.text_input("Парола", type="password")

    if st.button("Влез"):
        if password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Грешна парола!")

# ---------- ПАНЕЛ НА БИБЛИОТЕКАРЯ ----------
else:
    st.write("Добре дошли, библиотекар!")

    if st.button("Изход"):
        st.session_state.logged_in = False
        st.rerun()

    # Добавяне на книга
    st.subheader("Добавяне на книга")
    new_book = st.text_input("Въведете заглавие на книга")

    if st.button("Добави"):
        if new_book != "":
            st.session_state.books.append(new_book)
            st.success("Книгата е добавена!")
        else:
            st.warning("Моля, въведете заглавие!")

    # Статистика
    st.subheader("Статистика")
    total = len(st.session_state.books)
    st.metric("Общ брой книги", total)

    # Показване на всички книги
    st.subheader("📖 Всички книги")
    if len(st.session_state.books) == 0:
        st.info("Библиотеката е празна!")
    else:
        for book in st.session_state.books:
            st.write("📖", book)

    # Търсене на книга
    st.subheader("Търсене на книга")
    search = st.text_input("Каква книга търсите?")

    if st.button("Търси"):
        found = False
        for book in st.session_state.books:
            if search.lower() in book.lower():
                st.success("Намерена книга: " + book)
                found = True
        if found == False:
            st.warning("Няма такава книга!")

    # Изтриване на книга
    st.subheader("Изтриване на книга")
    if len(st.session_state.books) > 0:
        selected_book = st.selectbox("Изберете книга:", st.session_state.books)
        if st.button("Изтрий"):
            st.session_state.books.remove(selected_book)
            st.success("Книгата е изтрита!")
            st.rerun()
    else:
        st.info("Няма книги за изтриване!")

    # Сортиране
    st.subheader("Сортиране")
    if st.button("Сортирай по азбучен ред"):
        st.session_state.books.sort()
        st.rerun()
