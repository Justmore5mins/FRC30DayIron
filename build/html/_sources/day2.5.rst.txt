Day 2.5 新建專案
===================

Step 0: 下載WPILib VScode

到 `這邊 <https://github.com/wpilibsuite/allwpilib/releases/tag/v2025.3.2>`_ 下載他的安裝檔之後跑他，他會自己裝好(特別輕鬆)

打開他並且叫出指令列

.. note::
    指令列的叫法有：F1(通用)/ Ctrl+Shift+P(Windows)/ Cmd+Shift+P(MacOS)

然後打Create New Project按Enter就會跳到這個頁面

.. image:: /_static/NewProject.png

最上面那個按鈕先選第一個，他分別有Example(範例)跟Template(模板)，如果是一般要寫機器的專案的話用Template，再來是語言(就是Java)

.. note::
    Python的話用一般的VSCode安裝RobotPy模組

接下來就會跳到一坨會選擇困難症發作的選單，不過只要看前四個就好了。

主要就是Timed Based跟Command Based跟有沒有Skeleton的差別

如果有Skeleton的話他就會註解(幹話)比較少(如果熟悉架構的話用Skeleton會比較舒服)

然後再選擇根資料夾，專案名城(會在根資料夾裡面新增資料夾)與隊號，然後就可以按Create New Project了(感動啜泣)

如果選了Timed Based
----------------------

在新建Timed Based專案之後，除了 :ref:`安裝VendorDeps` 之外，只有要注意一個Robot.java要注意。


.. code-block:: java
    
    public Robot() {} //所有東西的初始化(Initialize)

    @Override
    public void robotPeriodic() {} //機器人的操控(通常不會動這邊)

    @Override
    public void autonomousInit() {} //自動初始化

    @Override
    public void autonomousPeriodic() {} //自動要做的事

    @Override
    public void teleopInit() {} //手動初始化

    @Override
    public void teleopPeriodic() {}//手動要做的事

    @Override
    public void disabledInit() {}//停止的時候的初始化

    @Override
    public void disabledPeriodic() {} //停止的時候要做的事(通常是空的)

    @Override
    public void testInit() {} //測試初始化(通常不會用到)

    @Override
    public void testPeriodic() {}//測試要做的事(通常不會用到)

    @Override
    public void simulationInit() {} //軟體模擬初始化

    @Override
    public void simulationPeriodic() {} //軟體模擬要做的事


如果選了Command Based
----------------------

如果你是選Skeleton的話，他應該只會有三個檔案，但是你還要新增
 | Constants.java
 | subsystems/
 | commands/

用來放專門的東西，`subsystems` 是用來放子系統也就是機構對應的功能，commands就是操控那些機構的指令(只有相對複雜的程式(像是底盤)才要分開來寫，一般來說像是基本的調速度這種用Lambda函數隨便用就好了)

.. note::
    Command Based因為比較複雜所以之後再寫一篇文章來講解

安裝VendorDeps
---------------

可以叫出指令列後找Manage Vendor Libraries>Install new libraries(online)然後再貼連結，或是更簡單的在最左邊那一條找長的很像右上角那個很抽象的Icon一樣的東西，然後再找自己需要的VendorDeps

.. note::
    之後的專案都會在前面先講好需要哪些VendorDeps