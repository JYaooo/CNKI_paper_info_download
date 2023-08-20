# CNKI_paper_info_download 
知网大批量文献信息获取与导出     

## 1、前置需求
    因为有大规模获取某主题下、某时间段内的期刊信息，包括题名、关键词、摘要和作者等信息，总数量上万计。
    但是发现知网导出excel表一次最多只能500篇文献，并且需要不断地点按选择。
    遍寻互联网也没有较为合适较新的代码可以使用，所以使用了selenium进行自动化批量获取。

## 2、需求说明
    项目中，对主题为“XX”，刊载期刊类型为北核和南核，时间段2016-2023年的期刊文献进行爬取，并导出excel文件。
    由于每份文件最多为500条数据，需要对获取的表格进行合并。因此项目中有CNKI_export_xls.py/信息获取、combined_excel.py/表格合并两个代码文件。

## 3、环境配置
    Python环境3.8
    配置环境见requirments文件：pip install -r requirements.txt
    另外还需配置selenium中的webdriver与Chrome浏览器版本，版本对应见：https://blog.csdn.net/jylsrnzb/article/details/131492090
    项目中使用的Chrome浏览器版本为103.0.5060.53

## 4、文献信息获取
    首先设置CNKI_export_xls.py中的Chrome驱动路径：chromedriver_path
    时间选择函数start_end_year，选择起始时间。这里推荐以一年为单位，即：2023-2023，随着时间增长，获取页面增多，不稳定性增加，因而选用一年为单位较为保险（血的教训）。
    在search_topic_input.send_keys("XX"),替换所要获取的主题。

## 5、Excel文件格式转换
    由于知网导出的xls文件格式混乱，尝试了很多办法，没有办法用pandas库直接打开，因而可以利用wps、word等另存为xlsx文件。

## 6、文件合并
    将转换后的xlsx文件放置与文件夹下，使用combined_excel.py，替换其中的文件夹路径：folder_path，后进行合并。

## 7、注意
    代码中的sleep停止时间是经过多次试验后，设置认为较为合适的。尽量不要轻易修改，以免频率过快需要输入验证码。

    
