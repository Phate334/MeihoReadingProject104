# 美和科大閱讀計畫成果展示網站 #

這份文件包含說明如何在[GAE](https://appengine.google.com/ "Google App Engine")上架設網站，以及處理課程資料的方法與工具，希望能幫助後續維護網站的助理節省時間。


----------

## 準備測試環境 ##

以下是在開發電腦上會使用到的軟體，大部分不需要額外設定，可以從下列官方網站中取得安裝軟體。

- [Visual Studio Code](https://www.visualstudio.com/zh-tw/products/code-vs.aspx)

如果手邊沒有適當的編輯軟體，推薦使用這個微軟所開發的文字編輯器，可以方便用來修改HTML、JavaScript、CSS。

- [Python 2.7](https://www.python.org/)

目前熱門的開發語言，除了這個網站外其他用來處理資料的工具也是用python撰寫。目前GAE支援的穩定python版本是2.7.X，請在開發電腦上[下載](https://www.python.org/downloads/)安裝該版本。

- [App Engine SDK](https://cloud.google.com/appengine/downloads)

GAE開發套件，可以在開發機器上建立簡單的測試網站。修改後的網站也必須使用該工具上傳至伺服器。

