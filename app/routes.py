from flask import render_template
from app import app
from app.cluster_algo import cluster_articles, cluster_product_images


news_articles = [
   "Breakthrough in Renewable Energy: New Solar Technology Promises 50% Increase in Efficiency",
   "Global Leaders Unite for Climate Action: Historic Agreement Reached at Environmental Summit",
   "Medical Marvel: Researchers Develop Promising New Treatment for Common Neurological Disorder",
   "Space Exploration Milestone: First Human Mission to Mars Successfully Launched",
   "Tech Giants Collaborate on Groundbreaking Artificial Intelligence Ethics Framework",
   "Record-Breaking Art Auction: Masterpiece Sells for Staggering $150 Million",
   "Young Entrepreneur Revolutionizes Urban Farming with Innovative Vertical Agriculture System"
]
images = [
    '/static/images/basketball1.jpg',
    '/static/images/basketball2.jpg',
    '/static/images/cooking1.jpg',
    '/static/images/cooking2.jpg',
    '/static/images/laugh1.jpg',
    '/static/images/run1.jpg',
    '/static/images/run2.jpg'
]
text_descriptions = [
    'Basketball',
    'Basketball',
    'Cooking',
    'Cooking',
    'Laughing',
    'running',
    'running'
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster/articles')
def cluster():
    # Perform clustering on the list of news articles
    clustered_data = cluster_articles(news_articles)

    # Pass clustered data to the template
    return render_template('results.html', clusters=clustered_data)

@app.route('/cluster/images')
def cluster_images():
    # Perform clustering on the list of news articles
    clustered_images = cluster_product_images(images, text_descriptions)

    # Pass clustered data to the template
    return render_template('results2.html', clustered_images=clustered_images)