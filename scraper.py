import requests

product_code = input("Podaj kod produktu: ")
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
responds = requests.get(url)
print(responds.status_code)
