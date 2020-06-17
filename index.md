## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/HalfMillennium/flippa-sale-price-predictions/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
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
