import streamlit as st

from src.lake_modelling.utils.read_products import (
    get_lime_product_names,
    get_lime_products,
)

from src.lake_modelling.utils.ca_model import Lake, LimeProduct, Model

from src.lake_modelling.utils.user_inputs import (
    get_duration,
    get_lake_params,
    get_lim_param,
)

from src.lake_modelling.utils.plot import plot_result

st.set_option("deprecation.showPyplotGlobalUse", False)

LIME_PRODUCTS_DATA = "data/lime_products.xlsx"


def app():
    """Main function for the 'lake_modelling' page."""
    st.markdown("## Lake modelling")

    lake = Lake(*get_lake_params())

    n_months = get_duration()

    products = get_lime_products(LIME_PRODUCTS_DATA)

    prod_name, dose, lime_month, spr_meth, K_L, F_sol = get_lim_param(
        get_lime_product_names(products)
    )
    prod = LimeProduct(prod_name, from_database=True)

    model = Model(lake, prod, dose, lime_month, spr_meth, F_sol, K_L, n_months)

    st.pyplot(fig=model.plot_result())

    return None
