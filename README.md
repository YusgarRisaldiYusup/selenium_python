# mini_project_web_automation_with_python

# Proyek Pengujian Web Automation ini menggunakan Phyton, Pytest, selenium dengan konsep Page Objek Model
-Api ini dibuat berdasarkan web dari saucedemo

Proyek ini mengimplementasikan pengujian otomatis untuk wen menggunakan seleniium dab Pytest sebagai library pengujian dan assertpy sebagai ibrary assertion, proyek ini berbasis page Object Model (POM), Phyton untuk bahasa pemrograman.

## instal library
-pip install -r requirements.txt 

## Tujuan Proyek
- Mengelola dan menjalankan pengujian otomatis untuk fitur log in dan cart 
- Memastikan bahwa fitur berperilaku sesuai dengan spesifikasi dalam berbagai skenario.

## Cara Menjalankan Pengujian
pytest Test/ -s     = run with debug
pytest Test/ -v     = run all test with desc
pytest  Test/       = run all test

## Struktur Proyek
- .helper/test_qase_management.py     = folder/file to integrate with test management tools (exp : QASE.IO)
- .helper/conftest.py            = folder/file to set up driver and send report
- .helper/action.py             = folder/file to setting our reusable action
- .helper/config.py         = folder/file to put reusable variabels
- .Test/share_step.py               = folder/file to make reusable step
- .test                           = folder/file to make our test (exp: unit/e2e/integration/etc)
- pytest.ini                      = folder/file to setting our pytest

 ## Slack Report
  - ![Hasil_running1](msedge_OalUSH1Bts.png)
    
  ## QaseIO Report
  - ![Hasil_running1](msedge_q4cJUb448u.png)

 ## Html(Netlify Deploy) Report
  - ![Hasil_running1](xEZRRy5zMH.png)

---
