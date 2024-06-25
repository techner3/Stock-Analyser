# Stock-Analyser

### Project Overview

This project aims to analyse stocks present in National Stock Exchange (NSE). It analyses the stock by collecting finanical data, respective company news, stock prices and provide a short analysis of the stock.

[](./images/overview.png)

### How to Run ?

1. Create an environment

```bash
conda create -p venv_sa python=3.10 -y

conda activate ./venv_sa
```

2. Install Requirements

```bash
pip install -r requirements.txt
```

3. Create .env file with GROQ_API_KEY and SERPER_API_KEY

4. Run the app.py file

```bash
streamlit run app.py
```

### Preview

Home Page :
[](./images/home.png)

Output

[](./images/output.png)