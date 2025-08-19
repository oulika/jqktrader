import jqktrader

user = jqktrader.use()

user.connect(
  exe_path=r'C:\同花顺软件\同花顺\xiadan.exe',
  tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)

print(user.balance)
print(user.buy('sz000001','12.08',100))