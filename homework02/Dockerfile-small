# 第一階段：構建階段
FROM python:3.11 AS builder

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝 Python 依賴項
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼
COPY . .

# 第二階段：運行階段
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 從構建階段複製已安裝的依賴項
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 複製應用程式程式碼
COPY --from=builder /app /app

# 暴露應用程式運行的端口
EXPOSE 8000

# 運行 FastAPI 應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
