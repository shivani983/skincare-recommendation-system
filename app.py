import pickle
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("artifacts/dataset/clean_data/clean_cosmetics_data.csv")  # Or wherever your clean data is
final_features = pickle.load(open("artifacts/dataset/transformed_data/transformed_cosmetics.pkl", "rb"))
indices_dict= pickle.load(open("artifacts/serialized_objects/indices.pkl", "rb"))
knn_model = pickle.load(open("artifacts/trained_model/knn_model.pkl", "rb"))

def get_recommendation(value, based_on='product_name', n=5):
    # Map the input column to its index
    index_map = {
        'product_name': indices_name,
        'labels': indices_label,
        'ingredients': indices_ingredients,
        'brand': indices_brand
    }

    if based_on not in index_map:
        return f"Invalid 'based_on' value: {based_on}. Choose from 'product_name', 'labels', 'ingredients', 'brand'."
    
    if value not in index_map[based_on]:
        return f"No product found with {based_on} = '{value}'"

    idx = index_map[based_on][value]
    distances, indices_knn = knn_model.kneighbors(final_features[idx], n_neighbors=n+1)

    # Exclude the first result (itself)
    recommended_indices = indices_knn.flatten()[1:]

    return df[['Name', 'Brand', 'Label', 'Price', 'Rank', 'Ingredients']].iloc[recommended_indices].reset_index(drop=True)


def main():
    st.set_page_config(page_title="Skincare Recommender", layout="wide")
    st.title("🧼Skincare Product Recommendation System")
    st.markdown("😉🤗Discover your next favorite product based on what you already love! ✨")
    
    indices_name = indices_dict["indices_name"]
    selected_product = st.selectbox("Choose a product you like:", indices_name.index)
    top_n = st.number_input("How many recommendations do you want?", min_value=0, max_value=100, step=5)

    if st.button("Get Recommendations"):
       st.sidebar.title("3 essential steps of skincare")
       st.sidebar.image(r"images\pngtree-cute-baby-girl-washing-face-at-the-morning-with-soap-and-png-image_15280362.png", caption="Cleanse", use_container_width = True)
       st.sidebar.image(r"images\moistorizer.jpg", caption = "moisturize", use_container_width = True)
       st.sidebar.image(r"images\sunscreen.jpg", caption = "protect", use_container_width = True)


       
    #    st.image(["images/cleanser.jpg", "images/moisturizer.jpg", "images/essence.jpg"],
    #          caption=["Cleanser", "Moisturizer", "Essence"],
    #          use_column_width=True)
       
       idx = indices_name[selected_product]
       distances, indices_knn = knn_model.kneighbors(final_features[idx], n_neighbors=top_n+1)
       recommended_indices = indices_knn.flatten()[1:]  # Exclude the selected product itself

       st.subheader("You might also like:")
       st.dataframe(df[['Name', 'Brand', 'Label', 'Price', 'Rank', 'Ingredients']].iloc[recommended_indices].reset_index(drop=True))


# Example usage
if __name__ == "__main__":
    main()



