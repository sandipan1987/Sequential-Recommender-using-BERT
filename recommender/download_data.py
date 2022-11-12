
# importing necessary modules
import requests, zipfile
from io import BytesIO
import os
import pandas as pd
from read_params import get_params

def download_file():
    print('Downloading started')

    #Defining the zip file URL
    url = get_params("data_source_zip")

    # Split URL to get the file name
    filename = url.split('/')[-1]

    # Downloading the file by sending the request to the URL
    req = requests.get(url)
    print('\nDownloading Completed')

    # extracting the zip file contents
    zfile = zipfile.ZipFile(BytesIO(req.content))
    zfile.extractall('./Data/') 

    # folder path
    dir_path = r'./Data/ml-latest-small'

    # list file and directories
    res = os.listdir(dir_path)
    print(res)


def create_csv():
    path = "./Data/InCSV/"
    os.mkdir(path)

    ### creating dataframes for movies from the .dat files
    df_movies = pd.read_table("./Data/ml-10M100K/movies.dat", sep="::", header=None)

    ### renaming the columns
    df_movies.rename(columns={0:"Movie_ID" , 1:"Movie_Name" , 2:"Movie_Genres"},inplace=True)
    df_movies.to_csv(path + 'movies.csv')
    print('\nMovies Converted to CSV')

    ### creating dataframes for ratings from the .dat files
    df_ratings = pd.read_table("./Data/ml-10M100K/ratings.dat", sep="::", header=None)
    ### renaming the columns
    df_ratings.rename(columns={0:"User_ID" , 1:"Movie_ID" , 2:"Rating" , 3:"Timestamp"},inplace=True)
    df_ratings.to_csv(path + 'ratings.csv')
    print('\nRatings Converted to CSV')


    ### creating dataframes for tags from the .dat files
    df_tags = pd.read_table("./Data/ml-10M100K/tags.dat", sep="::", header=None)
    ### renaming the columns
    df_tags.rename(columns={0:"User_ID" , 1:"Movie_ID" , 2:"Tag" , 3:"Timestamp"},inplace=True)
    df_tags.to_csv(path + 'tags.csv')
    print('\nTags Converted to CSV')


if __name__ == "__main__":
    download_file()
    #create_csv()
