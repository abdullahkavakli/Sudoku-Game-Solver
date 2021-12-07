Developed a UI(by Pygame) to play the game of Sudoku, implemented a solver feature that uses the backtracking algorithm to find a solution to any solvable game. To start solver, press SPACE. 

With solver feature, matrixes tht is unsolved is solved by the code.

For solver feature, backtracking algorithm is used.

For DB connection i used MsSQL. You can find backup file.(If you don't know how to restore a database from .bak file you can find from this tutorial: https://www.youtube.com/watch?v=mr8Lpkx5yag)

Run sudoku_GUI.py to play sudoku.

![](img/sudoku-gif.gif)

To run, change your server name with "Server=YOURSERVERNAME;" in dbconnection.py. You can find your server name from msSQL:

![](img/db-connection.jpg)

Tr özet:

Sudoku Oyunu & Çözücü|Python, MsSQL

•Arayüz için Pygame kütüphanesi kullanılarak yazılmış bir sudoku oyunudur.

•Sudoku çözücü özelliği sayesinde MsSQL veritabanından aldığı çözülmemiş sudoku matrislerini çözerek yeni oyun için kullanıyor.
•Geri izleme algoritması kullanılarak çözücü görselleştirmesi eklendi.
Veritabanı bağlantısı için MsSQl kullanıldı.(.bak dosyasından veritabanının restore edileceğini bilmiyorsanız şuradan izleyebilirsiniz: https://www.youtube.com/watch?v=mr8Lpkx5yag)
