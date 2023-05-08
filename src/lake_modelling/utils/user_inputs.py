import streamlit as st


def get_lake_params():
    st.markdown("### Lake characteristics")
    col1, col2 = st.columns(2)

    area = col1.number_input("Area [km2]", min_value=0.0, value=0.2)
    tau = col1.number_input("Residence time [years]", min_value=0.0, value=0.7)
    ph = col1.number_input("Initial pH [-]", min_value=1.0, max_value=11.0, value=5.5)
    mean_depth = col2.number_input("Mean depth [m]", min_value=0.0, value=5.0)
    flow_profile = (
        col2.selectbox("Flow profile", ("None", "Fjell", "Kyst"), index=0)
    ).lower()
    colour = col2.number_input("Initial colour [mgPt/l]", min_value=0, value=4)

    lake_params = (area, mean_depth, tau, flow_profile, ph, colour)

    return lake_params


def get_duration():
    st.markdown("### Model setup")
    n_months = st.number_input("Number of months to simulate", min_value=1, value=12)
    return n_months


def get_lim_param(products):
    st.markdown("### Liming product")
    col1, col2 = st.columns(2)

    lime_prod = col1.selectbox("Choose liming product", (products))
    lime_dose = col1.number_input(
        'Liming "dose" [mg-lime/l]', min_value=0.0, value=10.0
    )
    lime_month = col1.number_input(
        "Month in which lime is added",
        max_value=12,
        value=1,
        min_value=1,
    )
    spr_meth = col2.selectbox("Choose distribution method", ("Wet", "Dry")).lower()
    K_L = col2.number_input(
        "Lime dissolution rate on the bottom of the lake [month^-1]",
        min_value=0.0,
        value=1.0,
    )
    F_sol = col2.number_input(
        'Proportion of lake-bottom lime that remains "soluble"',
        min_value=0.0,
        max_value=1.0,
        value=0.4,
    )

    lim_param = (lime_prod, lime_dose, lime_month, spr_meth, K_L, F_sol)

    return lim_param
