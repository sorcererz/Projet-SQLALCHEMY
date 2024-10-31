
import streamlit as st
import pandas as pd
import numpy as np
import models as models
import sqlite3
from models import Genre, Sales, Game, Platform, Publisher, Base
# from sqlalchemy.orm import session
from sqlalchemy import create_engine

from sqlalchemy.orm import Session

import os

from tqdm import tqdm


class createData():

    def createDB(self):
        print('ici')
        try: 
            print('toto')
            os.remove('data/vgsales.db')
            print('remove database')
        except:
            print('no database sqlite')

        engine = create_engine('sqlite:///data/vgsales.db')
        session = Session(bind=engine)


        # st.title('Mon Projet SQL Alchemy - récupération des dinnées pour les transférer dans la bse de données')

        # Nettoyer et préparer les données avec Pandas
        # Charger le fichier "vgsales.csv" dans un DataFrame

        # Création des table dans la base de données
        Base.metadata.create_all(engine)


        vgsales = pd.read_csv("data/vgsales.csv")

        st.dataframe(vgsales)

        ############################################################## names in streamlit

        namesArray = vgsales['Name'].unique()
            
        names_nparray = np.array(namesArray)

        df_names = pd.DataFrame(names_nparray, columns=['Name']).sort_values(by=['Name'])
        st.text('Games names')

        st.dataframe(df_names)

        ############################################################## add Genre in database
        genreArray = vgsales['Genre'].unique()
        for genre in genreArray:
            myGenre = models.Genre(name=genre)
            session.add(myGenre)
        session.commit()

        df_genre = pd.read_sql_table('genres','sqlite:///data/vgsales.db')


        ############################################################## add Platform in database

        platformArray = vgsales['Platform'].unique()
        for plateform in platformArray:
            myPlatform = models.Platform(name=plateform)
            session.add(myPlatform)

        session.commit()

        df_platform = pd.read_sql_table('platforms','sqlite:///data/vgsales.db')
        st.text('df_platform')
        st.dataframe(df_platform)

        ############################################################## add Publisher in database

        publisherArray = vgsales['Publisher'].unique()
        for publisher in publisherArray:
            myPublisher = models.Publisher(name=publisher)
            session.add(myPublisher)

        session.commit()

        df_publisher = pd.read_sql_table('publishers','sqlite:///data/vgsales.db')
        st.text('df_publisher')
        st.dataframe(df_publisher)

        ############################################################## add Game in database

        # gameArray = vgsales['Name','Genre']
        # df_game = pd.DataFrame(vgsales, columns=['Name', 'Genre'])

        for index_game, row_game in vgsales.iterrows():
            for index_genre, row_genre in df_genre.iterrows():
                if row_game['Genre'] == row_genre['name']:
                    # print(row_genre['id'])
                    # print(row_game['Name'])
                    myGame = models.Game(name=row_game['Name'], genre_id=int(row_genre['id']))
                    # print(myGame.__dict__)
                    session.add(myGame)
                    # print('add game')
        session.commit()

        df_game = pd.read_sql_table('games','sqlite:///data/vgsales.db')
        st.text('df_game')
        st.dataframe(df_game)


        ############################################################## add Sales in database

        # df_sale = pd.DataFrame(vgsales, columns=['Other_Sales', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Year', 'Platform', 'Publisher', 'Name'])
        # print(df_platform)
        for index_sale, row_sale in tqdm(vgsales.iterrows()):
        # for index_sale, row_sale in tqdm(df_sale.iterrows()):
            
            mySale = models.Sales()
            mySale.eu_sales = row_sale['EU_Sales']
            mySale.jp_sales = row_sale['JP_Sales']
            mySale.na_sales = row_sale['NA_Sales']
            mySale.other_sales = row_sale['Other_Sales']
            mySale.year_sale = row_sale['Year']
            
            # print('indxe')

            for index_platform, row_platform in df_platform.iterrows():

                # print(row_platform['id'])
                if row_sale['Platform'] == row_platform['name']:
                    # print(row_sale['Platform'])
                    # print(row_platform['name'])
                    mySale.platform_id = row_platform['id']
            for index_publisher, row_publisher in df_publisher.iterrows():
                if row_sale['Publisher'] == row_publisher['name']:
                    mySale.publisher_id = row_publisher['id']
            for index_game, row_game in df_game.iterrows():
                if row_sale['Name'] == row_game['name']:
                    mySale.game_id = row_game['id']
            # print(mySale.__dict__)
            session.add(mySale)
            # print('boucle')
            # print(index_sale)
            # if index_sale > 1:
            #     break
        session.commit()
        print('fini')

