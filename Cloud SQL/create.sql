CREATE TABLE disaster_report (
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id),
	keterangan VARCHAR(50),
	nama VARCHAR(30),
	deskripsi VARCHAR(1000),
	alamat VARCHAR(200),
	tanggal DATE,
	image VARCHAR(200)
);
