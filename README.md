# Concrete-Strength-Prediction

## Objective
Concrete is the most important material in Civil Engineering. This is the most common material used in construction of building and infrastructure.
The strength and consistency of concrete determines the integrity of structure being build. Concrete is prepared by mixing various ingredients such as cement, water, fly ash, slag etc. The quantities and proportions are very important to achieve desired strength of the concrete.

This project focuses on developing a model to predict compressive strength of the concrete based on different proportion of ingredients and building a web app where user can enter different quantities of materials to predict compressive strength of the concrete.

## Use-Cases and Advantages (Purpose of The Model)

**Optimizing Material Use:**

It could help in optimizing the use of materials. By knowing exactly how different quantities of ingredients affect the strength of the concrete, one can adjust these quantities to get the desired strength. This could lead to cost savings and more efficient use of materials.

**Improving Quality and Safety:**

It could lead to higher quality and safer construction projects. With the ability to predict concrete strength, engineers could ensure that the buildings and structures they design will be strong and durable.

**Saving Time:**

It could lead to faster decision making. Rather than having to wait for physical concrete samples to cure and then test them, a ML model could predict strength based on ingredient quantities, thereby saving a lot of time.

**Reducing Carbon Footprint:**

Concrete production is responsible for a significant amount of carbon emissions. If we can optimize the mix to achieve the same strength with less cement (the ingredient responsible for most of the emissions), it would help in reducing the carbon footprint.

**Predictive Maintenance and Durability:**

The model could be used to predict the longevity and maintenance requirements of a building or structure based on the quality and strength of the concrete used. This could be invaluable for infrastructure planning and management.

**Automation:**

As ML models can be integrated into other systems, it could contribute to more automated processes in the construction industry. For example, a fully automated system could adjust concrete ingredient quantities on-the-fly to ensure optimal strength based on environmental conditions, specific use cases, and more.

**Research and Development:**

The model could also be used in research and development to discover new concrete mixes and compositions. By adjusting the input parameters (quantities of ingredients), researchers can predict the output (strength) and potentially discover more efficient or effective mixes.

## Dataset Source:

The dataset used for this analysis is downloaded from UCI Machine Learning Repository Website.

## Attributes

The dataset has following 8 attributes:

Cement (component 1) -- quantitative -- kg in a m3 mixture -- Input Variable

Blast Furnace Slag (component 2) -- quantitative -- kg in a m3 mixture -- Input Variable

Fly Ash (component 3) -- quantitative  -- kg in a m3 mixture -- Input Variable

Water  (component 4) -- quantitative  -- kg in a m3 mixture -- Input Variable

Superplasticizer (component 5) -- quantitative -- kg in a m3 mixture -- Input Variable

Coarse Aggregate  (component 6) -- quantitative -- kg in a m3 mixture -- Input Variable

Fine Aggregate (component 7)	 -- quantitative  -- kg in a m3 mixture -- Input Variable

Age -- quantitative  -- Day (1~365) -- Input Variable

Concrete Compressive Strength -- quantitative -- MPa -- Output Variable

## Contents

1. Import Libraries
2. Load Data
3. Data Preprocessing and Exploration
4. Separating Features and Target Label
5. Train Test Split and Scaling the Data
6. Model 1 - Support Vector Machine Model (SVR)
   
   6a. Define and Fit the Model (baseline model)
   
   6b. Evaluation of Base Model
   
   6c. Grid Search in Attempt for Better Model
   
   6b. Determine the Best Estimator and Evaluate on Test Set
   
   6c. Calculate Error Metric (RMSE) and Compare with Baseline Model
   
8. Model 2 - Random Forest Regressor
9. Compare Model 1 and Model 2 Performance and Determine the Best Model
10. Save the Model as Pickle File
11. Develop a web app using Dash Library
12. Deploy the Web App to Heroku
