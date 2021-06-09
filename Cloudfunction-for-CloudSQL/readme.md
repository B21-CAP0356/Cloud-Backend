### Insertdb is used for inserting record to your CLOUD SQL database.

# To trigger the insertdb function :

You can use POST command with curl or java

## Curl
you can use this in your terminal

```bash
curl --location --request POST 'https://asia-southeast2-xxxx-xxxxx-xxxxxx.cloudfunctions.net/insertdb' \
--header 'Content-Type: application/json' \
--data-raw '{
    "keterangan_v": "jembatan",
    "nama_v": "ctes",
    "deskripsi_v": "ctes",
    "alamat_v": "ctes",
    "tanggal_v": "2021-06-02",
    "image_v": "http:image link"
}'
```

## Java
you can use java for putting the POST command in your android application
```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"keterangan_v\": \"jembatan\",\r\n    \"nama_v\": \"nama pelapor\",\r\n    \"deskripsi_v\": \"deskripsi kerusakan\",\r\n    \"alamat_v\": \"lokasi bangunan rusak\",\r\n    \"tanggal_v\": \"2021-06-02\",\r\n    \"image_v\": \"http:image link\"\r\n}");
Request request = new Request.Builder()
  .url("https://asia-southeast2-xxxx-xxxxx-xxxxxx.cloudfunctions.net/insertdb")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```
### Selectdb is used for getting all your CLOUD SQL record in json format.
# To trigger the selectdb function :

You can use GET command with curl or java

## Curl
you can use this in your terminal

```bash
curl --location --request GET 'https://asia-southeast2-xxxxx-xxxxxx-xxxxxx.cloudfunctions.net/selectdb'
```

## Java
you can use java for putting the GET command in your android application
```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("https://asia-southeast2-xxxxx-xxxxxx-xxxxxx.cloudfunctions.net/selectdb")
  .method("GET", null)
  .build();
Response response = client.newCall(request).execute();
```
