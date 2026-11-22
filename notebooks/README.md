# Bayesian Price Elasticity Notebooks

Run the notebooks in this order:

1. `01_model1_linear.ipynb` - global Bayesian linear regression
2. `02_model2_gam.ipynb` - global Bayesian spline regression
3. `03_model3_hierarchical_gam.ipynb` - product-level hierarchical spline regression
4. `04_model4_heteroskedastic.ipynb` - hierarchical spline regression with product-level noise

Each notebook includes:

- data loading and inspection
- an explanation of the model structure
- PyMC model code
- posterior diagnostics
- posterior predictive intervals
- saved outputs in `models/`

The notebook sampling defaults are smaller than the script defaults so they
are easier to run interactively. Increase `DRAWS`, `TUNE`, or `CHAINS` near
the top of each notebook for more stable final inference.
