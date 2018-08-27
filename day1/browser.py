import webbrowser

#webbrowser.open("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="+ "아이유"&&"수지"&&"설현")


keywords = ["아이유","수지","설현"]
for name in keywords:
    url = "https://search.naver.com/search.naver?query=" + name
    webbrowser.open(url)
