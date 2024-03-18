import streamlit as st
import datetime
from urllib.parse import quote

def test():
    # 現在の日付と時刻を取得
    now = datetime.datetime.now()

    # 年、月、日を変数に格納
    year = now.year
    month = now.month
    day = now.day
    # Streamlit API の title を使用して文字表示
    st.title("Googleカレンダーリンクを作ろう！")
    carender_title = st.text_input("件名")
    quoted_title = quote(carender_title)
    st.write(quoted_title)
    min_date = datetime.date(year, month, day)
    max_date = datetime.date(2100, 12, 31)
    target_day = st.date_input("日付",  min_value=min_date, max_value=max_date)
    day = target_day.strftime("%Y%m%d")
    st.write(day)
    times = st.slider(
        "時間",
        value=(datetime.time(21, 30), datetime.time(23, 00)))
    s_hour,s_minute,e_hour,e_minute = (str(times[0].hour).zfill(2),str(times[0].minute).zfill(2),str(times[1].hour).zfill(2),str(times[1].minute).zfill(2))
    st.write(s_hour,s_minute,e_hour,e_minute)
    quoted_details = ""
    carender_details = st.text_input("詳細")
    if carender_details != "":
        quoted_details = f"details={quote(carender_details)}"


    if carender_title != "":
        URL_text = ("https://www.google.com/calendar/render?action=TEMPLATE&text="
                    + quoted_title +"&"
                    + f"dates={day}T{s_hour}{s_minute}00/{day}T{e_hour}{e_minute}00"+"&"
                    +quoted_details)
        st.write(URL_text)
#     st.write(f"""
# https://www.google.com/calendar/render?action=TEMPLATE&text={}
# dates={}T{}{}00/{}T{}{}00&
# details={}&
# location={}&
# sprop={}""")
if __name__ == '__main__':
    test()