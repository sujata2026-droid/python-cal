import streamlit as st


# 1. ページのタイトル
st.title("sujata")
st.write("数値を入力して計算ボタンを押してください。")


# 2. 入力フォームの作成
num1 = st.number_input("1つ目の数値を入力", value=0.0)
num2 = st.number_input("2つ目の数値を入力", value=0.0)


# 3. 四則演算の選択肢
operation = st.selectbox("計算方法を選択", ["足し算 (+)", "引き算 (-)", "掛け算 (×)", "割り算 (÷)"])


# 4. 計算ボタンと処理
if st.button("計算する"):
    result = 0
    error_message = None
    
    if operation == "足し算 (+)":
        result = num1 + num2
    elif operation == "引き算 (-)":
        result = num1 - num2
    elif operation == "掛け算 (×)":
        result = num1 * num2
    elif operation == "割り算 (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            error_message = "エラー: 0で割ることはできません！"


# 5. 結果の表示
    if error_message:
        st.error(error_message)
    else:
        st.success(f"計算結果: {result}")