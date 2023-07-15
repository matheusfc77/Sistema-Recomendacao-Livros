# Book Recommendation System
Project to recommend books using different approaches

### Important libs
* [Anaconda](https://www.anaconda.com/products/individual)

### V1 - Content-Based Filtering
* After installation of Anaconda execute in the API root path the command `python apiV1.py`
* Run in your laptop the file testAPI.html
* In “Enter Book”, inform a ISBN code (examples in clean_books.csv). Some valid codes: 0002005018, 1841721522, 0553294385
* It will be return a JSON with the ISBN of the top 10 books


### V2 - Collaborative Filtering
* Download  [filtering_recommendation.csv](https://drive.google.com/file/d/1EUAs1wKWLhOyqRibDfLQ7PI77kjyWzDI/view?usp=sharing) and paste in ...\Sistema-Recomendacao_Livros\api\v2\ (the file have 380 MB)
* After installation of Anaconda execute in the API root path the command `python apiV2.py`
* Run in your laptop the file testAPI.html
* In “Enter User”, inform a user ID (examples in filtering_recommendation.csv). Some valid codes: 242, 388, 446, 643
* It will be return a JSON with the ISBN of the top 10 books
