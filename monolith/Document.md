
# cloudProject

دیتاست این پروژه تاریخچه فروش بازی ها از سال  1980 تا 2020 بر روی پلتفرم های متفاوت است و به این دلیل انتخاب شده است که می توانداطلاعات مفیدی درباره صنعت بازی را در اختیار ما قرار دهد.


این پروژه متشکل از سرویس های زیر است:

- سرویس authentication:  که در این سرویس کاربر نام کاربری و رمز خود را وارد می کند و در جواب به او یک توکن داده می شود.

- سرویس game: در این سرویس کاربر می تواند تمامی اطلاعات مربوط به بازی را من جمله بدست آوردن بازی بر اساس رتبه، سال انتشار، نام و ژانر بدست آورد.

- سرویس analysis:  در این سرویس کاربر می تواند نمودار های مربوط به سرویس قبل را مشاهده کند.

 سرویس های authentication و analysis به شدت به سرویس game وابسته بودند و این موضوع باعث شد تا نمودار ها را از درخواست های اصلی جدا کنیم. 
 برای گرفتن پاسخ از بقیه سرویس ها لازم تا token ای به آن ها داده شود که این خود نشان دهنده وابستگی بقیه سرویس ها به سرویس authentication است.
 
![image](https://user-images.githubusercontent.com/46274547/166003550-fbaac073-ef0d-4047-99e7-a04570d16319.png)

![image](https://user-images.githubusercontent.com/46274547/166003800-184fd1eb-9825-44e3-801e-57000230a4ec.png)

در تمامی سرویس ها token چک می شود.

## Authentication service
در این سرویس کاربر نام کاربری خود را با کلید username در body درخواست به صورت form data قرار می دهدودر پاسخ توکن را دریافت میکند.

`POST /api/user/sign_in/`



## Game service

در این سرویس اطلاعات مربوط به بازی قرار دارد.

`GET /api/data_sales/search_by_name/<name>/`

با استفاده از این api می توان با نام بازی اطلاعات مربوط به بازی را گرفت.  



`GET /api/data_sales/search_by_platform/<paltform>/<pk>`

با استفاده از این api میتوان با اسم platform در بازی ها جستجو کرد و اطلاعات بازی ها را گرفت.



`GET /api/data_sales/search_by_rank/<rank>`

در این  api میتوان اطلاعات تمامی بازی هایی که rank آن ها برابر با رنک داده شده است گرفت.


`GET /api/data_sales/search_by_year/<year>/<pk>`

با استفاده از این api می توان تمامی بازی هایی که در سال خاصی منتشر شده اند را گرفت.


`GET /api/data_sales/search_by_genre/<genre>/<pk>`

با استفاده از این api میتوان تمامی بازی در ژانر خاصی را گرفت.


`GET /api/data_sales/all_data/`

با استفاده از این api میتوان تمامی بازی ها را گرفت.

`GET /api/data_sales/best_games/<paltform>/<year>`

با استفاده از این api می توان بهترین بازی هایی را در یک پلتفرم و سالی خاص منتشر شده اند را گرفت.

`GET /api/data_sales/search_by_greater_euro/`

بااستفاده از این api می توان تمامی بازی هایی که در اروپا فروش بالایی داشتند را گرفت .



## Analysis service

`/api/analyse_sales/compare_game/chart/<name>/<name>`

این api اسم دو بازی مختلف را میگیرد و با استفاده از اسم آن ها را مقایسه کرده و نموداری در قالب html درست می کند.


`/api/analyse_sales/compare_sale_by_year/chart/<year>/<year>/`

این api سال های انتشار دو بازی مختلف را میگیرد و با استفاده از سال انتشار آن ها را مقایسه کرده و نموداری در قالب html درست می کند.


`/api/analyse_sales/compare_publisher_by_year/chart/<Publisher>/<Publisher>/<year>/<year>/`

این api ناشر و سال انتشار دو بازی مختلف را میگیرد و با استفاده آن ها ناشرها را مقایسه کرده و نموداری در قالب html درست می کند.


`/api/analyse_sales/compare_genre_by_year/chart/<year>/<year>/`

این api  سال های انتشار دو بازی مختلف را میگیرد و با استفاده آن سال ژانرهای مختلف را مقایسه کرده و نموداری در قالب html درست می کند.

