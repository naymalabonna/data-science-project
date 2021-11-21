# What's Cooking?

### Group Members
- Atiya Mirza
- Nayma Labonna

### Repository Structure
- `data`
  - `train.json`: The training set containing recipes id, type of cuisine, and list of ingredients.
  - `test.json`: The test set containing recipes id, and list of ingredients.
  - `train_data_dictionary.json`: The data dictionary for cleaned.

- `code`
  - `etl_recipes.py`: Cleans `train.json` and `test.json`, returns cleaned list of ingredients.
  - `exploratory_data_analysis.ipynb`: Includes descriptive statistics and charts.
  - `build_model.py`: Builds Neural Network model. (yet to be added)

### Exploratory Analysis
We explored some of the main characteristics of the data including the total number of recipes and ingredients. We 
also determined the number of unique cuisines, the total number of recipes for each unique cuisine, the total number
of unique ingredients, and the total number of recipes for each unique ingredient. This helped increase our
understanding of which ingredients could be more/less useful in determining the cuisine that a recipe belongs to. 

### Challenges
At first glance, we did not think our data sets needed cleaning, especially since it consists of only three aspects (id, cuisine, and ingredients). However, upon further inspection of the data set, we realized that it did in fact need cleaning, and it was a challenge to figure out what exactly we should alter to ensure not only that it will be easy to work with for future use, but also that it would not hinder our model's accuracy. 
### Future Work
Describe what work you are planning to complete for the final analysis.
Since we did not begin creating our model yet, our future work consists of creating a Neural Network Classification Model using Keras.

### Contributions
This project was fully collaborative. 
