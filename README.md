# FlaskBackand

Skenario pengujian menggunakan Postman memungkinkan Anda untuk menguji endpoint yang telah Anda buat dalam aplikasi Flask. Berikut adalah skenario pengujian yang mungkin Anda lakukan dengan Postman:

1. Registrasi Pengguna Baru
Metode: POST
URL: http://localhost:5000/register
Body:
json
Salin kode
{
    "username": "john_doe",
    "password": "secure_password",
    "role": "petugas"
}
Header:
bash
Salin kode
Content-Type: application/json
2. Login Pengguna
Metode: POST
URL: http://localhost:5000/login
Body:
json
Salin kode
{
    "username": "john_doe",
    "password": "secure_password"
}
Header:
bash
Salin kode
Content-Type: application/json
3. Menambahkan Data Kondisi Mesin
Metode: POST
URL: http://localhost:5000/add_machine_data
Body:
json
Salin kode
{
    "machine_code": "ABC123",
    "timestamp": "2024-05-21 21:00:00",
    "FEILD_V": 160,
    "FIELD_A": 125,
    "VOLTAGE_BEFORE_TRAFO": 11.2,
    "AFTER_TRAVO_1-2": 33,
    "AFTER_TRAVO_2-3": 33,
    "AFTER_TRAVO_3-1": 33,
    "LOAD_AMP_1": 215,
    "LOAD_AMP_2": 215,
    "LOAD_AMP_3": 215,
    "POWER_ACTOR": 0.86,
    "LOAD_MW_METER": 10.9,
    "M_VAR_METER": 4.0,
    "LIQUID_LEVEL": 7.2,
    "LIQUID_TEMPERATURE": 38,
    "WIND_TEMPERATURE": 40,
    "RECT_TRAFO_LIQUID_TEMP": 53
}
