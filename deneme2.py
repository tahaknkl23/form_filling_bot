import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Tarayıcıyı başlat
driver = webdriver.Edge()  # Edge için

# Web sayfasını aç
driver.get("Giris ysayfası url ")  # Giriş sayfasının URL'si

# Sayfanın tam yüklenmesini bekle
driver.implicitly_wait(10)

# Kullanıcı adı ve şifre alanlarını bul
username_field = driver.find_element(By.NAME, "Username")  # Kullanıcı adı alanının ismi
password_field = driver.find_element(By.NAME, "Password")  # Şifre alanının ismi

# Kullanıcı adı ve şifre bilgilerini gir
username_field.send_keys("**********")
password_field.send_keys("**********")

time.sleep(2)  # 2 saniye bekle

# Giriş yap butonuna bas
login_button = driver.find_element(By.CLASS_NAME, "giris")  # Giriş yap butonunun ismi
login_button.click()

# Yeni form oluştur butonunun yüklenmesini bekle ve tıkla
new_form_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.card-footer.text-center"))
)
new_form_button.click()

# Yeni sayfanın yüklenmesini bekle
time.sleep(2)

# "Gebe Veri Toplama Formu" kartını bul ve tıkla
gebe_form_card = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//h4[text()='Form']/ancestor::div[@class='card']//a"))
)
gebe_form_card.click()

# Eğer formda herhangi bir seçim yapman gerekiyorsa, burada kodu ekle
# Örneğin, ders seçim kutusunu bul ve bir seçenek seç
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text("Seçenek 1")

time.sleep(2)  # 2 saniye bekle

# İşlem tamamlandığında tarayıcıyı kapat
driver.quit()
