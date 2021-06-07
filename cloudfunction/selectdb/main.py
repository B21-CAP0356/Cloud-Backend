import sqlalchemy
from flask import jsonify
from sqlalchemy.dialects.mysql import JSON
import json

connection_name = "project-name:region-zone:database-name" #feel with your HTTP trigger link
table_name = "disaster_report"
table_field = "keterangan,nama,deskripsi,alamat,tanggal,image"
db_name = "user_report"
db_user = "root"
db_password = "password" #feel with your instance password

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

def select(request):
    request_json = request.get_json()
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
    conn = db.connect()
    data = conn.execute('select *from disaster_report')
    rows = data.fetchall()
    objects_list = []
    for row in rows:
        objects_list.append({
          'id_v':row[0],
          'keterangan_v':row[1],
          "nama_v":row[2],
          "deskripsi_v":row[3],
          "alamat_v":row[4],
          "tanggal_v":row[5],
          "image_v":row[6]})
    j = objects_list

    return jsonify(j)
