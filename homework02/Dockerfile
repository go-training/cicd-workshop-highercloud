# 使用官方的 Python 基礎映像檔
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝 Python 依賴項
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼
COPY . .

# 暴露應用程式運行的端口
EXPOSE 8000

# 運行 FastAPI 應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
