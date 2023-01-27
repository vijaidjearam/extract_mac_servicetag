Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/vijaidjearam/extract_mac_servicetag/main/extract-macadress-servicetag.py" -OutFile "C:\Users\WDAGUtilityAccount\Desktop\extract-macadress-servicetag.py"
choco install -y python3 tesseract
[System.Environment]::SetEnvironmentVariable('TESSDATA_PREFIX','C:\Program Files\Tesseract-OCR\tessdata')
New-Item -ItemType Directory -Path c:\ -Name temp
$Env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") 
python.exe -m pip install --upgrade pip
pip install pytesseract pillow
