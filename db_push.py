import pandas as pd
from requests import get
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Graduate, Base


def get_xlsx(url):
    req = get(url, verify=False)
    # not recommended
    if req.status_code is 200:
        return req.content
    print("Error: {}".format(req.status_code))
    return None


def connect_to_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()


def push_xlsx_to_db(df, session):
    for index, row in df.iterrows():
        session.add(Graduate(السنة_الدراسية=row['السنة الدراسية'],
                             المرحلة_الدراسية=row['المرحلة الدراسية'],
                             المستوى_الدراسي =row['المستوى الدراسي'],
                             نوع_المؤسسة_التعليمية=row['نوع المؤسسة التعليمية'],
                             المنطقة_الإدارية=row['المنطقة الإدارية'],
                             المحافظة=row['المحافظة'],
                             نوع_الجهة=row['نوع الجهة'],
                             الجهة_التعليمية=row['الجهة التعليمية'],
                             المجال_الواسع=row['المجال الواسع'],
                             المجال_الضيق=row['المجال الضيق'],
                             المجال_التفصيلي=row['المجال التفصيلي'],
                             نظام_الدراسة=row['نظام الدراسة'],
                             الجنس=row['الجنس'],
                             الجنسية=row['الجنسية'],
                             العدد=row['العدد']))
        session.commit()


def main():
    # get excel file
    url = 'https://data.gov.sa/Data/ar/dataset/ce41f22c-dddc-411a-b40f-e8acb6c835ec/resource/e21fea7f-3659-4714-ab32' \
          '-8bf3b0e50eb1/download/number-of-graduates-by-field-of-study-2013-2018.xlsx '
    xlsx = get_xlsx(url)

    # exit if file fails to download
    if xlsx is None:
        exit(1)

    # load excel file in pandas
    df = pd.read_excel(xlsx)

    # connect to db
    db_url = 'postgresql://alraedah_user:plain_text@localhost/graduate'
    session = connect_to_db(db_url)
    # push excel rows in to past
    push_xlsx_to_db(df, session)

    print("all the excel rows have been added to the database")


if __name__ == '__main__':
    main()


