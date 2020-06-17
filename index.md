# Using Machine Learning to Predict the Sale Price of Digital Asset Auctions on Flippa.com

_An ongoing study by Garrett Chestnut, undergraduate CS student at Stevens Institute of Technology._

_**Commenced:**_ June 8th, 2020  /  _**Last Updated:**_ June 17th, 2020

### Introduction

For the past few years, I have been an active member of the Flippa online community, building and selling many different assets (primarily android applications). During that time I have developed a hypothesis relating to the diversity of asset valuations within sub-industries (e.g., e-commerce websites, domain names, Amazon FBA, etc). By observing auctions unfold, I noticed that bidders cared very little about the content behind each property (i.e., subject-matter, topic, niche) and based most, if not all, of their appraisal on metrics. By “metrics”, I mean traffic, downloads, uniques, profit, age, and other important features.

However, this isn’t surprising. Most of the goods on Flippa sell for less than $5000, making them less significant than the ones sold on sites like Exchange Marketplace, which have a much higher average value. Due to this reality, buyers are less interested in holding onto profitable assets for the long-term, which would require a strong or steadily growing niche, and more concerned in a quick ROI. 

A relatively low-risk method of obtaining an efficient ROI is to invest in assets that are already proving themselves within key metrics. In this study, I have decided to utilize elementary and intermediate machine learning models to determine if asset features (obtained through Flippa’s public API) truly have a high degree of impact on the eventual auction sale price.

_*Note: This first portion of the study has been restricted to premium Flippa listings, since those are more likely to have equal visibility in the marketplace._

---
### Features

The full list of the metrics I used to train my subsequent models is as follows:

- Downloads
- Average profit
- Buy-It-Now price
- Display price
- Listing duration
- Has verified revenue (yes/no)
- Has verified traffic (yes/no)
- Page views per month
- Profit per month
- Asset age
- Property type
- Uniques per month
- Industry

Several of these features depend on the property type, so their values defaulted to zero if they weren’t applicable.

---

My first attempt to develop a relationship between the aforementioned metrics and current price (the dependent variable), was with basic regression (Multiple and Polynomial). I used a dataset with 100 entries, reserving 20 of those for testing.

A prediction was determined to be accurate if it fell within $100 of the true value, or deviated from it by no more than 5% (this definition is consistent throughout my research).

### Basic Regression Accuracy

Multiple Linear Regression | Polynomial Regression _(degree=3)_
------------ | -------------
15% | 15%

Both Multiple Linear and Polynomial Regression managed to make the same number of good predictions, each accurately guessing a different set of 3 out of 20 sale prices. Of course, this is incredibly poor, and offers no significant support for my hypothesis. My next trial utilizes SVR (Support Vector Regression), a more advanced form of regression, in the hopes of establishing a more significant relationship.

### Support Vector Regression (SVR) Accuracy

**Kernel** | **Accuracy**
------------ | -------------
Linear | 0%
RBF (Radial Basis Function) | 20%
Polynomial | 10%
Sigmoid | 5%

Interestingly, the results from SVR were fairly on par with the basic regression techniques. RBF, the most popular Kernel used for SVR, performed the best out of the four, with 20% of its predictions considered close. Below is a graph that displays the prediction results from the RBF kernel alongside the testing values.

![Sale Price Predictions vs Actual Price](https://lh6.googleusercontent.com/gqfwoMVkOY4YUzQR5GMRVD6HcHxgxx-krPYYI-kGy1SDY8TflgAweUt3VTvO_WgYsDeMNJ3nKb_PzaBydg0rY6ipeHRKRLvw9VYlzw-4s2-urNtpiUhwi9CKT--GRyzoOTCp7tTP)
