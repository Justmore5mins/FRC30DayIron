Day 1 FRC 簡介
========================

引文
---------

FRC 是 FIRST Robotics Competition 的縮寫，是所有高中機器人比賽的最高殿堂，從1992年開始至今已經舉辦超過30年的比賽，而今年(2024-2025 season)的主題珊瑚逃脫(Reefscape)也是一場相當盛大的賽事。

規則簡介
---------

每場比賽總共由兩個陣營 (Alliance) 合計六支隊伍組成。每隊要在限制體積與重量的情況下製作出他們的機器人，在為時15秒與2分15秒的自動與手動模式大展身手。


.. image:: /_static/alliance.png
    :width: 60%
    :align: center

在自動模式時，人員都不可以操控機器人，只能用提前寫好的路徑讓他去跑，在這個階段，因為沒有人員的手動控制輔助，所以獲得分數的難度較高，所以他會獲得的分數也比較多。

手動模式時，人員就可以利用搖桿遠端遙控機器人，在場上進行廝殺，除了要在自己的隊伍中的分外還要防止對面的隊伍得分，可說是相當累人的一件事情

物件介紹
------------

Coral
+++++++++

.. image:: https://stemos.com.br/wp-content/uploads/2025/01/am-5601.jpg
    :width: 60%
    :align: center

這個就是Coral(俗名叫水管)，是用PVC管裁切而成，在比賽中，可以從地上撿或是從CoralStation 去拿

Alage
++++++++

.. image:: https://www.chiefdelphi.com/uploads/default/original/3X/a/f/afad8866eebaefe0f9315037967d4c07d1a654a2.jpeg
    :width: 60%
    :align: center

這個就是Alage(俗名叫做球)，要從地上撿或是從Reef上弄下來，再把它從processor給Human player或是機器人自己放到Net上來得分，如果給Human Player的話，兩隊都會得到Co-op積分

Reef
+++++++++

.. image:: https://i.ytimg.com/vi/YWbxcjlY9JY/maxresdefault.jpg
    :width: 60%
    :align: center

這個紫色一根一根的東西就是Reef, 我們在取得Coral之後要把它插到這個上面，依據高度有分L1~L4，或者是把原本有在上面的球弄下來

CoralStation
++++++++++++

.. image:: https://i.ytimg.com/vi/Vq2450jd_6s/maxresdefault.jpg
    :width: 60%
    :align: center

這位老兄站的後面的那個東西就是Coral Station, human player會從coral station給出coral(廢話)，這也是coral的主要來源。

Cage
+++++++

.. image:: https://preview.redd.it/do-the-cages-provide-an-added-defense-strategy-v0-gng54qvesebe1.jpeg?auto=webp&s=f0039782d17537e090678db41589df225abc4881
    :width: 60%
    :align: center

Cage有分淺的跟深的，淺的可以直接用電梯把自己撐起來，但是深的因為只有離地九公分所以要另外去想機構設計他。

小複習
+++++++++

.. image:: https://news.okstate.edu/articles/engineering-architecture-technology/images/2025/ceat_hosts_first_robotics_kickoff_competition/first_instory_0.jpg

計分方式
-------------

在比賽開始之前，隊伍可以在Barge選擇要掛淺或深的吊籠(cage)，還有要不要預先插一支Coral到機器上。

在比賽開始後的15秒內是自動模式，隊伍的機器可以利用編程的方式讓機器離開聯盟線(3分)或是把Alage從Reef上弄下來，或是把Coral放到Reef上來得分。

.. image:: /_static/AutoLeave.png
    :width: 60%
    :align: center

.. image:: /_static/CoralScoring.png
    :width: 60%
    :align: center

.. tip::
    在三台機器都有離開聯盟線且至少有一台用Coral得分，可以獲得一個Auto Ranking Poin(不累加)

在接下來的2分15秒內，由操控手操控機器人，他們可以把Alage飛到Net裡面(4分)，或者是從CoralStation與地板上獲取Coral並放到Reef上得分，此時L1得2分L2得3分以此類推。

.. tip::
    如果聯盟在每一層Reef上都有5個Coral的話，就會有Coral Ranking Point

或者是機器也可以把Alage丟到processor(6分)讓human player把它飛到Net裡面(成功飛進去的話會有4分)

.. image:: /_static/AlageProcessor.png
    :width: 60%
    :align: center

.. tip::
    當每個Processer都有放兩個Alage(也就是兩邊都有放兩個)的時候，除了會得到Co-op Point以外，原本是每級Reef都要放才會有的Coral Ranking Point變成只要 3級就會有

在時間快要結束的時候(會有提示聲)，回到那個框框內有2分，吊淺吊籠有6分，深吊籠有12分(非常多)

.. tip::
    只要有一個機器人成功吊上深吊籠而且至少有一個機器人回到框框中，就會有Barge Ranking Point

最後，得分最多的聯盟獲勝

.. note::
    Ranking Point是獨立於比賽中的計分系統，跟字面上的意思一樣，除了比賽的名次以外，Ranking Point也會被參照進排名的依據裡面。

資料來源
-----------

FRC 2025 Kickoff `Video <https://www.youtube.com/watch?v=YWbxcjlY9JY>`_