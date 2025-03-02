import fitz  
<<<<<<< HEAD
from pdfminer.high_level import extract_text
=======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

#configuring selenium (for overcoming 403 and SSLCertificate Errors)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

#setting up webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#disguise
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
>>>>>>> 37a6753 (Stufff)

def extract_pdf_text(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text")
    return text

def text_to_markdown(text):
    lines = text.splitlines()
    markdown = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(" " * 4): 
            markdown += f"- {line.strip()}\n"
        elif line.isupper() and len(line) < 50:
            markdown += f"# {line}\n"
        else:
            markdown += line + "\n"
    return markdown

if __name__ == '__main__':
    pdf_text = extract_pdf_text("pdfs/apUSGovfrq.pdf")
    markdown_text = text_to_markdown(pdf_text)
    print(markdown_text)
