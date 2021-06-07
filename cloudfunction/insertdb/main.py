import sqlalchemy


connection_name = "project-name:region-zone:database-name" #feel with your HTTP trigger link
table_name = "disaster_report"
table_field = "keterangan,nama,deskripsi,alamat,tanggal,image"
db_name = "user_report"
db_user = "root"
db_password = "password" #feel with your instance password

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If your database is PostgreSQL, uncomment the following two lines:
#driver_name = 'postgres+pg8000'
#query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

def insert(request):
    request_json = request.get_json()
    keterangan_v  = request.get_json().get('keterangan_v')
    nama_v = request.get_json().get('nama_v')
    deskripsi_v = request.get_json().get('deskripsi_v')
    alamat_v = request.get_json().get('alamat_v')
    tanggal_v = request.get_json().get('tanggal_v')
    image_v = request.get_json().get('image_v')
    stmt = sqlalchemy.text('insert into {} ({}) values ("{}","{}","{}","{}","{}","{}")'.format(table_name, table_field, keterangan_v,nama_v,deskripsi_v,alamat_v,tanggal_v,image_v))
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'ok'
