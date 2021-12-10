# What's Cooking?

Have you ever wondered where the food you eat everyday comes from? Have you ever thought about how every part of the world eats their own distinct type of food? Eating is an essential part of life, culture, and nationality. The dishes we eat have their own identity and are tied to a lineage of cuisine. Food transcends the barrier of language and culture, telling a story and bringing people closer with every bite. Immigration and cultural diffusion gave us the privilege of being able to try foods that we would have never been able to taste otheriwse. Have you ever wanted to cook a meal from a cuisine using the ingredients you already have at home? Have you ever been curious about which ingredients certain cuisines use the most in their dishes? If you relate to any of the previous questions, this project may be of interest to you. 

### Motivation

The problem we were trying to solve with this project was being able to match a recipe to a cuisine based on its ingredients only, more precisely, “Which cuisine does a recipe’s ingredients belong to?” Apart from food being such a crucial part of our lives, we chose this problem because we both love food and cooking, and thought it was an interesting topic because we knew that there can be a lot of overlap of ingredients in many cuisines, so we wanted to try and attempt to make a model that would help differentiate them. Here is an example on how this would work. Let's say you have the following ingredients and want to know which cuisine you can cook a meal from with them:

- sugar
- salt
- fennel bulb
- water
- lemon olive oil
- grapefruit juice

Can you guess which cuisine these ingredients belong to? It isn't very easy, but if you guessed French, you'd be correct! Our model can take the guess-work out of this problem. The goal is to be able to predict the category of a dish’s cuisine given a list of its ingredients. We found this idea on Kaggle and thought it would be a fun and interesting way to test if it really is that simple to categorize food based on ingredients only.

### Data 

The dataset we used comes from Yummly, a smart cooking app that provides recipe recommendations personalized to an individual’s taste. We accessed this data through Kaggle’s website, which we were able to obtain only after making an account on their website and agreeing to the rules of the competition. There are a total or two datasets, the training data, which contains an id, cuisine type, and ingredient list for each recipe. Since our objective is to predict the cuisine type of a recipe, we also have testing data which includes id and ingredient list, but does not include the cuisine field name. The data dictionary for the training data is provided below. 
| **Field Name**  | **Data Type** | **Description** | **Example**  | 
|:-:|:-:|:-:|:-:|
|  id |  int |  the id will help keep track of the data |  1000 |   
|  cuisine |  string |  the cuisine is the type of food |  "Indian" |   
| ingredients   |  list of strings |  the ingredients correspond to a cuisine and belong to a list |  ["turmeric",  "vegetable stock", "tomatoes", "garam masala"] | 

We are limited to the cuisines provided by our dataset, which means that popular and well-known cuisines like Indian, Mexican, Chinese, Italian, etc will be centered in our data. This raises an ethical concern because not every culture’s cuisine will be an available option in the testing of our data, thus marginalizing the lesser known cuisines. Furthermore, many ingredients may overlap in many cultures’ cuisines but not every cuisine will be included in the dataset, so there will be no choice but to generalize the ingredients to an already known cuisine.
Because the data is presented as being so simple, consisting of a maximum of three columns, we initially did not believe that it needed any cleaning. However, upon further analysis and exploration, we realized that our data needed to be pre-processed in a way that would not hinder the accuracy of our model. After removing any special characters and numbers from both datasets, adding lemmatization, and creating a uniform data of lowercase letters, we were satisfisfied with our cleaning and ready to proceed with building our model. 

### Evaluation 

We feel that our logistic regression model performs quite well since the model’s accuracy was determined to be roughly 79%. After further inspecting our classification results using a confusion matrix which allowed us to see the confusion the classifier made, we saw how some cuisines were really well predicted (Moroccan, Thai, Indian) while some suffered from more confusion (Greek and Irish are often predicted as other cuisines). We also viewed our results using a classification report, which showed us the precision, recall, and f1-score values for every cuisine as well as the support which is the number of occurrences of each cuisine in the test set. Though there is always room for improvement in machine learning models, we feel confident about our model’s current performance since its overall accuracy, precision, recall, and f1-scores are all near 80%.

![download](https://user-images.githubusercontent.com/92902065/145545580-700d073f-bffb-4715-9480-a1d97efa7f5c.png)
![Screen Shot 2021-12-10 at 3 49 07 AM](https://user-images.githubusercontent.com/92902065/145545587-d3b15c4e-3e8c-4322-8232-76a771655487.png)




