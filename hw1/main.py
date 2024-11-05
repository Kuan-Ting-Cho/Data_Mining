from apriori import apriori
from fp_growth import fp_growth

if __name__ == "__main__":
    test_data = './input/2022-DM-release-testdata-2.txt'
    kaggle_data = './input/Market_Basket_Optimisation_kaggle.txt'

    apriori(test_data, 0.1, 0.1)

    fp_growth(test_data, 0.1, 0.1)
    
    apriori(kaggle_data, 0.03, 0.1)

    fp_growth(kaggle_data, 0.03, 0.1)

    

    