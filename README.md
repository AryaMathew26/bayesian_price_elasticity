# Why Bayesian?
Predicts the line as well as the credible interval (uses probability/ likelihood of point falling between points)

# How does bayesian come up with credible interval?
Markov Chain Monte Carlo (MCMC) - special optimisation technique that lets us do a lot of sampling, and then come up with a probability distribution, based on where the data falls
Which allows us to do things like understand our models risk
And the Bayesian model tells us exactly how to price our products to 
- maximize sales and 
- limit downside risk

# About
 - Introduction to non-linear models for price elasticity
 - Use hierarchical modeling for product groups
 - Probabilistic modeling using Markov Chain Monte Carlo (MCMC) Stan
 - Change variance by group+


# Bayesian Price Elasticity in Python

This project is a Python conversion of the original R/brms Bayesian
price elasticity lab.

The original R project uses:

- `tidyverse`
- `tidymodels`
- `bayesian`
- `brms`
- `tidybayes`
- `ggplot2`

The Python version uses:

- `pandas`
- `numpy`
- `PyMC`
- `ArviZ`
- `matplotlib`
- `scikit-learn`

## Current conversion status

Completed:

1. Project setup and data loading
2. Model 1: Bayesian linear regression
3. Model 2: global Bayesian GAM / spline regression
4. Model 3: Hierarchical Bayesian GAM by product
5. Model 4: Heteroskedastic hierarchical Bayesian model
6. Prediction and price optimisation workflow

## Project structure

```text
bayesian_price_elasticity_python/
├── data/
│   └── iphone_case_daily_sales.csv
├── figures/
│   └── generated plots will be saved here
├── models/
│   └── generated model outputs will be saved here
├── notebooks/
│   ├── README.md
│   ├── 01_model1_linear.ipynb
│   ├── 02_model2_gam.ipynb
│   ├── 03_model3_hierarchical_gam.ipynb
│   └── 04_model4_heteroskedastic.ipynb
├── utils/
│   ├── __init__.py
│   └── data_loader.py
├── main.py
├── model1_linear.py
├── model2_gam.py
├── model3_hierarchical.py
├── model4_heteroskedastic.py
├── requirements.txt
└── README.md
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Inspect the data

```bash
python main.py
```

## Run Model 1

```bash
python model1_linear.py
```

or:

```bash
python main.py --run-model-1
```

## Run Model 2

```bash
python model2_gam.py
```

or:

```bash
python main.py --run-model-2
```

## Run the notebooks

Notebook versions live in `notebooks/` and are designed for learning through
the full modeling workflow step by step:

1. `notebooks/01_model1_linear.ipynb`
2. `notebooks/02_model2_gam.ipynb`
3. `notebooks/03_model3_hierarchical_gam.ipynb`
4. `notebooks/04_model4_heteroskedastic.ipynb`

The first two notebooks mirror the implemented Python scripts. The third and
fourth notebooks include runnable PyMC implementations for the hierarchical
and heteroskedastic models while the corresponding `.py` files remain
placeholders.

## Model 1 explanation

The original R model is:

```r
quantity ~ unit_price
```

The Python/PyMC equivalent is:

```text
quantity_i ~ Normal(mu_i, sigma)
mu_i = alpha + beta * unit_price_i
```

where:

- `alpha` is the global intercept
- `beta` is the price slope
- `sigma` is the residual standard deviation

## Model 2 explanation

The original R model is:

```r
quantity ~ s(unit_price)
```

The Python/PyMC equivalent is:

```text
quantity_i ~ Normal(mu_i, sigma)
mu_i = alpha + spline_function(unit_price_i)
```

In Python, the smooth term is implemented manually:

1. Standardise `unit_price`.
2. Create spline basis columns using `SplineTransformer`.
3. Estimate one Bayesian coefficient for each spline basis column.
4. Combine the basis columns and coefficients to form a smooth demand curve.

Model 2 is nonlinear, so it is better than Model 1 for curved price-demand
relationships. However, it is still global: every product shares the same
smooth curve. Model 3 will fix that by adding product-specific smooths and
hierarchical product effects.

## Generated outputs

Model 1 produces:

- `models/model1_linear_trace.nc`
- `models/model1_linear_predictions.csv`
- `models/model1_price_scaling.txt`
- `figures/model1_linear_predictions.png`

Model 2 produces:

- `models/model2_gam_trace.nc`
- `models/model2_gam_predictions.csv`
- `models/model2_spline_metadata.txt`
- `figures/model2_gam_predictions.png`

Prediction CSV files include:

- `.pred`
- `.pred_lower_95`
- `.pred_lower_66`
- `.pred_upper_66`
- `.pred_upper_95`

These mirror the interval outputs created in the R workflow.
