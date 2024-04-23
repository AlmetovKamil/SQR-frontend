# Import necessary libraries
import streamlit as st
from streamlit_star_rating import st_star_rating

from sample_books import books

# Sample book data (you can replace this with actual data from your external API)

def on_details_click():
    st.switch_page('pages/book_page.py')


st.set_page_config(page_title="BRP", page_icon="📚", layout="wide")
st.session_state.selected_book = None

# Streamlit app layout
st.title("Book Review Platform (BRP)")

# Sidebar widgets
st.sidebar.title("Filters")
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + list(set(book.genre for book in books)))
selected_rating = st.sidebar.slider("Select Minimum Rating", min_value=1.0, max_value=5.0, step=0.1, value=3.0)
n_columns = 4
# Display filtered book reviews
st.header("Filtered Book Reviews")
for i, book in enumerate(books):
    if selected_genre == "All" or book.genre == selected_genre:
        if book.rating >= selected_rating:
            
            if i % n_columns == 0:
                columns = st.columns(n_columns)
            with columns[i % n_columns]:
                # Book Tile
                with st.container(border=True):
                    st.image(book.cover_image_url, caption=book.author, use_column_width=True)
                    st.subheader(book.title)
                    st.write(f"Genre: {book.genre.name}")
                    stars = st_star_rating("", maxValue=5, defaultValue=book.rating, key=i, size=25, read_only=True)
                    if st.button('Details', key=i+10000):
                        st.session_state.selected_book = book
                        st.switch_page('pages/book_page.py')
                    
                

# Display personalized book recommendations (you can customize this section)
st.header("Personalized Book Recommendations")
st.write("Based on your reading history and preferences, we recommend the following books:")
# Add recommended book details here...

# Footer
st.markdown("---")
st.write("Explore more books and join the discussion on BRP!")
